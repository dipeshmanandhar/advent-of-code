from functools import reduce

from src.common.read_input import read_input


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


input = read_input("input.txt", 2023, 8)

instructions = input[0]
instructions_i = 0
nodes = {
    line.split("=")[0].strip(): tuple(
        line.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")
    )
    for line in input[2:]
}

NODE = "NODE"
Z_NODES = "Z_NODES"
STEPS = "STEPS"
INSTR_I = "INSTR_I"
LOOP_START = "LOOP_START"
LOOP_STEP = "LOOP_STEP"
curr_nodes = [
    {NODE: node, Z_NODES: [], LOOP_START: -1, LOOP_STEP: -1}
    for node in nodes
    if node[2] == "A"
]
num_steps = 0

while True:
    next_step = 0
    if instructions[instructions_i] == "R":
        next_step = 1

    instructions_i = (instructions_i + 1) % len(instructions)
    num_steps += 1

    done = True
    for i in range(len(curr_nodes)):
        if curr_nodes[i][LOOP_STEP] >= 0:
            continue
        curr_nodes[i][NODE] = nodes[curr_nodes[i][NODE]][next_step]
        if curr_nodes[i][NODE][2] == "Z":
            is_loop = False
            for z_node in curr_nodes[i][Z_NODES]:
                if (
                    curr_nodes[i][NODE] == z_node[NODE]
                    and instructions_i == z_node[INSTR_I]
                ):
                    curr_nodes[i][LOOP_START] = z_node[STEPS]
                    curr_nodes[i][LOOP_STEP] = num_steps - curr_nodes[i][LOOP_START]
                    is_loop = True
                    break
            if not is_loop:
                curr_nodes[i][Z_NODES].append(
                    {
                        NODE: curr_nodes[i][NODE],
                        STEPS: num_steps,
                        INSTR_I: instructions_i,
                    }
                )
        if curr_nodes[i][LOOP_STEP] < 0:
            done = False

    if done:
        break
# Now because the input LOOP_STEP is the same as LOOP_START, we just find the LCM of all of the LOOP_STEPS
loops = [x[LOOP_STEP] for x in curr_nodes]
num_steps = lcmm(*loops)

print(num_steps)
