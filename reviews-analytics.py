data = [] #清單

count = 0 #計算

with open('reviews.txt','r') as f:
	for line in f: #for line means for loop.
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %:求倍數的餘數符號，count 是1001 % 1000 =1，count 7 % 3 = 1， 1000 == 0 一千的倍速
			print(len(data)) # print 大量資料很花時間
print('檔案讀取完了，總共有',len(data),'筆資料')

sum_len = 0
for d in data: #(每一個d是一個字串)
	sum_len = sum_len + len(d)     # sum_len += len(d) #累計每一筆的長度
	#print(sum_len)
print('留言的平均長度，為',sum_len / len(data),'個字')  #總長度/len(data) 1百萬筆的資料