data = []
count = 0 #計算

with open('reviews.txt','r') as f:
	for line in f: #for line means for loop.
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %:求倍數的餘數符號，count 是1001 % 1000 =1，count 7 % 3 = 1， 1000 == 0 一千的倍速
			print(len(data)) # print 大量資料很花時間

print(data[0])
