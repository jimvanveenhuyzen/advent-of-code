with open("input1.txt") as f:
    input_data = f.readlines()

input_data = [s.rstrip() for s in input_data]


def dial(rotations: list, starting_position: int = 50) -> tuple[int, int]:
    """Calculates the number of passes through 0

    Args:
        rotations (list): list of rotations performed on the dial
        starting_position (int, optional): starting position on the safe. Defaults to 50.

    Returns:
        counts_at_zero (tuple[int, int]): number of passes through 0
    """
    counts_exactly_at_zero = 0
    counts_passes_zero = 0
    position = starting_position
    for rot in rotations:
        direction = rot[0]
        value = int(rot[1:])

        difference = value if direction == "R" else -value

        # difference = position + value
        counts_passes_zero += int(abs(difference)/100)
        remainder = abs(difference) % 100

        if difference > 0 and position + remainder >= 100:
            counts_passes_zero += 1
        elif difference < 0 and position - remainder <= 0:
            counts_passes_zero += 1

        position = (position + difference) % 100

        if position == 0:
            counts_exactly_at_zero += 1

    return counts_exactly_at_zero, counts_passes_zero


count_at_zero, count_passes_zero = dial(rotations=input_data)
print(
    f"Number of cases exactly at zero: {count_at_zero}\nNumber of passes through zero: {count_passes_zero}"
)
