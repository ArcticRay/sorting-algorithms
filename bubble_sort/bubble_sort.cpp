#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <ctime>

void bubble_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    std::ifstream input("data/input_10k.txt");
    if (!input) {
        std::cerr << "Error: File not found!" << std::endl;
        return 1;
    }

    std::vector<int> data;
    int value;
    while (input >> value) {
        data.push_back(value);
    }

    clock_t start = clock();
    bubble_sort(data);
    double elapsed_time = (double)(clock() - start) / CLOCKS_PER_SEC;

    std::cout << "C++ Bubble Sort: " << elapsed_time << " seconds" << std::endl;

    std::ofstream output("results/bubble_sort_results.csv", std::ios::app); // Append-Mode
    output << "C++," << data.size() << "," << elapsed_time << "\n"; 
    return 0;
}
