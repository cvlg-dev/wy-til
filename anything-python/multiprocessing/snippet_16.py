# Pipeline은 부모프로세스와 자식프로세스의 1:1 통신일 때.

from multiprocessing import Process, Pipe, current_process
import time
import os


# 프로세스 통신 구현 Pipe
## 5억을 세는 코드. 


# 실행함수
def worker(id, baseNum, conn):
	
	process_id = os.getpid()
	process_name = current_process().name

	# count 누적 변수
	sub_total = 0

	# 계산
	for i in range(baseNum):
		sub_total += 1


	# Producer
	conn.send(sub_total)
	conn.close()   # 파이프는 반드시 잠그는 과정이 필요함.

	# 정보 출력
	print("Process ID: {} // Process name: {} // ID: {}".format(process_id, process_name, id))
	print("Result: {}".format(sub_total))


def main():
	
	# parent process id
	parent_process_id = os.getpid()
	print("Parent process ID: {}".format(parent_process_id))

	# start time
	start_time = time.time()
	
	# 프로세스 예약 생성
	# 단, 파이프는 부모, 자식간의 1:1 통신이기에, 
	# for 문으로 하나의 부모에 자식 여러개를 생성하는 방식은 적합하지 않음.

	parent_conn, child_conn = Pipe()
	t = Process(name=str(1), target=worker, args=(1, 500000000, child_conn))

	# 시작
	t.start()

	# Join
	t.join()

	# end time
	end_time = time.time()

	# 결과값은 부모 프로세스에서 receive를 통해 받음
	total = parent_conn.recv()

	# 순수 계산 시간
	print("--- {} seconds ---".format(end_time - start_time))
	print("Main-processing Total Count = {}".format(total))
	print("Main-processing done.")



if __name__ == "__main__":
	main()






# 위와 동일한 작업을 하는 코드를 
# 멀티프로세싱을 하지 않고 실행하면 71초가 걸림. (snippet_17.py)
# 그러나 위의 코드는 24.4초가 걸림.
