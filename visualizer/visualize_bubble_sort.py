import matplotlib.pyplot as plt
import pandas as pd
import os

# Load CSV Data
data = pd.read_csv("results/bubble_sort_results.csv", header=None, names=["Language", "ArraySize", "Time"])

# Group by language and calculation of average time
grouped = data.groupby("Language").mean()

# create plot
plt.bar(grouped.index, grouped["Time"], color=["blue", "green", "orange"])
plt.xlabel("Programming Languages")
plt.ylabel("Time (seconds)")
plt.title("Bubble Sort Performance Comparison")

# Create Folder for outputs
os.makedirs("visualizer/outputs", exist_ok=True)

# save plot
output_path = "visualizer/outputs/bubble_sort_performance.png"
plt.savefig(output_path)
print(f"Plot saved to {output_path}")

# show plot
plt.show()
