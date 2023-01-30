f_name = input("Enter first name : ")
m_list = []
print("Enter 5 elements for list : ")
for _ in range(5):
    m_list.append(input(""))
print(f"{f_name} {' '.join(m_list)}")