
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('there are', len(data), 'reviews in total')

sum_len = 0
for d in data:
	sum_len += len(d)
print('the average length of the reviews is', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('there are', len(new), 'reviews length less than 100')
print(new[0])
print(new[1])
