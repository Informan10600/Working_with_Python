def Simultaneous2():
    print("\tAx+By=C\n\tDx+Ey=F")
    A =float(input("A:"))
    B =float(input("B:"))
    C =float(input("C:"))
    D =float(input("D:"))
    E =float(input("E:"))
    F =float(input("F:"))

    det1 =((B*D)-(A*E))
    det2 =((A*E)-(B*D))
    if det1 !=0.0:
        if det2 !=0.0:
            X =((B*F)-(E*C))/((B*D)-(A*E))
            Y =((A*F)-(D*C))/((A*E)-(B*D))
            return X, Y
    else:
        return "SYNTAX ERROR!"


print (Simultaneous2())