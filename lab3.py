employee={'name':'[kusuma,supriya,sai,jyothi,bhaggi]','age':[24,31,28,31,45],'salary':[12000,23000,90000,34000,51000]}
print(employee)
print("The Employee salaries are:")
print(employee['salary'])
print("The salaries are:")
for v in employee['salary']:
    print(v)
L1 = employee['salary']
print("The listed salaries:", L1)
print("The sorted salarles are:", sorted(L1))
print("The reveresed salaries:",L1[::-1])
print("The minimum salary is:", min(L1))
print("The maximum salary is:", max(L1))
print("The total salaary is:", sum(L1))

#this is the lab for devops