lst = [1,2,3,4,5]
nested_lst = []

for i in range(len(lst)):
    res = [lst[i]]
    
    nested_lst.append(res)
  
    for j in range(i+1,len(lst)):
        res.append(lst[j])
     
        nested_lst.append(res)
        
    res = []
print(nested_lst)