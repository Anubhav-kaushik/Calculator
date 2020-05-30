

def factorize(number):
    n = 1
    factors = []
    while n <= number:
        if number % n == 0:
            factors.append(n)
        n += 1
    return factors


def primeFactorize(number):
    n = 1
    primeFactors = []
    primepowerfactors = []
    while n <= number:
        if len(factorize(n)) == 2:
            if number % n == 0:
                primeFactors.append(n)
        n += 1
    for i in primeFactors:
        div = number
        power = 0
        while div % i == 0:
            div /= i
            power += 1
        for _ in range(power):
            primepowerfactors.append(i)
    return primepowerfactors


def squareRoot(number, precision=15):
    num = abs(number)
    str_number = str(num)
    lengthOfNumber = len(str_number)
    runlength = lengthOfNumber // 2
    remainder = 0
    # quotient = 0
    quotient = []
    divisor = 0

    if lengthOfNumber % 2 != 0:
        runlength = (lengthOfNumber + 1) // 2
        str_number = "0" + str_number

    for i in range(runlength + precision):
        if i < runlength:
            dividend = remainder*100 + int(str_number[2*i: 2*(i+1)])
        else:
            dividend = remainder*100
        dynamic_divisor = 0
        while True:
            temp_divisor = divisor * 10 + dynamic_divisor
            if dividend - (temp_divisor * dynamic_divisor) < 0:
                remainder = dividend - ((temp_divisor - 1) * (dynamic_divisor - 1))
                # quotient = quotient*10 + (dynamic_divisor - 1)
                quotient.append(str(dynamic_divisor - 1))
                divisor = (temp_divisor - 1) + (dynamic_divisor - 1)
                break
            dynamic_divisor += 1
    quotient.insert(-(precision), ".")
    if number < 0:
        quotient.append("j")
    result = "".join(quotient)
    return result


def average(numberList):
    sum = 0
    for i in numberList:
        sum += i
    totalnum = len(numberList)
    return sum / totalnum


def product(numberList):
    prod = 1
    for i in numberList:
        prod *= i
    return prod


def summation(numberList):
    sum = 0
    for i in numberList:
        sum += i
    return sum


def commonFactor(numberList):
    factors = []
    common = []
    for i in numberList:
        factors.append(factorize(i))
    factors = sorted(factors, key=lambda f: len(f))
    for j in factors[0]:
        for k in range(1, len(factors)):
            if j not in factors[k]:
                break
        else:
            common.append(j)
    return common


def commonprimefactors(numberList):
    factors = []
    common = []
    for i in numberList:
        factors.append(primeFactorize(i))
    factors = sorted(factors, key=lambda f: len(f))
    print(factors)
    for j in factors[0]:
        for k in range(1, len(factors)):
            if j not in factors[k]:
                break
            else:
                pass
        else:
            common.append(j)
    return common


def hcf(numberList):
    common = commonprimefactors(numberList)
    return product(common)


if __name__ == "__main__":
    num = [2000, 600, 80, 10, 1720]
    print(squareRoot(-381))

