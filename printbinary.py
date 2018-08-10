a = int(input("decimal number:"))

if not a:
	print("0")
	exit(0)

string = ''

while a:
	string = str(a % 2) + string
	a = a // 2
print(string)
