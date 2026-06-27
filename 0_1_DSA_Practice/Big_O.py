def big_o_notation():
    """
    This function demonstrates the concept of Big O notation by providing examples of different time complexities.
    """
    
    # Example 1: O(1) - Constant Time Complexity
    def constant_time_example(arr):
        return arr[0]  # Accessing the first element takes constant time

    # Example 2: O(n) - Linear Time Complexity
    def linear_time_example(arr):
        for item in arr:
            print(item)  # Iterating through each element takes linear time

    # Example 3: O(n^2) - Quadratic Time Complexity
    def quadratic_time_example(arr):
        for i in arr:
            for j in arr:
                print(i, j)  # Nested loops result in quadratic time complexity

    # Example 4: O(log n) - Logarithmic Time Complexity
    def logarithmic_time_example(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid  # Found the target
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Target not found

    # Example usage of the functions
    sample_array = [1, 2, 3, 4, 5]
    
    print("O(1) Example:", constant_time_example(sample_array))
    print("O(n) Example:")
    linear_time_example(sample_array)
    
    print("O(n^2) Example:")
    quadratic_time_example(sample_array)
    
    print("O(log n) Example:", logarithmic_time_example(sample_array, 3))

big_o_notation()