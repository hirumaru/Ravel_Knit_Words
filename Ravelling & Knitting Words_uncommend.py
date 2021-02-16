def ravel(q):
    x=''
    y=''
    for i in q:
        for j in range(len(i)):
            x+=i
            y+=x
    return y
q=input('masukan kata : ')
print(ravel(q))

# === knitting masih kurang mas kal :(

def knit(p):
    list_p=[]
    list_p_copy=[]
    list_p.extend(p)
    x=''
    for i in list_p:
        for j in range(len(i)):
            if i == list_p[j+1]:
                list_p_copy.extend(i)
    x = "".join(list_p_copy)
    return x

a=input('masukan kata : ')
print(knit(a))
