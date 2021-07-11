import os
from multiprocessing import Process, current_process
import logging
import random
import time



def square(n):
	time.sleep(random.randint(1, 5))
	process_id = os.getpid()
	process_name = current_process().name

	# 제곱 연산 수행
	result = n * n * n

	# 정보 출력
	print("Process ID: {} // Process name: {}".format(process_id, process_name))
	print("Result of {} 3 square: {}".format(n, result))


# main 영역
def main():
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")


# main 시작
if __name__ == "__main__":
	
	parent_process_id = os.getpid()
	print("Parent process ID {}".format(parent_process_id))

	# process list
	ls_process = list()

	# 프로세스 생성 및 실행
	for i in range(1, 100+1):

		# Process naming. 프로세스를 실행할 때, ID를 name에 전달해서 지정할 수 있음. 문자를 받음.
		t = Process(name=str(i), target=square, args=(i,))

		# 프로세스를 process list에 담음
		ls_process.append(t)

		# 프로세스 시작
		t.start()

	for process in ls_process:
		process.join()

	# 종료
	print("Main-process is done.")

