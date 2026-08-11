from pathlib import Path
from optimize_farm import parse_field, print_field, evaluate_field, get_side_and_area


files = [
    "standard_field.txt",
    "best_random_field.txt",
    "best_mutated_field.txt",
    "best_geometric_field.txt",
    "best_milp_field.txt",
    "reddit_field.txt",
]

for file_name in files:
    file_path = Path(file_name)
    print(f"Field from {file_path.name}:")
    field = parse_field(file_path)
    _, area = get_side_and_area(field)
    print_field(field)
    productive_area, relative_area = evaluate_field(field)
    print(f"Total productive area: {productive_area} of {area}")
    print(f"Relative productive area: {relative_area:.2f} %")

    print()