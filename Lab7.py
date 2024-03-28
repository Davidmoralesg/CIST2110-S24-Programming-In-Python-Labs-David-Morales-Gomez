
# Lab7
# Author:David Morales Gomez


## add in functions from test.py's test statements here to make the pytest work
## Use this file and your test plan to complete the lab


def calculate_rectangle_area(length: int, width: int) -> int:
    """Calculate the area of a rectangle

    Args:
        length (int): The length of the rectangle
        width (int): The width of the rectangle
    """
    return length * width




#def main():
 #   print(calculate_rectangle_area(3,4))
  #  print(calculate_rectangle_area(5,5))
   # print(calculate_rectangle_area(0,0))
    #print(calculate_rectangle_area(10,20))
    
def calculate_hypotenuse(a: int, b: int) -> float:
    """Calculate the hypotenuse using the pythagorean theorem

    Args:
        a (int): a side of the triangle
        b (int): b side of the triangle
        
    Returns:
        floot: The length of the hypotenuse
    """
    return (a**2 + b**2)**0.5

#def main():
 #  pass 
#    print(calculate_hypotenuse(3,4))
#    print(calculate_hypotenuse(5,12))
#    print(calculate_hypotenuse(7,24))
#    print(calculate_hypotenuse(8,15))
def main():
   pass 
def is_even(number: int) -> bool:
    """Check if a number is even"""
    return number % 2 == 0

#print(test_is_even(2))
#print(test_is_even(7))
#print(test_is_even(0))
#print(test_is_even(11))


def find_maximum(a: int, b: int) -> int:
    """Find the maximum of two numbers
    Args:
        a (int): number 1
        b (int): number 2
    """
    if a > b:
        return a
    else:
        return b
def main():
    print(find_maximum(3,4))


if __name__ == "__main__":
    main()
