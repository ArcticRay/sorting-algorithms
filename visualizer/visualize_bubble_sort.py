import matplotlib.pyplot as plt
import pandas as pd
import os

# Laden der CSV-Daten
data = pd.read_csv("results/bubble_sort_results.csv", header=None, names=["Language", "ArraySize", "Time"])

# Gruppieren nach Sprache und Berechnung der durchschnittlichen Zeit
grouped = data.groupby("Language").mean()

# Plot erstellen
plt.bar(grouped.index, grouped["Time"], color=["blue", "green", "orange"])
plt.xlabel("Programming Languages")
plt.ylabel("Time (seconds)")
plt.title("Bubble Sort Performance Comparison")

# Werte über den Balken anzeigen
for i, (lang, time) in enumerate(zip(grouped.index, grouped["Time"])):
    plt.text(i, time + 0.01, f"{time:.3f}s", ha="center", fontsize=10, color="black")

# Ordner für die gespeicherten Bilder erstellen
os.makedirs("visualizer/outputs", exist_ok=True)

# Plot speichern
output_path = "visualizer/outputs/bubble_sort_performance.png"
plt.savefig(output_path)
print(f"Plot saved to {output_path}")

# Plot anzeigen
plt.show()
