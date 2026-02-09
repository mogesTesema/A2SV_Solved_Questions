
figures = {"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
total_face = 0
n = int(input())
for _ in range(n):
    obj = input()
    total_face += figures[obj]
print(total_face)