print("                  POLY PEDIA")
print("-------------------------------------------------------------------------\n")
print('''Polygons are 2-dimensional shapes. They are made of straight lines, and
the shape is CLOSED (all the lines connect up).
Polygon comes from Greek. Poly- means "many" and -gon means ANGLE.

To Know more about Poygons see below  ''')
print("\n-------------------------------------------------------------------------")

x=int(input("Enter the number of sides of the Polygon:"))
if x==0 or x==1 or x==2:
    print("\n\nA Polygon requires minimum 3 sides")
if x==3:
    print('''
    IT IS TRIANGLE\n \n
    Area: ½ × base × height\n
    Perimeter: sum of side lengths of the triangle\n
    Number of vertices: 3\n
    Number of edges: 3\n
    Internal angle: 60° (for equilateral)\n
    Properties: Convex, cyclic, equilateral, isogonal, isotoxal
    Type: Regular polygon                                                          ''')

    print("---------------------------------------------------------------------")
if x==4:
    print('''
    IT IS QUADRILATERAL\n\n
    Area: ½ x diagonal x (sum of perpendicular heights)\n
    Perimeter: sum of sides of the quadrilateral\n
    Number of vertices: 4\n
    Number of edges: 4\n
    Internal angle: 90° (for square and rectangle)\n
    Sum of interior angles: 360°
    Type: Regular polygon

                                                               ''')
    print("---------------------------------------------------------------------")
if x==5:
    print('''
    IT IS PENTAGON
    Area: ½ × perimeter × apothem\n
    Perimeter: 5 x side\n
    Number of vertices: 5\n
    Number of edges: 5\n
    Internal angle: 108°\n
    Properties: Convex polygon, Equilateral polygon, Isogonal figure, Isotoxal figure, Cyclic\n
    Type: Regular polygon

                                                               ''')
    print("---------------------------------------------------------------------")
if x==6:
    print('''
    IT IS HEXAGON
    Area: 3√3/2 × (side)²\n
    Perimeter: 6 x side\n
    Number of edges: 6\n
    Internal angle: 120°\n
    Properties: Convex polygon, Equilateral polygon, Isogonal figure, Isotoxal figure, Cyclic\n
    Type: Regular polygon
                                                               ''')
    print("---------------------------------------------------------------------")
if x==7:
    print('''
    Area: ½ × perimeter × apothem\n
    Perimeter: 7 x side\n
    Number of vertices: 7\n
    Number of edges: 7\n
    Properties: Convex polygon, Equilateral polygon, Isotoxal figure, Isogonal figure, Cyclic\n
    Internal angle (degrees): ≈128.571°\n
    Type: Regular polygon

                                                               ''')
    print("---------------------------------------------------------------------")
if x==8:
    print('''
    IT IS HEPTAGON
    Area: 2 × (side length)² × (1+√2)\n
    Perimeter: 8 x side\n
    Number of vertices: 8\n
    Number of edges: 8\n
    Internal angle: 135°\n
    Properties: Equilateral polygon, Convex polygon, Isogonal figure, Isotoxal figure, Cyclic\n
    Type: Regular polygon

                                                               ''')
    print("---------------------------------------------------------------------")
if x==9:
    print('''
    IT IS NONAGON
    Area: ½ × perimeter × apothem\n
    Perimeter: 9 x side\n
    Number of vertices: 9\n
    Number of edges: 9\n
    Internal angle: 140°\n
    Properties: Convex polygon, Equilateral polygon, Isogonal figure, Isotoxal figure, Cyclic\n
    Type: Regular polygon

                                                               ''')
    print("---------------------------------------------------------------------")
if x==10:
    print('''
    IT IS DECAGON
    Area: ½ × perimeter × apothem\n
    Perimeter: 10 x side\n
    Number of vertices: 10\n
    Number of edges: 10\n
    Internal angle: 144°\n
    Properties: Convex polygon, Isogonal figure, Equilateral polygon, Isotoxal figure, Cyclic\n
    Type: Regular polygon

                                                               ''')
    print("---------------------------------------------------------------------")
if x>10:
    print("this POLY PEDIA is only upto decagon(10 sides)")
