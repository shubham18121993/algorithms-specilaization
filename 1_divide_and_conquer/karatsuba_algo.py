"""
Programming assignment #1
karatsuba algorithm is used for multiplication of 2 "n" digit number
"""

def karatsuba_algorithm_1(num1, num2):
    str1, str2 = str(num1), str(num2)
    len1, len2 = len(str1), len(str2)

    n = min(len1, len2)
    if n==1:
        return num1 * num2
    n2 = n//2
    high1, low1 = int(str1[:len1-n2]), int(str1[len1-n2:])
    high2, low2 = int(str2[:len2-n2]), int(str2[len2-n2:])

    x = karatsuba_algorithm_1(high1, high2)
    y = karatsuba_algorithm_1(low1, low2)
    z = karatsuba_algorithm_1(high1+low1, high2+low2)

    multiplication = (
        x * (10**(2*n2)) + y + (z-x-y) * (10**n2)
    )
    return multiplication


def karastuba_algorithm_2(num1, num2):
    if num1 < 100 or num2 < 100:
        return num1*num2

    s1, s2 = str(num1), str(num2)

    n = max(len(s1), len(s2))
    if n%2 == 1:
        n = n+1

    n2 = int(n/2)
    try:
        xl, xr = int(s1[:-n2]), int(s1[-n2:])
        yl, yr = int(s2[:-n2]), int(s2[-n2:])
    except:
        print(n2)
        print(s1)
        print(s2)


    z1 = karastuba_algorithm_2(xl, yl)
    z2 = karastuba_algorithm_2(xr, yr)
    z3 = karastuba_algorithm_2(xl+xr, yl+yr)
    z4 = z3 - z2 - z1
    ans = z1*(10**(n)) + z4*(10**(n2)) + z2
    return ans


if __name__ == "__main__":
    print("Please enter number 1:")
    num1 = int(input().strip())
    print("\nPlease enter number 2:")
    num2 = int(input().strip())
    method1 = karatsuba_algorithm_1(num1, num2)
    method2 = karastuba_algorithm_2(num1, num2)
    method3 = num1*num2
    print(f"method1: {method1} \n")
    print(f"method2: {method2} \n")
    print(f"method3: {method3} \n")
    print(f"{method1==method3}")
    print(f"{method2==method3}")
