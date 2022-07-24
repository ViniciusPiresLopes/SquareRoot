import time
from decimal import *


def factorize(num):
    factors = []
    
    for i in range(2, num + 1):
        if num % i == 0:
            factors.append(i)
            factors.extend(factorize(num // i))
            break

    return factors


def sqrt_integer(num, precision=28):
    ratio = Decimal(num).as_integer_ratio()
    
    getcontext().prec = precision

    # Perfect square method
    factors = factorize(num)
    factors_quantity = {}
    perfect_square = True

    # Initialize dict
    for factor in factors:
        factors_quantity[factor] = 0

    # Count repeated values
    for factor in factors:
        factors_quantity[factor] += 1

    # Verify if it is a perfect square
    for value in factors_quantity.values():
        if value % 2 == 1:
            perfect_square = False

    if perfect_square:
        result = 1

        for factor, quantity in factors_quantity.items():
            result *= factor ** (quantity // 2)

        return result

    # Irrational results
    minimal = Decimal(0)
    maximum = Decimal(num)
    average = Decimal((minimal + maximum) / 2)

    diff1 = diff2 = 0

    while minimal != maximum:
        diff1 = Decimal(abs(minimal - maximum))

        average = Decimal((minimal + maximum) / 2)

        result = Decimal(num / average)

        if result > average:  # Value too small
            minimal = average
        elif result < average:  # Value too big
            maximum = average
        else:  # "Exact" sqrt (depends on the precision used)
            return average

        # If difference doesn't change in two loops, then we get the maximum precision capable
        if diff1 == diff2:  # Calculate the accurate number, checking between the minimal and maximum values
            accurate_number = ""
            
            for index1, char1 in enumerate(str(minimal)):
                for index2, char2 in enumerate(str(maximum)):
                    if index1 == index2:
                        if char1 == char2:
                            accurate_number += char1
                        else:  # Need to be a sequence of equal chars
                            break
            
            return Decimal(accurate_number)

        diff2 = diff1


def sqrt(num, precision=28):
    ratio = Decimal(num).as_integer_ratio()
    result = Decimal(sqrt_integer(ratio[0], precision) / sqrt_integer(ratio[1], precision))

    return result


if __name__ == "__main__":
    num = Decimal(input("Type a integer number: ").replace(",", "."))
    print(f"Result: {sqrt(num)}")
