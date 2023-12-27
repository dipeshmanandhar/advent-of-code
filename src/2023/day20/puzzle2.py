from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
from functools import reduce

from src.common.read_input import read_input

TYPE = "TYPE"
DESTS = "DESTS"
BROADCASTER = "broadcaster"
FLIP_FLOP = "%"
CONJUNCTION = "&"
BUTTON = "button"
RX = "rx"
PRINT_STEPS = False


class Pulse(Enum):
    LOW = 0
    HIGH = 1

    def reverse(self) -> Pulse:
        if self == Pulse.LOW:
            return Pulse.HIGH
        else:
            return Pulse.LOW


class Module(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.dests: list[Module] = []
        self.input_pulses: deque[tuple[Pulse, Module]] = deque()
        self.received_low: bool = False

    def add_dest(self, dest: Module) -> None:
        self.dests.append(dest)

    @abstractmethod
    def send_pulse(self) -> tuple[int, int]:
        pass

    def receive_pulse(self, pulse: Pulse, src: Module) -> None:
        self.input_pulses.append((pulse, src))
        if pulse == Pulse.LOW:
            self.received_low = True
        if PRINT_STEPS:
            print(f"{src.name} -{'high' if pulse==Pulse.HIGH else 'low'}-> {self.name}")

    def __repr__(self) -> str:
        return f"[{self.name} -> {', '.join([dest.name for dest in self.dests])}]"


class NoneModule(Module):
    def send_pulse(self) -> tuple[int, int]:
        has_low = any([pulse == Pulse.LOW for pulse in self.input_pulses])
        self.input_pulses.clear()
        if has_low:
            self.input_pulses.append(Pulse.LOW)
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
        self.inputs: dict[Module, Pulse] = {}

    def send_pulse(self) -> tuple[int, int]:
        in_pulse, src = self.input_pulses.popleft()
        self.inputs[src] = in_pulse
        out_pulse = (
            Pulse.LOW
            if all([input == Pulse.HIGH for input in self.inputs.values()])
            else Pulse.HIGH
        )
        for dest in self.dests:
            dest.receive_pulse(out_pulse, self)
        if out_pulse == Pulse.LOW:
            return (len(self.dests), 0)
        else:
            return (0, len(self.dests))

    def add_input(self, input: Module):
        self.inputs[input] = Pulse.LOW


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
        if PRINT_STEPS:
            print()
    return (total_low, total_high)


def gcf(a: int, b: int):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    return a * b // gcf(a, b)


def lcmm(*args: int):
    return reduce(lcm, args)


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

rx_module = None
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
            if dest == RX:
                rx_module = dest_module

# find all modules that send to the module that sends to rx
module_to_rx: ConjunctionModule = None
for module in modules:
    if rx_module in module.dests:
        module_to_rx = module
        break
modules_to_module_to_rx: list[tuple[Module, int]] = [
    (module, -1) for module in module_to_rx.inputs
]


# push_button(modules)


num_button_pushes = 0
while True:
    low, high = push_button(modules)
    num_button_pushes += 1
    if any([pulse == Pulse.LOW for pulse in rx_module.input_pulses]):
        break
    for i, (module, first_button) in enumerate(modules_to_module_to_rx):
        if first_button < 0:
            if module.received_low:
                module.received_low = False
                first_button = num_button_pushes
                modules_to_module_to_rx[i] = (module, first_button)
    if all([first_button >= 0 for _, first_button in modules_to_module_to_rx]):
        break

print(lcmm(*[first_button for _, first_button in modules_to_module_to_rx]))
