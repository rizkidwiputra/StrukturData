def palindrom(array,start, panjang):
    tengah = panjang//2
    belakang =+1
    if tengah == start:
        return "Palindrom"
    elif array[start] != array[-belakang]:
        return "Bukan Palindrom"
    else:
        return palindrom(array, belakang, len(array))

bilangan = [1,2,3,4,4,3,2,1]

print(bilangan, "adalah", palindrom(bilangan, 0, len(bilangan)))