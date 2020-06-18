#Bubble Sorting 
def bubble_sort(list):
    itera,f=0,True
    while(f):
         f=False
         for i in range(len(list)-1):
             count=0
             for j in range(len(list) -i- 1):
                 if list[j] > list[j + 1]:
                    list[j],list[j+1]=list[j+1],list[j]
                    f=True
                    count+=1
             itera+=count
    print('\nThe sorted list:', list)
    print(f'Number of Iteration=\n',itera)


lst = []
size = int(input("\nEnter size of the list:"))

for i in range(size):
   
    lst.append(int(input("Enter the element: ")))
bubble_sort(lst)
