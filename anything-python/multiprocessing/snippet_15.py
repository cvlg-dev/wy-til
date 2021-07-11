from multiprocessing import Process, Queue, current_process
import time
import os


# 프로세스 통신 구현
## 5억을 세는 코드. 


# 실행함수
def worker(id, baseNum, q):
	
	process_id = os.getpid()
	process_name = current_process().name

	# count 누적 변수
	sub_total = 0

	# 계산
	for i in range(baseNum):
		sub_total += 1


	# Producer
	q.put(sub_total)

	# 정보 출력
	print("Process ID: {} // Process name: {} // ID: {}".format(process_id, process_name, id))
	print("Result: {}".format(sub_total))


def main():
	
	# parent process id
	parent_process_id = os.getpid()
	print("Parent process ID: {}".format(parent_process_id))

	# process list
	ls_process = list()

	# start time
	start_time = time.time()

	# Queue 선언
	q = Queue()

	for i in range(5): # 1 ~ 100 적절히 ... 

		# 프로세스 예약 생성
		t = Process(name=str(i), target=worker, args=(i, 100000000, q))

		# 배열에 담기
		ls_process.append(t)

		# 시작
		t.start()

	# Join
	for process in ls_process:
		process.join()

	# end time
	end_time = time.time()

	# 순수 계산 시간
	print("--- {} seconds ---".format(end_time - start_time))

	total = 0

	# Join이 끝날 시, 큐에 종료 플래그 부여
	q.put("exit")

	# 대기
	while True:
		tmp = q.get()
		if tmp == "exit":
			break
		else:
			total += tmp


	print("Main-processing Total Count = {}".format(total))
	print("Main-processing done.")



if __name__ == "__main__":
	main()






# 위와 동일한 작업을 하는 코드를 
# 멀티프로세싱을 하지 않고 실행하면 71초가 걸림. (snippet_17.py)
# 그러나 위의 코드는 6.3초가 걸림.
