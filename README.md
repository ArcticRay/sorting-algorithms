# Sorting Algorithms Performance Analysis

This project focuses on implementing and benchmarking sorting algorithms, starting with **Bubble Sort**, across multiple programming languages (**Python**, **C++**, and **Java**). The goal is to analyze runtime differences when sorting identical datasets and visualize the performance comparison.

---

## 📊 Results: Bubble Sort Performance

The following chart illustrates the runtime performance of Bubble Sort implemented in **Python**, **C++**, and **Java** for a dataset of 1,000 integers.

![Bubble Sort Performance](visualizer/outputs/bubble_sort_performance.png)

---

## 📂 Project Structure

. ├── data/ # Contains input datasets ├── results/ # Stores runtime results in CSV format ├── bubble_sort/ # Bubble sort implementations │ ├── bubble_sort.py # Python implementation │ ├── bubble_sort.cpp # C++ implementation │ ├── BubbleSort.java # Java implementation ├── visualizer/ # Visualization scripts │ ├── visualize_bubble_sort.py │ ├── outputs/ # Stores generated plots └── run_all_sorters.py # Automation script to run and benchmark all algorithms
