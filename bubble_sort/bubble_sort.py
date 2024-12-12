import time
import csv
import os

def bubble_sort(arr):
    """Implementierung des Bubble-Sort-Algorithmus."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    # Sicherstellen, dass der Ordner und die Ergebnisse existieren
    data_file = "data/input_10k.txt"
    csv_path = "results/bubble_sort_results.csv"
    os.makedirs("results", exist_ok=True)

    # Daten aus Datei einlesen
    try:
        with open(data_file, "r") as f:
            data = list(map(int, f.read().split()))
        print(f"Loaded {len(data)} integers from {data_file}.")
    except FileNotFoundError:
        print(f"Error: {data_file} not found. Please generate the data first.")
        exit(1)

    # Bubble Sort ausführen und Zeit messen
    start_time = time.time()
    bubble_sort(data)
    elapsed_time = time.time() - start_time

    print(f"Python Bubble Sort: {elapsed_time:.5f} seconds")

    # Ergebnisse in die CSV-Datei schreiben
    try:
        with open(csv_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Python", len(data), elapsed_time])
        print(f"Results written to {csv_path}.")
    except Exception as e:
        print(f"Error writing results to CSV: {e}")
