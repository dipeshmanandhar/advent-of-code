from src.common.read_input import read_input

input = read_input("input.txt", 2023, 8)

instructions = input[0]
instructions_i = 0
nodes = {
    line.split("=")[0].strip(): tuple(
        line.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")
    )
    for line in input[2:]
}

curr_node = "AAA"
num_steps = 0

while curr_node != "ZZZ":
    if instructions[instructions_i] == "L":
        curr_node = nodes[curr_node][0]
    else:
        curr_node = nodes[curr_node][1]
    instructions_i = (instructions_i + 1) % len(instructions)
    num_steps += 1

print(num_steps)
