#unique numbers of the list
print("This program will find the unique numbers in the list.")
print("\n*For Example:\n List of numbers=[1,2,5,2,3,2,9,5]")
print(" In the above list, numbers i.e. 1,3,9 are UNIQUE as they are not repeated in the list.\n")
print("Enter list of numbers separated by a single space:")
l=[int(i) for i in input().split()]
uni=[]
for i in range(len(l)):
    cout=0
    for j in range(len(l)):
        if l[i]==l[j]:
            cout+=1
    if cout==1:
        uni.append(l[i])
print("\nThe unique numbers in the list are:",uni)
    
