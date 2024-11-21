class PolynomialDerivativeCalculator:
    def __init__(self):
        self.polynomial = None
    
    def get_user_input(self):
        raw_input = input("Enter a polynomial (e.g., 3*x^3 - 4*x^2 + 5*x - 7): ")
        self.polynomial = raw_input.replace(' ', '')

    def parse_polynomial(self):
        terms = self.polynomial.replace('-', '+-').split('+')  
        parsed_terms = []
        for term in terms:
            if 'x^' in term:
                coef, exp = term.split('*x^')
                parsed_terms.append({'coef': float(coef), 'exp': int(exp)})
            elif 'x' in term:
                coef = term.split('*x')[0]
                parsed_terms.append({'coef': float(coef), 'exp': 1})
            elif term.strip():
                parsed_terms.append({'coef': float(term), 'exp': 0})
        return parsed_terms

    def differentiate(self, terms):
        differentiated_terms = []
        for term in terms:
            if term['exp'] > 0:
                new_coef = term['coef'] * term['exp']
                new_exp = term['exp'] - 1
                differentiated_terms.append({'coef': new_coef, 'exp': new_exp})
        return differentiated_terms

    def format_polynomial(self, terms):
        formatted_terms = []
        for term in terms:
            coef = term['coef']
            exp = term['exp']
            if exp == 0:
                formatted_terms.append(f"{coef}")
            elif exp == 1:
                formatted_terms.append(f"{coef}*x")
            else:
                formatted_terms.append(f"{coef}*x^{exp}")
        return " + ".join(formatted_terms).replace("+ -", "- ")

    def calculate_derivative(self):
        parsed_terms = self.parse_polynomial()
        differentiated_terms = self.differentiate(parsed_terms)
        return self.format_polynomial(differentiated_terms)


if __name__ == "__main__":
    calculator = PolynomialDerivativeCalculator()
    calculator.get_user_input()
    derivative = calculator.calculate_derivative()
    print("Derivative:", derivative)
