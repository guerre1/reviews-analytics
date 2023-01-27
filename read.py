date = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: 
	 	date.append(line)
	 	count += 1 # = count = count + 1
	 	if count % 1000 == 0: # '%'=求餘數;=>如果count 對1000的餘數是0
	 		print (len(date))
print('檔案讀取完畢,總共有' ,len(date), '筆資料')


sum_len = 0
for d in date:
	sum_len += len(d) #sum_len = sum_len + len(d)
print('留言平均長度是', sum_len/len(date),'個字')