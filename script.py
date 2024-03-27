import sys

def sum_numbers(num1, num2):
  """This function takes two numbers as arguments and returns their sum.

  Args:
      num1: The first number.
      num2: The second number.

  Returns:
      The sum of num1 and num2.
  """
  # Check if two arguments are provided
  if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
    sys.exit(1)

  # Try converting arguments to floats in case they are strings
  try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
  except ValueError:
    print("Error: Please enter valid numbers.")
    sys.exit(1)

  # Calculate the sum
  sum = num1 + num2

  # Print the sum
  #print(f"The sum of {num1} and {num2} is: {sum}")
  print(f"{sum}")
  return sum

# Call the function with the arguments passed from command line
sum_numbers(sys.argv[1], sys.argv[2])
