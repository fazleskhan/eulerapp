def greeting():
    print("Hi there")


def calculate_pi_to_5th_digit():
    """
    Calculate pi to the 5th decimal digit using the Chudnovsky algorithm.
    This is one of the fastest converging algorithms for pi.
    Returns pi accurate to at least 5 decimal places: 3.14159
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough for accurate calculation
    getcontext().prec = 50
    
    def factorial(n):
        """Calculate factorial of n"""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def chudnovsky_term(k):
        """Calculate the k-th term of Chudnovsky algorithm"""
        numerator = factorial(6 * k) * (13591409 + 545140134 * k)
        denominator = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
        return Decimal(numerator) / Decimal(denominator) * (Decimal(-1) ** k)
    
    # Sum terms until we have enough precision
    # For 5 decimal places, a few terms are sufficient
    pi_sum = Decimal(0)
    for k in range(3):  # 3 terms gives us plenty of precision for 5 digits
        pi_sum += chudnovsky_term(k)
    
    # Apply the Chudnovsky formula constant
    constant = Decimal(426880) * Decimal(10005).sqrt()
    pi_approx = constant / pi_sum
    
    # Round to 5 decimal places
    return round(float(pi_approx), 5)