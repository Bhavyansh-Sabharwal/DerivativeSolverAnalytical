# Analytical Derivative Calculator

This program calculates the derivative of a polynomial using symbolic differentiation. It currently supports polynomials with terms like a*x^n, where a is the coefficient, x is the variable, and n is the exponent.

---

## Features
- **Flexible Input**: Accepts user-input polynomials (e.g., `3*x^3 - 4*x^2 + 5*x - 7`).
- **Handles Spaces**: Automatically removes unnecessary spaces in the input.
- **Symbolic Differentiation**: Applies the power rule to calculate derivatives.
- **Formatted Output**: Returns the derivative in a clean, readable polynomial format.

---

## Requirements
- Python 3.x

---

## Usage

1. **Run the Script**  
   Execute the script in your terminal or IDE:
   ```bash
   python polynomial_derivative_calculator.py

2. **Enter a Polynomial**
   When prompted, input a polynomial. For example:
   ```bash
   Enter a polynomial (e.g., 3*x^3 - 4*x^2 + 5*x - 7): 3*x^3 - 4*x^2 + 5*x - 7
3. **View the Output**
   The program will output the derivative. For the above input, it will display:
   ```bash
   Derivative: 9*x^2 - 8*x + 5
---

## Further Enhancements
- **Add support for fractional exponents.**
- **Extend functionality to handle trigonometric, logarithmic, and exponential terms.**
- **Validate input for errors and provide helpful feedback**
