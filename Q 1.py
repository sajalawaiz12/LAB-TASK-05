def divide_without_operator(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero is not allowed."

    quotient = 0
    sign = 1

    if dividend < 0:
        dividend = -dividend
        sign = -sign

    if divisor < 0:
        divisor = -divisor
        sign = -sign

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    quotient *= sign

    return quotient
print(divide_without_operator(10, 2))  
 