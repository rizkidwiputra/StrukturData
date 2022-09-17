print("\n=====> Fibonacci <=====\n")

def fibonaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)

print("fibonaci deret ke-5  :", fibonaci(5))
print("fibonaci deret ke-7  :", fibonaci(7))
print("fibonaci deret ke-10 : ", fibonaci(10))

#mabar