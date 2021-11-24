from random import random
from pathlib import Path


with open(Path(__file__).parent / "sample.txt", "w") as f:
    for i in range(5000):
        number = round(random() * 5000)
        f.write(f"{number}\n")
