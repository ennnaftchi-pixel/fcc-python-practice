def hanoi_solver(n):
    """
    Solves the Tower of Hanoi puzzle and records the state of rods after each move.

    Args:
        n (int): Number of disks

    Returns:
        str: Multiline string showing the rods after each move
    """
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = []

    def move_disks(num, from_rod, to_rod, aux_rod):
        if num == 0:
            return

        move_disks(num - 1, from_rod, aux_rod, to_rod)

        to_rod.append(from_rod.pop())

        moves.append(f"{source} {auxiliary} {target}")

        move_disks(num - 1, aux_rod, to_rod, from_rod)

    moves.append(f"{source} {auxiliary} {target}")

    move_disks(n, source, target, auxiliary)

    return "\n".join(moves)


if __name__ == "__main__":
    disks = 3
    print(hanoi_solver(disks))
