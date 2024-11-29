''' to get list input  '''

a = list()
n = int(input("num of ele in  list "))
for i in range(n):
    print(i+1," input ")
    p = input()
    a.append(p)
print("list ",a)

n = int(input("list val num : "))
bb = list(map(str,input().strip().split()))
print(f"list for {n} elements is {bb}")


