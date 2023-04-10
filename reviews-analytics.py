data = [] #清單
count = 0 #計算

with open('reviews.txt','r') as f:
	for line in f: 
	#for line means for loop.
		data.append(line)
		count += 1 
		# count = count + 1
		if count % 1000 == 0: 
		# %:求倍數的餘數符號，count 是1001 % 1000 =1，count 7 % 3 = 1， 1000 == 0 一千的倍速
			print(len(data)) 
			# print 大量資料很花時間
print('檔案讀取完了，總共有',len(data),'筆資料')

#留言的平均長度是多少

sum_len = 0
for d in data: 
#(每一個d是一個字串)
	sum_len = sum_len + len(d)     
	# sum_len += len(d) #累計每一筆的長度
	#print(sum_len)
print('留言的平均長度，為',sum_len / len(data),'個字')  
#總長度/len(data) 1百萬筆的資料

# 小於100的留言有多少筆

new = []
for d in data:  
#d是字串，data是裝著一百萬筆留言的清單
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'長度<100') 
#for loop 執行完才print，不然會一直print.
print(new[0]) 
#print new 裡面第一筆留言
print(new[1])