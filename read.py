date = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: 
	 	date.append(line)
	 	count += 1 # = count = count + 1
	 	if count % 1000 == 0: # '%'=求餘數;=>如果count 對1000的餘數是0
	 		print (len(date))
print(len(date))
print(date[0])