from pathlib import Path
from datetime import datetime
import random

def parse_field(file: Path) -> list[str]:
    field = file.read_text().splitlines()
    return field

def get_side_and_area(field: list[str]) -> tuple[int, int]:
    size = len(field)  # assume NxN
    return size, size * size


def print_field(field: list[str]) -> None:
    # "F" tile is green if touching "W"
    # "F" tile is yellow if not touching "W"
    # "W" tile is always blue
    size, _ = get_side_and_area(field)
    for y in range(size):
        for x in range(size):
            tile = field[y][x]
            if tile == "F":
                # check neighbors
                neighbors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
                is_productive = False
                for ny, nx in neighbors:
                    if 0 <= ny < size and 0 <= nx < size:
                        if field[ny][nx] == "W":
                            is_productive = True
                            break
                if is_productive:
                    print("\033[92mF\033[0m", end="")  # green for "F"
                else:
                    print("\033[93mF\033[0m", end="")  # yellow for "F"
            elif tile == "W":
                print("\033[94mW\033[0m", end="")  # blue for "W"
        print()


def evaluate_field(field: list[str]) -> tuple[int, float]:
    # if a tile of "F" is next to a tile of "W", then the field is productive
    # find the total & relative area of productive land 
    productive_area = 0

    size, area = get_side_and_area(field)
    for y in range(size):
        for x in range(size):
            if field[y][x] == "F":
                # check neighbors
                neighbors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
                for ny, nx in neighbors:
                    if 0 <= ny < size and 0 <= nx < size:
                        if field[ny][nx] == "W":
                            productive_area += 1
                            break

    relative_area = (productive_area / area) * 100 if area > 0 else 0
    return productive_area, relative_area


def random_field(size: int, water_ratio: float) -> list[str]:
    field = []
    for _ in range(size):
        row = ''.join(random.choices(['F', 'W'], weights=[1 - water_ratio, water_ratio], k=size))
        field.append(row)
    return field


def get_best_random_field(size: int, water_ratio: float, iterations: int = 10_000) -> list[str]:
    best_field = ["F" * size] * size  # start with all fertile land
    best_productive_area, _ = evaluate_field(best_field)

    for _ in range(iterations):
        new_field = random_field(size, water_ratio)
        productive_area, _ = evaluate_field(new_field)
        if productive_area > best_productive_area:
            best_productive_area = productive_area
            best_field = new_field

    return best_field


def mutate_field(field: list[str]) -> list[str]:
    size, _ = get_side_and_area(field)
    y = random.randrange(size)
    x = random.randrange(size)

    field = [list(row) for row in field]
    field[y][x] = "W" if field[y][x] == "F" else "F"
    return ["".join(row) for row in field]


def get_best_mutated_field(size: int, iterations: int = 10_000) -> list[str]:
    best_field = ["F" * size] * size  # start with all fertile land
    best_score, _ = evaluate_field(best_field)

    for _ in range(iterations):
        candidate_field = mutate_field(best_field)
        score, _ = evaluate_field(candidate_field)
        if score > best_score:
            best_score = score
            best_field = candidate_field

    return best_field

def save_field(field: list[str], prod: int, method: str) -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = Path(f"{timestamp}_{prod}_pct_{method}_field.txt")
    file_path.write_text("\n".join(field))


if __name__ == "__main__":
    # Example usage
    field_file = Path("standard_field.txt")
    print("Original Field:")
    field = parse_field(field_file)
    print_field(field)
    side, area = get_side_and_area(field)
    productive_area, relative_area = evaluate_field(field)
    # print(f"Field side: {side} x {side}")
    print(f"Total productive area: {productive_area} of {area}")
    print(f"Relative productive area: {relative_area:.1f}%")

    # print()
    # print("Randomly Optimized Field:")
    # best_field = get_best_random_field(side, water_ratio=0.3)
    # print_field(best_field)
    # productive_area, relative_area = evaluate_field(best_field)
    # print(f"Total productive area: {productive_area} of {area}")
    # print(f"Relative productive area: {relative_area:.1f}%")
    # save_field(best_field, int(relative_area), "random")
# 
    # print()
    # print("Mutation Optimized Field:")
    # best_field = get_best_mutated_field(side)
    # print_field(best_field)
    # productive_area, relative_area = evaluate_field(best_field)
    # print(f"Total productive area: {productive_area} of {area}")
    # print(f"Relative productive area: {relative_area:.1f}%")
    # save_field(best_field, int(relative_area), "mutated")

    print()
    print("Copilot Optimized Field:")
    best_field = parse_field(Path("best_field.txt"))
    print_field(best_field)
    productive_area, relative_area = evaluate_field(best_field)
    print(f"Total productive area: {productive_area} of {area}")
    print(f"Relative productive area: {relative_area:.1f}%")

    print()
    print("Reddit Optimized Field:")
    best_field = parse_field(Path("reddit_field.txt"))
    print_field(best_field)
    productive_area, relative_area = evaluate_field(best_field)
    print(f"Total productive area: {productive_area} of {area}")
    print(f"Relative productive area: {relative_area:.1f}%")
