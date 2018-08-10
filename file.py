with open("words.txt", mode='a') as f:
	for i in range(13):
		print("{:>2} times 2 is {}".format(i,i*2), file=f)
