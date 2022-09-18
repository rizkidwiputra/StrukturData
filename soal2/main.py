print("\n=====> Polindrom <=====\n")

def palindrom(array, start, panjang):
    tengah = panjang//2
    if tengah == start:
        return "--> Palindrom <--"
    elif array[start] != array[-(start+1)]:
        return "Bukan Palindrom"
    else:
        return palindrom(array, start+1, len(array))

bilangan = [1,2,3,4,4,3,2,1]

print(f"{bilangan} {palindrom(bilangan, 0, len(bilangan))}")