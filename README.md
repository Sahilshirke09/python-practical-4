# MCA Semester I - Practical 4: Recursion, Exceptions & Debugging
**Course:** Python Programming Foundations (Unit I / CO1)  
**Student:** Sahil Surendra Shirke  

## Part A: Manual Trace of `factorial(3)`
- **Winding Phase (Calls):** `factorial(3)` $\rightarrow$ `3 * factorial(2)` $\rightarrow$ `2 * factorial(1)` $\rightarrow$ `1 * factorial(0)` (base case)
- **Unwinding Phase (Returns):** `factorial(0)` returns `1` $\rightarrow$ `factorial(1)` returns `1` $\rightarrow$ `factorial(2)` returns `2` $\rightarrow$ `factorial(3)` returns `6`

## Part D: Debugging Note
- **Symptom:** `factorial_buggy(4)` returned `0` instead of `24`.
- **Breakpoint Location:** Set on the first line inside `factorial_buggy(n)` (`if n == 0:`).
- **Observation:** Using Step Into in the debugger confirmed `n` decremented accurately (`4 -> 3 -> 2 -> 1 -> 0`), but hitting `n == 0` returned `0`, turning every subsequent multiplication on the call stack into `0`.
- **Root Cause:** Returning `0` instead of `1` at the base case.
- **Fix:** Updated the base case return value to `1`, producing `1` for `n = 0` and `24` for `n = 4`.

## Oral Justification (Viva Reference)
1. **Why must `factorial` use a base case of `1` for `n = 0`?**
   - Mathematically, $0! = 1$ (the empty product / multiplicative identity). Computationally, recursion unwinds by multiplying `n * factorial(n - 1)`; without a base case, recursion runs infinitely (`RecursionError`), and if the base case returned `0`, every recursive product would evaluate to `0`.
2. **Why is a custom exception (`InvalidInputError`) useful for negative input?**
   - `ValueError` handles type-conversion failures (such as `"abc"` failing `int()`), whereas `InvalidInputError` enforces the application's domain rule (`value >= 0`). Separating them allows distinct, clear error messages and cleaner control flow without mixing syntax/type errors with business-rule violations.
