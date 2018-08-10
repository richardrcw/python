str = input("Enter string :")

vowels = {'a','e','i','o','u','y'}
str = set(str)
str.difference_update(vowels)
print(sorted(str))
