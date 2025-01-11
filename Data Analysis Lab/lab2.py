import numpy as np

def main():
    # Task 1: Generate a 5x5 matrix with random numbers (0-1)
    np.random.seed(42)  # Fixed seed for consistency
    matrix = np.random.rand(5, 5)
    
    print("Original Matrix:")
    print(matrix)
    
    # Task 2: Attempt to compute the inverse of the matrix
    try:
        inverse_matrix = np.linalg.inv(matrix)
        print("\nInverse Matrix:")
        print(inverse_matrix)
    except np.linalg.LinAlgError:
        print("\nThe matrix is non-invertible (singular).")
        return
    
    # Task 3: Verify closeness to the identity matrix
    identity_check = np.dot(matrix, inverse_matrix)
    print("\nProduct of Matrix and its Inverse (Should approximate Identity Matrix):")
    print(identity_check)
    print("\nCloseness to Identity Matrix:")
    print(np.allclose(identity_check, np.eye(5)))  # Checks if the product is close to the identity matrix
    
    # Task 4: Statistical Analysis
    mean_value = np.mean(matrix)
    median_value = np.median(matrix)
    variance_value = np.var(matrix)
    
    print("\nStatistical Analysis of Original Matrix:")
    print(f"Mean: {mean_value:.2f}")
    print(f"Median: {median_value:.2f}")
    print(f"Variance: {variance_value:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
