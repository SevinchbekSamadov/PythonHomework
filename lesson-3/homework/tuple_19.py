tp = (1,2,5,3,7)
removing_ele = 5

new_tp = (i for i in tp if i != removing_ele)
print(tuple(new_tp))