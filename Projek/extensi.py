import random
import time
import matplotlib.pyplot as plt

# Function to generate array with n elements and max_value
def generate_array(n, max_value, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

# Function to check if array elements are unique
def is_unique(array):
    seen = set()
    for num in array:
        if num in seen:
            return False
        seen.add(num)
    return True

# Measure execution time of a function
def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time

# Parameters
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
stambuk_last_3_digits = 123  # Example last 3 digits
max_value = 250 - stambuk_last_3_digits
seed = 42  # Random seed for reproducibility

# Data storage for plotting and output
worst_case_times = []
average_case_times = []
results = []

for n in n_values:
    # Generate average case array
    avg_case_array = generate_array(n, max_value, seed)

    # Measure time for average case
    _, avg_time = measure_time(is_unique, avg_case_array)
    average_case_times.append(avg_time)

    # Generate worst case array (all elements the same)
    worst_case_array = [1] * n

    # Measure time for worst case
    _, worst_time = measure_time(is_unique, worst_case_array)
    worst_case_times.append(worst_time)

    # Store results for output
    results.append(f"n = {n}: Average Case Time = {avg_time:.6f}s, Worst Case Time = {worst_time:.6f}s")

# Save results to a .txt file
with open("worst_avg.txt", "w") as file:
    file.write("\n".join(results))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label="Worst Case", marker='o')
plt.plot(n_values, average_case_times, label="Average Case", marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (seconds)")
plt.title("Performance of Uniqueness Check")
plt.legend()
plt.grid()
plt.savefig("performance_plot.jpg")  # Save plot as .jpg
plt.show()
