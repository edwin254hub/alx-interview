def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        # Calculate the elements in the current row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

# Example usage
if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

