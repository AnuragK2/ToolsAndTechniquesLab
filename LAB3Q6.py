m_list = []
n = int(input("Enter number of elements : ")) 
print(f"Enter {n} integers : ")
for _ in range(n):
    m_list.append(int(input("")))
m_list.sort()
print(f"Sorted list : {m_list}")
print(f"Reverse list : {m_list[::-1]}")
