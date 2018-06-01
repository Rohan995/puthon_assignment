n=int(raw_input("enter size of list"))
alist=list()
for _ in range(0,n):
	alist.append(tuple(map(int,raw_input().split())))
print sorted(alist,key=lambda x:x[-1])