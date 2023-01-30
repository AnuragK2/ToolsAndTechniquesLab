d= input("Enter dimension of matrix : ")
m = int(d.split(" ")[0])
n = int(d.split(" ")[0])
matrix = []
print("Enter matrix : ")
for _ in range(m):
    tp = []
    for _ in range(n):
        tp.append(input(""))
    matrix.append(tp)
print(f"Matrix is: {matrix}")