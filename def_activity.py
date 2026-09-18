# A "def" function lets us group a set of instructions under one name,
# so we can reuse that code by simply calling the function's name
# instead of rewriting the same lines every time. Functions can also
# accept inputs (parameters) and give back a result (return value).

def calculate_area(length, width):
    """Calculates and returns the area of a rectangle."""
    area = length * width
    return area


def main():
    length = 5
    width = 3
    result = calculate_area(length, width)  # calling/invoking the function
    print(f"The area of a rectangle with length {length} and width {width} is {result}")


main()  # calling the main function to run the program