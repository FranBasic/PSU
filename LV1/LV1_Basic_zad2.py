try:
    ocjena = float(input("\nUnesite ocjenu (0.0 - 1.0): "))

    if ocjena < 0.0 or ocjena > 1.0:
        print("\nGreska, pogresan unos")
    elif ocjena >= 0.9:
        print("A")
    elif ocjena >= 0.8:
        print("B")
    elif ocjena >= 0.7:
        print("C")
    elif ocjena >= 0.6:
        print("D")
    else:
        print("F")

except ValueError:
    print("\nGreska, pogresan unos")