import logging
from concurrent.futures import ThreadPoolExecutor
import time



def task(name):
	logging.info('Sub-Thread %s: starting', name)

	result = 0
	for i in range(10001):
		result += i

	logging.info('Sub-Thread %s: finishing result: %d', name, result)

	# 결과값이 있을 경우 출력 가능.
	return result


def main(num_worker):
	# 로깅
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")
	
	# 메인스레드의 영역
	logging.info("Main-thread : before creating and running thread")


	# 실행방법1
	# max_workers : 작업의 개수가 넘어가면, 직접 worker의 개수를 설정하는 것이 유리함.
	executer = ThreadPoolExecutor(max_workers=num_worker)
	task1 = executer.submit(task, ('First', ))
	task2 = executer.submit(task, ('Two', ))

	# 결과값이 있을 경우
	print(task1.result())
	print(task2.result())


if __name__ == "__main__":
	main(num_worker=3)


