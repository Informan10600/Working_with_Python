def Simultaneous3():
    print("\ta1X+b1Y+c1Z=d1\n\ta2X+b2Y+c2Z=d2\n\ta3X+b3Y+c1Z=d3")
    a1 = float(input("a1:"))
    b1 = float(input("b1:"))
    c1 = float(input("c1:"))
    d1 = float(input("d1:"))
    a2 = float(input("a2:"))
    b2 = float(input("b2:"))
    c2 = float(input("c2:"))
    d2 = float(input("d2:"))
    a3 = float(input("a3:"))
    b3 = float(input("b3:"))
    c3 = float(input("c3:"))
    d3 = float(input("d3:"))
    A1 = ((a1 * b2) - (b1 * a2))
    B1 = ((a1 * c2) - (c1 * a2))
    C1 = ((a1 * d2) - (a2 * d1))
    D1 = ((a1 * b3) - (b1 * a3))
    E1 = ((a1 * c3) - (c1 * a3))
    F1 = ((a1 * d3) - (a3 * d1))

    det1 = ((B1 * D1) - (A1 * E1))
    det2 = ((A1 * E1) - (B1 * D1))
    if det1 != 0.0:
        if det2 != 0.0:
            Y = ((B1 * F1) - (E1 * C1)) / ((B1 * D1) - (A1 * E1))
            Z = ((A1 * F1) - (D1 * C1)) / ((A1 * E1) - (B1 * D1))
            X = (d1 - (b1 * Y) - (c1 * Z)) / a1
            print("X:", X, "Y:",Y,"Z:",Z)
            return X, Y, Z
    else:
        return "SYNTAX ERROR!"


print(Simultaneous3())