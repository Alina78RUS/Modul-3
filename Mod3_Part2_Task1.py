''' В произвольном списке найти повторяющиеся элементы
 и добавить в новый список.'''
L=[7,5,7,'hello','hello',1,3,'world',7]
L_count=[]


for x in L:
	count=0
	for y in L:
		if y==x:
			count+=1
	L_count.append(count)
	
L_counter=set()
i=0
while i < len(L):
	if L_count[i]!=1:
		L_counter.add(L[i])
	i +=1


print (L_counter)
