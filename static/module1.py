arr=list(map(int,input().split()))
s = int(input())
pref= [0]
c= 0
for i in arr:
    c+=i
    pref.append(c)
k=0
for i in range(0,len(pref)):
    if k == 1:
        break
    for j in range(i,len(pref)):
        if pref[j] - pref[i-1] == s:
            print(i+1,j+1)
            k=1
            break
        print(pref[i],pref[j])

