import subprocess
import os


def clear_csv():
    """Leert die CSV-Datei, um alte Ergebnisse zu entfernen."""
    csv_path = "results/bubble_sort_results.csv"
    os.makedirs("results", exist_ok=True) 
    with open(csv_path, "w") as csvfile:
        csvfile.write("")
    print(f"Cleared previous contents of {csv_path}.")

def generate_data():
    print("Generating test data...")
    subprocess.run(["python", "generate_test_data.py"], check=True)

def run_python_sort():
    print("Running Python Bubble Sort...")
    result = subprocess.run(["python", "bubble_sort/bubble_sort.py"], capture_output=True, text=True)
    print(result.stdout)
    if not os.path.exists("results/bubble_sort_results.csv"):
        print("Error: results/bubble_sort_results.csv not found after Python sort.")

def run_cpp_sort():
    print("Running C++ Bubble Sort...")
    subprocess.run(["g++", "bubble_sort/bubble_sort.cpp", "-o", "bubble_sort/bubble_sort.out"])
    result = subprocess.run(["./bubble_sort/bubble_sort.out"], capture_output=True, text=True)
    print(result.stdout)

def run_java_sort():
    print("Running Java Bubble Sort...")
    subprocess.run(["javac", "bubble_sort/BubbleSort.java"])
    result = subprocess.run(["java", "-cp", "bubble_sort", "BubbleSort"], capture_output=True, text=True)
    print(result.stdout)

def visualize_results():
    print("Visualizing results...")
    csv_path = "results/bubble_sort_results.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} does not exist. Skipping visualization.")
        return
    subprocess.run(["python", "visualizer/visualize_bubble_sort.py"], check=True)

def main():
    os.makedirs("results", exist_ok=True)

    csv_path = "results/bubble_sort_results.csv"
    if not os.path.exists(csv_path):
        with open(csv_path, "w") as f:
            f.write("")

    clear_csv()

    generate_data()
    run_python_sort()
    run_cpp_sort()
    run_java_sort()
    visualize_results()
    print("\nAll steps completed successfully.")

if __name__ == "__main__":
    main()
