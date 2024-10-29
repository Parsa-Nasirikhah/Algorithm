def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b
    else:
        n = max(len(str(a)), len(str(b)))
        mid = n//2
        x = a // (10 ** (mid))
        y = a % (10 ** (mid))
        z = b // (10 ** (mid))
        t = b % (10 ** (mid))
        xz = karatsuba(x,z)
        yt = karatsuba(y,t)
        sum = karatsuba(x + y, z + t) -xz -yt 
        return xz * (10 ** (2 * mid)) + (sum * (10 ** mid)) + yt

x = int(input())
y = int(input())
print(karatsuba(x, y))