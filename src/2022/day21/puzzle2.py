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
    except ValueError:
        val = monkey
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


def has_human(root):
    if not root.left and not root.right:
        return root.val == 'humn'
    return has_human(root.left) or has_human(root.right)


def rev_calc(root, val):
    if not root.left and not root.right:
        if root.val != 'humn':
            print('ERROR')
        return val
    other_total = 0
    human_on_left = has_human(root.left)
    next_root = None
    next_val = 0
    if human_on_left:
        other_total = calc(root.right)
        next_root = root.left
        if root.val == '+':
            next_val = val - other_total
        elif root.val == '-':
            next_val = val + other_total
        elif root.val == '*':
            next_val = val // other_total
        elif root.val == '/':
            next_val = val * other_total
    else:
        other_total = calc(root.left)
        next_root = root.right
        if root.val == '+':
            next_val = val - other_total
        elif root.val == '-':
            next_val = other_total - val
        elif root.val == '*':
            next_val = val // other_total
        elif root.val == '/':
            next_val = other_total // val

    return rev_calc(next_root, next_val)


def calc_human(root):
    other_total = 0
    human_on_left = has_human(root.left)
    human = 0
    if human_on_left:
        other_total = calc(root.right)
        human = rev_calc(root.left, other_total)
    else:
        other_total = calc(root.left)
        human = rev_calc(root.right, other_total)
    return human


input = read_input('input.txt', 2022, 21)

monkeys = {}
for line in input:
    name, val = line.split(': ')
    try:
        val = int(val)
    except ValueError:
        val = val.split()
    if name == 'humn':
        val = 'humn'
    monkeys[name] = val

root = build_tree(monkeys)


print(calc_human(root))
