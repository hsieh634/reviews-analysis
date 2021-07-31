data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# 把1改為d就等於下列
good = [1 for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')
# output = [ d (number-1) for number in reference if (number %2 == 0)]
#  appendd進去^   運算			變數			清單			  篩選條件
print(good)

bad = ['bad' in d for d in data]
print(bad)