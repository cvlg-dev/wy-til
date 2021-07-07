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


	# 실행방법 2
	with ThreadPoolExecutor(max_workers=num_worker) as executer:
		tasks = executer.map(task, ['First', 'Second', 'Third'])

	# 결과 확인
	print(list(tasks))


if __name__ == "__main__":
	main(num_worker=3)

