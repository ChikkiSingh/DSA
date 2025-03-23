# write a python function implement bubble sort.
def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
                
# modify bubble_sort ;
def modify_bubble_sort(data_list):
    result=False
    for r in range(1,len(data_list)):
        result=False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                result=True
            if not result:
                break

l=[12,8,15,89,54,23,14,99,55]
modify_bubble_sort(l)
print(l)