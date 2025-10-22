import numpy as np


# Function to display matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)


# Function to add two matrices
def add_matrices(matrix1, matrix2):
    try:
        result = np.add(matrix1, matrix2)
        return result
    except ValueError:
        return "Matrices must have the same dimensions for addition."


# Function to subtract two matrices
def subtract_matrices(matrix1, matrix2):
    try:
        result = np.subtract(matrix1, matrix2)
        return result
    except ValueError:
        return "Matrices must have the same dimensions for subtraction."


# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    try:
        result = np.dot(matrix1, matrix2)
        return result
    except ValueError:
        return "Number of columns of matrix1 must be equal to number of rows of matrix2."


# Function to transpose a matrix
def transpose_matrix(matrix):
    return np.transpose(matrix)


# Main menu function
def main():
    print("Welcome to the Matrix Calculator!")

    # Input matrices
    rows1 = int(input("Enter the number of rows for matrix 1: "))
    cols1 = int(input("Enter the number of columns for matrix 1: "))
    matrix1 = []
    print("Enter elements for matrix 1:")
    for i in range(rows1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    rows2 = int(input("Enter the number of rows for matrix 2: "))
    cols2 = int(input("Enter the number of columns for matrix 2: "))
    matrix2 = []
    print("Enter elements for matrix 2:")
    for i in range(rows2):
        row = list(map(int, input().split()))
        matrix2.append(row)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # Show the menu options
    while True:
        print("\nMatrix Calculator Options:")
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Transpose matrix 1")
        print("5. Transpose matrix 2")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            print("\nMatrix 1 + Matrix 2:")
            result = add_matrices(matrix1, matrix2)
            display_matrix(result)

        elif choice == '2':
            print("\nMatrix 1 - Matrix 2:")
            result = subtract_matrices(matrix1, matrix2)
            display_matrix(result)

        elif choice == '3':
            print("\nMatrix 1 * Matrix 2:")
            result = multiply_matrices(matrix1, matrix2)
            display_matrix(result)

        elif choice == '4':
            print("\nTranspose of Matrix 1:")
            result = transpose_matrix(matrix1)
            display_matrix(result)

        elif choice == '5':
            print("\nTranspose of Matrix 2:")
            result = transpose_matrix(matrix2)
            display_matrix(result)

        elif choice == '6':
            print("Exiting the Matrix Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
