"""
karatsuba algorithm is used for multiplication of 2 "n" digit number
"""


def get_karatsuba_multiplication(num1, num2):
    """
    return the mulplication of 2 number
    """
    str1, str2 = str(num1), str(num2)
    len1, len2 = len(str1), len(str2)

    n = min(len1, len2)
    if n==1:
        return num1 * num2
    n2 = n//2
    high1, low1 = int(str1[:len1-n2]), int(str1[len1-n2:])
    high2, low2 = int(str2[:len2-n2]), int(str2[len2-n2:])

    x = get_karatsuba_multiplication(high1, high2)
    y = get_karatsuba_multiplication(low1, low2)
    z = get_karatsuba_multiplication(high1+low1, high2+low2)

    multiplication = (
        x * (10**(2*n2)) + y + (z-x-y) * (10**n2)
    )
    return multiplication


if __name__ == "__main__":
    print("Please enter number 1:")
    num1 = int(input().strip())
    print("\nPlease enter number 2:")
    num2 = int(input().strip())
    multiplication = get_karatsuba_multiplication(num1, num2)
    # print(multiplication==num1*num2)
    print(f"\nmultiplication of {num1} and {num2} is {multiplication}")
