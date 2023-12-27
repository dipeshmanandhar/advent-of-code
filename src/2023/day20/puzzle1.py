from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from enum import Enum

from src.common.read_input import read_input

TYPE = "TYPE"
DESTS = "DESTS"
BROADCASTER = "broadcaster"
FLIP_FLOP = "%"
CONJUNCTION = "&"
BUTTON = "button"
BUTTON_PUSHES = 1000


class Pulse(Enum):
    LOW = 0
    HIGH = 1


class Module(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.dests: list[Module] = []
        self.input_pulses: deque[tuple[Pulse, Module]] = deque()

    def add_dest(self, dest: Module) -> None:
        self.dests.append(dest)

    @abstractmethod
    def send_pulse(self) -> tuple[int, int]:
        pass

    def receive_pulse(self, pulse: Pulse, src: Module) -> None:
        self.input_pulses.append((pulse, src))
        # print(f"{src.name} -{'high' if pulse==Pulse.HIGH else 'low'}-> {self.name}")


class NoneModule(Module):
    def send_pulse(self) -> tuple[int, int]:
        return (0, 0)


class ButtonModule(Module):
    def send_pulse(self) -> tuple[int, int]:
        self.dests[0].receive_pulse(Pulse.LOW, self)
        return (1, 0)


class BroadcastModule(Module):
    def send_pulse(self) -> tuple[int, int]:
        in_pulse, _ = self.input_pulses.popleft()
        for dest in self.dests:
            dest.receive_pulse(in_pulse, self)
        if in_pulse == Pulse.LOW:
            return (len(self.dests), 0)
        else:
            return (0, len(self.dests))


class FlipFlopModule(Module):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.on: bool = False

    def send_pulse(self) -> tuple[int, int]:
        in_pulse, _ = self.input_pulses.popleft()
        if in_pulse == Pulse.LOW:
            self.on = not self.on
            out_pulse = Pulse.HIGH if self.on else Pulse.LOW
            for dest in self.dests:
                dest.receive_pulse(out_pulse, self)
            if out_pulse == Pulse.LOW:
                return (len(self.dests), 0)
            else:
                return (0, len(self.dests))
        else:
            return (0, 0)


class ConjunctionModule(Module):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.inputs: dict[Pulse, bool] = {}

    def send_pulse(self) -> tuple[int, int]:
        in_pulse, src = self.input_pulses.popleft()
        self.inputs[src] = in_pulse == Pulse.HIGH
        out_pulse = Pulse.LOW if all(self.inputs.values()) else Pulse.HIGH
        for dest in self.dests:
            dest.receive_pulse(out_pulse, self)
        if out_pulse == Pulse.LOW:
            return (len(self.dests), 0)
        else:
            return (0, len(self.dests))

    def add_input(self, input: Module):
        self.inputs[input] = False


def push_button(modules: list[Module]) -> tuple[int, int]:
    curr_modules: list[Module] = [modules[0]]
    total_low = 0
    total_high = 0

    while curr_modules:
        next_modules: list[Module] = []
        for src_module in curr_modules:
            low, high = src_module.send_pulse()
            total_low += low
            total_high += high
            if low + high > 0:
                next_modules.extend(src_module.dests)
        curr_modules = next_modules
    return (total_low, total_high)


input = read_input("input.txt", 2023, 20)

modules: list[Module] = [ButtonModule(BUTTON)]
modules_dests: list[str] = [[BROADCASTER]]
for line in input:
    src, dests = line.split(" -> ")
    dests = dests.split(", ")
    module: Module = None
    if src == BROADCASTER:
        module = BroadcastModule(src)
    elif src[0] == FLIP_FLOP:
        module = FlipFlopModule(src[1:])
    elif src[0] == CONJUNCTION:
        module = ConjunctionModule(src[1:])
    modules.append(module)
    modules_dests.append(dests)

for i, src_module in enumerate(modules):
    for dest in modules_dests[i]:
        found_dest = False
        for dest_module in modules:
            if dest_module.name == dest:
                src_module.add_dest(dest_module)
                if isinstance(dest_module, ConjunctionModule):
                    dest_module.add_input(src_module)
                found_dest = True
                break
        if not found_dest:
            dest_module = NoneModule(dest)
            modules.append(dest_module)
            modules_dests.append([])
            src_module.add_dest(dest_module)
            if isinstance(dest_module, ConjunctionModule):
                dest_module.add_input(src_module)


total_low = 0
total_high = 0
for _ in range(BUTTON_PUSHES):
    low, high = push_button(modules)
    total_low += low
    total_high += high

print(total_low * total_high)
