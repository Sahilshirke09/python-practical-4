"""
Practical 4: Recursion, Exceptions & Debugging
Course: MCA Semester I - Python Programming Foundations (Unit I / CO1)
Student: Sahil Surendra Shirke

Part A - Manual Trace of factorial(3):
Call sequence (winding phase):
  factorial(3) -> 3 * factorial(2)
  factorial(2) -> 2 * factorial(1)
  factorial(1) -> 1 * factorial(0)
  factorial(0) -> base case reached (returns 1)

Return order (unwinding phase):
  factorial(0) returns 1
  factorial(1) returns 1 * 1 = 1
  factorial(2) returns 2 * 1 = 2
  factorial(3) returns 3 * 2 = 6

Part D - Debugging Note:
- Symptom: Calling factorial_buggy(4) returned 0 instead of 24.
- Breakpoint Location: Placed on the base-case check (`if n == 0:`) inside factorial_buggy().
- Observation: Stepping into the recursive calls showed `n` decrementing properly (4 -> 3 -> 2 -> 1 -> 0),
  but when `n == 0` was hit, the function returned 0, causing every unwinding multiplication (1*0, 2*0, 3*0, 4*0) to collapse to 0.
- Root Cause: Incorrect base-case return value (0 instead of the multiplicative identity 1).
- Fix: Changed `return 0` to `return 1` when `n == 0`, restoring the expected outputs (1 for n=0, 24 for n=4).
"""


# Part C: Custom Exception Definition
class InvalidInputError(Exception):
    """Raised when user input violates the application's domain rules."""
    pass


# Part B: Recursive Functions
def factorial(n):
    """Computes n! recursively for non-negative integers."""
    if n < 0:
        raise ValueError("n must be non-negative")
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)


def recursive_search(items, target, index=0):
    """Recursively searches for target in items and returns its index, or -1 if not found."""
    # Base case 1: end of list reached
    if index >= len(items):
        return -1
    # Base case 2: target found
    if items[index] == target:
        return index
    # Recursive case: check remaining slice starting at index + 1
    return recursive_search(items, target, index + 1)


# Part D: Corrected Function (after breakpoint debugging)
def factorial_debugged(n):
    """Fixed version of factorial_buggy where base case n == 0 returns 1."""
    if n == 0:
        return 1  # Fixed: changed from 0 to 1
    return n * factorial_debugged(n - 1)


# Part C: Specific Exception Handling & Input Validation
def read_non_negative_integer(prompt="Enter a non-negative integer: "):
    """Reads and validates a non-negative integer using try/except/else/finally."""
    raw = input(prompt)
    try:
        value = int(raw)
        if value < 0:
            raise InvalidInputError("Number cannot be negative.")
    except ValueError:
        print("Input error: enter a whole number, such as 4.")
        return None
    except InvalidInputError as error:
        print(f"Validation error: {error}")
        return None
    else:
        print("Input accepted.")
        return value
    finally:
        print("Input validation attempt finished.")


def run_automated_tests():
    """Executes all test cases from the Practical 4 Test Checklist."""
    print("=== 1. Recursive Factorial Tests ===")
    print(f"factorial(0) = {factorial(0)}")  # Expected: 1
    print(f"factorial(1) = {factorial(1)}")  # Expected: 1
    print(f"factorial(5) = {factorial(5)}")  # Expected: 120
    try:
        factorial(-2)
    except ValueError as err:
        print(f"factorial(-2) raised ValueError: {err}")

    print("\n=== 2. Recursive Linear Search Tests ===")
    sample = [8, 3, 12]
    print(f"Search 8 (first) in {sample}  -> index {recursive_search(sample, 8)}")    # Expected: 0
    print(f"Search 12 (last) in {sample}  -> index {recursive_search(sample, 12)}")  # Expected: 2
    print(f"Search 5 (missing) in {sample} -> index {recursive_search(sample, 5)}")  # Expected: -1

    print("\n=== 3. Debugged Function Verification ===")
    print(f"factorial_debugged(0) = {factorial_debugged(0)}")  # Expected: 1
    print(f"factorial_debugged(4) = {factorial_debugged(4)}")  # Expected: 24


def main():
    run_automated_tests()

    print("\n=== 4. Interactive Input Validation & Exception Handling ===")
    print("(Test with: 'abc', '-3', and '4')")
    for attempt in range(1, 4):
        print(f"\nAttempt {attempt}/3:")
        number = read_non_negative_integer()
        if number is not None:
            print(f"Factorial of {number} is {factorial(number)}")


if __name__ == "__main__":
    main()
