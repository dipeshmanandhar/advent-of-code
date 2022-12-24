from src.common.read_input import read_input


class LinkNode:
    pass


class LinkNode:
    def __init__(self, val: int, prev: LinkNode = None, next: LinkNode = None) -> None:
        self.val = val
        self.prev = prev if prev else self
        self.next = next if next else self

    def __str__(self) -> str:
        out = ''
        curr_node = self
        out += f'{curr_node.val}, '
        curr_node = curr_node.next
        while curr_node != self:
            out += f'{curr_node.val}, '
            curr_node = curr_node.next
        return out[:-2]


class ParallelNode:
    def __init__(self, val: int = 0, link: LinkNode = None) -> None:
        self.val = val
        self.link = link


def move(mixed_head: LinkNode, mixed_tail: LinkNode, p_node: ParallelNode, LENGTH: int) -> None:
    a = p_node.link
    b = a
    if abs(a.val) % (LENGTH-1) == 0:
        return
    for _ in range(abs(a.val)):
        if a.val > 0:
            b = b.next
            if b == a:
                b = b.next
        elif a.val < 0:
            b = b.prev
            if b == a:
                b = b.prev
    # remove a
    a.prev.next = a.next
    a.next.prev = a.prev
    # insert a where b is
    if a.val > 0:
        a.next = b.next
        a.prev = b
    elif a.val < 0:
        a.next = b
        a.prev = b.prev
    a.prev.next = a
    a.next.prev = a

    return


def mix(encrypted: list[int]) -> LinkNode:
    LENGTH = len(encrypted)
    mixed_head: LinkNode = None
    mixed_tail: LinkNode = None
    encrypted_parallel: list[ParallelNode] = [
        ParallelNode() for _ in range(LENGTH)]
    for i, val in enumerate(encrypted):
        if not mixed_head:
            mixed_head = LinkNode(val)
            mixed_tail = mixed_head
        else:
            mixed_tail = LinkNode(val, mixed_tail, mixed_head)
            mixed_tail.prev.next = mixed_tail
            mixed_tail.next.prev = mixed_tail
        encrypted_parallel[i].val = val
        encrypted_parallel[i].link = mixed_tail

    # print(mixed_head)
    # print()
    for p_node in encrypted_parallel:
        if p_node.val == 0:
            # print(p_node.val)
            # print(mixed_head)
            # print()
            continue
        move(mixed_head, mixed_tail, p_node, LENGTH)
        # print(p_node.val)
        # print(mixed_head)
        # print()
    return mixed_head


def decrypt(encrypted: list[int]) -> tuple[int, int, int]:
    mixed_head = mix(encrypted)
    curr_node = mixed_head
    while curr_node.val != 0:
        curr_node = curr_node.next
    pos = [0, 0, 0]
    pos_i = 0
    for i in range(3000):
        curr_node = curr_node.next
        if (i+1) % 1000 == 0:
            pos[pos_i] = curr_node.val
            pos_i += 1
    return pos


input = read_input('input.txt', 2022, 20)

encrypted = [int(line) for line in input]
decrypted = decrypt(encrypted)

print(decrypted)
print(sum(decrypted))
