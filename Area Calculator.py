import math as m

#2D SURFACES
def areaCircle():
    r= float(input("Input Radius:"))
    cirArea= m.pi * r**2
    return cirArea

def areaRect():
    L=float(input("LENGTH:"))
    W=float(input("WIDTH:"))
    rectArea=(L*W)
    return rectArea

def areaPar():
    print("    ______________")
    print("  /          |  /")
    print(" /          H| /")
    print("/____________|/")
    print("       B      " )
    print("Input,")
    B=float(input("B:"))
    H=float(input("H:"))
    parArea=(B*H)
    return parArea

def areaTrap():
    print("          a       ")
    print("     ______________")
    print("   /|             |\\")
    print("  / |             | \\")
    print(" /  |             |h \\")
    print("/___|_____________|___\\")
    print("          b           ")
    print("Input,")
    a=float(input("a:"))
    b=float(input("b:"))
    h=float(input("h:"))
    trapArea=(h*(a+b))/2
    return trapArea

#3D SURFACES
#CUBOID
def surfaceCuboid():
    Length=float (input("INPUT LENGTH:"))
    Width=float (input("INPUT WIDTH:"))
    Height=float (input("INPUT HEIGHT:"))
    sCuboid=(2*Length*Width)+(2*Width*Height)+(2*Length*Height)
    return sCuboid

#CYLINDER
def surfaceCylinder():
    Radius=float(input("INPUT RADIUS:"))
    l=float(input("INPUT HEIGTH:"))
    sCylinder=(m.pi*Radius**2*2)+(2*m.pi*Radius*l)
    return sCylinder

#SPHERE
def surfaceSphere():
    radius=float(input("INPUT RADIUS:"))
    sSphere=4*m.pi*radius**2
    return sSphere

#VOLUME
def Volume():
    print("\nFor a solid with uniform cross section, volume is found by multiplying the area of the cross section by the length of the solid's extrusion.")
    y=0
    CA=int
    while y==0:
            x = input(" 1. Circle\n 2. Rectangle\n 3. Parallelogram\n 4. Trapezium\nSELECT CROSS SECTION:")
            if x =="1":
                CA = areaCircle()
                y=1
            elif x =="2":
                CA = areaRect()
                y =1
            elif x =="3":
                CA = areaPar()
                y = 1
            elif x =="4":
                CA = areaTrap()
                y = 1
            else:
                y=0
                print("INVALID CHOICE TRY AGAIN")
    l=float(input("EXTRUSION:"))
    volume= CA*l
    return volume

#GEOMETRY FUNCTIONS
def HypotuneseFinder():
    H=float(input("Input Height:"))
    B=float(input("Input Base:"))
    Hypotunese= m.sqrt((H**2)+(B**2))
    return Hypotunese

#EQUATIONS MODE
#DEGREE 2; aX^2+bX+c=0
def Degree2():
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))

    det=float((b**2)-(4*a*c))
    if det >= 0:
        x1=(-b + m.sqrt(det)/2*a)
        x2=(-b - m.sqrt(det)/2*a)
        print("X1:",x1, "\nx2:",x2)
    else:
        Re=float(-b/(2*a))
        Im=float(m.sqrt(-det))/(2*a)
        print("X1:",Re,"+",Im,"i")
        print("X2:",Re,"-",Im,"i")

def Degree3():
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    d = float(input("d:"))


#SIMULTANEOUS EQUATIONS
#2 UNKNOWNS
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
        return "MATH ERROR!"

#3UNKNOWN
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
        return X, Y, Z
    else:
        return "SYNTAX ERROR!"

#MAIN FUNCTION
print("Hi there!\nWELCOME TO INFALC:\nWhat would you wish to do:")

while True:
    mode = int(input(" 1. AREA\n 2. VOLUME \n 3. GEOMETRY \n 4. EQUATION \n 5. DEGREE<>RADIANS\nSELECT MODE:"))
    if mode == 1:
        dimension = int(input(" 1. 2D SHAPES\n 2. 3D SHAPES\nSELECT DIMENSION:"))
        if dimension == 1:
            D2shape = int(input(" 1. Circle\n 2. Rectangle\n 3. Parallelogram\n 4. Trapezium\nSELECT SHAPE:"))
            if D2shape == 1:
                print("AREA:",areaCircle())
            elif D2shape == 2:
                print("AREA:", areaRect())
            elif D2shape == 3:
                print("AREA:", areaPar())
            elif D2shape == 4:
                print("AREA:", areaTrap())
            else:
                print("INVALID CHOICE!")

        elif dimension == 2:
            D3shape = int(input(" 1. Cube/Cuboid\n 2. Cylinder\n 3. Sphere\nSELECT SHAPE:"))
            if D3shape == 1:
                print("S.AREA:", surfaceCuboid())
            elif D3shape == 2:
                print("S.AREA:", surfaceCylinder())
            elif D3shape == 3:
                print("S.AREA:", surfaceSphere())
            else:
                print("INVALID CHOICE, TRY AGAIN!")
        else:
            print("INVALID CHOICE!")

    elif mode == 2:
        print("VOLUME:", Volume())

    elif mode == 3:
        find =int(input("\t1. Hypotunese\n\t2. SIN RULE\n\t3. COS RULE\nFIND:"))
        if find == 1:
            print("Hypotunese:", HypotuneseFinder())

    elif mode == 4:
        EqMode = int(input(" 1. FIND ROOTS\n 2. SIMULTANEOUS EQUATIONS\nmode:"))
        if EqMode == 1:
            degree = int(input(" 2\n 3\nDEGREE:"))
            if degree == 2:
                print(Degree2())
            elif degree == 3:
                print(Degree3())
            else:
                print("INVALID CHOICE!")

        elif EqMode == 2:
            unknowns = int(input(" 2\n 3\nUNKNOWNS:"))
            if unknowns == 2:
                print(Simultaneous2())
            elif unknowns == 3:
                print(Simultaneous3())
            else:
                print("INVALID CHOICE!")

    else:
        print("INVALID CHOICE!")