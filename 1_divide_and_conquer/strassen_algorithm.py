"""
Divide and conquer algorithm for matrix multiplication.

N has to be in 2^n form to apply strassen formula
Applicable on square matrices only

Strassen's algorithm
A = [[a, b], [c, d]]
B = [[e, f], [g, h]]
A, B = N*N
a, b, c, d, e, f, g, h = N/2*N/2
p1 = a(f-h)
p2 = (a+b)h
p3 = (c+d)e
p4 = d(g-e)
p5 = (a+d)(e+h)
p6 = (b-d)(g+h)
p7 = (a-c)(e+f)
A.B = [[p5+p4-p2+p6, p1+p2], [p3+p4, p1+p5-p3-p7]]
A.B = [[ae+bg, af+bh], [ce+dg, cf+dh]]

7 recursive calls instead of 8, which saves time
Generally Strassen’s Method is not preferred for practical applications
for following reasons.
1) The constants used in Strassen’s method are high and for a typical
application Naive method works better.
2) For Sparse matrices, there are better methods especially designed
for them.
3) The submatrices in recursion take extra space.
4) Because of the limited precision of computer arithmetic on
noninteger values, larger errors accumulate in Strassen’s algorithm
than in Naive Method.
"""
import numpy as np


def split_matrix(X):
    rows, cols = X.shape
    x1, x2, x3, x4 = (
        X[: rows // 2, : cols // 2],
        X[: rows // 2, cols // 2 :],
        X[rows // 2 :, : cols // 2],
        X[rows // 2 :, cols // 2 :],
    )

    return x1, x2, x3, x4


def strassen(A, B):
    if len(A) == 1:
        return np.dot(A, B)
    a, b, c, d = split_matrix(A)
    e, f, g, h = split_matrix(B)

    p1 = strassen(a, (f - h))
    p2 = strassen((a + b), h)
    p3 = strassen((c + d), e)
    p4 = strassen(d, (g - e))
    p5 = strassen((a + d), (e + h))
    p6 = strassen((b - d), (g + h))
    p7 = strassen((a - c), (e + f))

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return C


if __name__ == "__main__":
    A = np.random.randint(1, 10, size=(1024, 1024))
    B = np.random.randint(1, 10, size=(1024, 1024))
    result = strassen(A, B)
    ans = np.dot(A, B)
    print((ans == result).all())
