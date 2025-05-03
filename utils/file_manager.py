import csv
import os.path


def read(filename: str) -> list:
    path = f"data/{filename}"
    if os.path.exists(path=path):
        with open(file=path, mode="r", encoding="UTF-8") as file:
            return list(csv.reader(file))
    return []


def write(filename: str, data: list) -> None:
    path = f"data/{filename}"
    with open(file=path, mode="w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        writer.writerow(data)
