

def validate(password):
	l=len(password)
	flag=1
	if l<6 or l>12 :
		flag=0
	for i in range(0,l):
		if ord(password[i])>=65 and  ord(password[i])<=90 :
			flag=1
			break
		else:
			flag=0

	for i in range(0,l):
		if ord(password[i])>=97 and  ord(password[i])<=122 :
			flag=1
			break
		else:
			flag=0

	for i in range(0,l):
		if ord(password[i])>=48 and  ord(password[i])<=57 :
			flag=1
			break
		else:
			flag=0


	for i in range(0,l):
		if (password[i])=='$' or (password[i])=='#' or password[i]=='@':
			flag=1
			break
		else:
			flag=0
			
	return flag


if __name__=="__main__":
	print "enter password"
	password=raw_input()
	flag=validate(password)
	if flag==1:
		print "valid"
	else:
		print"not valid"





