num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
n=int(input())
for i in num_list:
    if n in i:
        index1=num_list.index(i) 
        index2=i.index(n) 
print(str(index1)+" "+str(index2))


###
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
new=""
n=int(input())
for i in num_list:
    if n in i: 
        new+=str(num_list.index(i))+" "
        new+=str(i.index(n)) 
print(new)

##### 
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
n=int(input()) 
for i in num_list:
    if n in i:
        tuple_a=i 
        index=num_list.index(tuple_a)
        if n in tuple_a:
            sub_index=tuple_a.index(n)
print(str(index)+" "+str(sub_index))

### 
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
n=int(input()) 
for tuple_a in num_list:
    if n in tuple_a:
        tuple_index=num_list.index(tuple_a)
        nested_tuple_index=tuple_a.index(n)
print("{} {}".format(tuple_index,nested_tuple_index))
        
        

