import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import random

def bubble_sort_visual(arr):
    """Bubble-Sort-Algorithmus mit Schritt-für-Schritt-Zustandsrückgabe."""
    n = len(arr)
    steps = [arr.copy()]  # Liste for Sorting Steps
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())  # Safe after exchange
    return steps

def update(frame, bar_rects, steps):
    """Aktualisiert die Balken im Plot für jedes Frame."""
    for rect, val in zip(bar_rects, steps[frame]):
        rect.set_height(val)

def create_bubble_sort_gif(data, output_path="visualizer/outputs/bubble_sort_animation.gif"):
    """Erstellt ein GIF für den Bubble-Sort-Algorithmus."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    steps = bubble_sort_visual(data)

    # Setup plot
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(data)), data, color="blue")
    ax.set_title("Bubble Sort Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_ylim(0, max(data) * 1.1)

    # Create Animation
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(steps),
        fargs=(bar_rects, steps),
        interval=500,  # Delay in milliseconds
        repeat=False,
    )

    # Safe as GIF
    ani.save(output_path, writer="imagemagick", fps=2)
    print(f"Animation saved to {output_path}")

if __name__ == "__main__":
    # generate Test Data
    random.seed(42)
    test_data = [random.randint(1, 50) for _ in range(20)]  # List with 20 integers

    print(f"Original Data: {test_data}")

    # Create GIF
    create_bubble_sort_gif(test_data)
