__author__ = 'rich'
name = input("name?")
age = int(input("how old are you, {0}?".format(name)))

if 18 <= age <= 30:
	print("come on in")
else:
	print("gtfo")
