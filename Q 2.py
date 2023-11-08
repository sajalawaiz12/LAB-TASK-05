def create_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
create_triangle(5)