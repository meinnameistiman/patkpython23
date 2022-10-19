def flatten(x):
    
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            flat_liste.append(i)

x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flat_liste=[]
flatten(x)
print(flat_liste)