def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
            list1[j+1]=temp
            
my_list=[90,45,12,87,34,54,22,55,44]
insertion_sort(my_list)
print(my_list)