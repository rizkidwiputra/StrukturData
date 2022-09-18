print("\n=====> Polindrom <=====\n")

def palindrom(objek):
    if len(objek) <= 1:
        return "--> Palindrom <--"
    elif objek[0] != objek[-1]:
        return "--> Bukan Palindrom <--"
    else :
        return palindrom(objek[1:-1])
bilangan = [1, 2, 3, 4, 4, 3, 2, 1]

print(f"{bilangan} {palindrom(bilangan)}")