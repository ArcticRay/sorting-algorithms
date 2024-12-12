import java.io.*;
import java.util.*;

public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        // Read data from file
        BufferedReader reader = new BufferedReader(new FileReader("data/input_10k.txt"));
        String[] numbers = reader.readLine().split(" ");
        int[] data = Arrays.stream(numbers).mapToInt(Integer::parseInt).toArray();
        reader.close();

        long start = System.currentTimeMillis();
        bubbleSort(data);
        long elapsedTime = System.currentTimeMillis() - start;

        System.out.println("Java Bubble Sort: " + elapsedTime / 1000.0 + " seconds");

        // Save results
        try (FileWriter writer = new FileWriter("results/bubble_sort_results.csv", true)) { // true for Append
            writer.write("Java," + data.length + "," + elapsedTime / 1000.0 + "\n");
}

    }
}
