from src.common.read_input import read_input


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(monkeys, name='root'):
    monkey = monkeys[name]
    val = None
    left = None
    right = None
    try:
        val = int(monkey)
    except TypeError:
        left, val, right = monkey
    root = Node(val)
    if left:
        root.left = build_tree(monkeys, left)
    if right:
        root.right = build_tree(monkeys, right)
    return root


def calc(root):
    if not root.left and not root.right:
        return root.val
    left = calc(root.left)
    right = calc(root.right)
    if root.val == '+':
        return left + right
    elif root.val == '-':
        return left - right
    elif root.val == '*':
        return left * right
    elif root.val == '/':
        return left // right
    else:
        print('ERROR')
        return None


input = read_input('input.txt', 2022, 21)

monkeys = {}
for line in input:
    name, val = line.split(': ')
    try:
        val = int(val)
    except ValueError:
        val = val.split()
    monkeys[name] = val

root = build_tree(monkeys)


print(calc(root))
