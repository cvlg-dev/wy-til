import time

if __name__=="__main__":
	start = time.process_time()
	total = 0
	for _ in range(500000000):
		total += 1
	end = time.process_time()
	print("--- {} seconds ---".format(end - start))
	print("Total count {}".format(total))



## 72초 걸림.