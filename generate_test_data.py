import random
import os

def generate_data(file_name, size):
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", file_name)
    with open(file_path, "w") as f:
        f.write(" ".join(str(random.randint(0, 1000)) for _ in range(size)))
    print(f"Generated {size} integers in {file_path}.")

if __name__ == "__main__":
    generate_data("input_1k.txt", 1000)
    generate_data("input_10k.txt", 10000)
    generate_data("input_100k.txt", 100000)
