from concurrent.futures import ThreadPoolExecutor
import logging
import queue
import random
import threading
import time


# 생산자
def producer(queue, event):
	"""
	생산자
		네트워크 대기 상태라 가정(서버)
	"""	
	while not event.is_set():
		message = random.randint(1, 2)
		logging.info("Producer got message: %s", message)
		queue.put(message)

	logging.info("Producer received event. Exiting.")

# 소비자
def consumer(queue, event):
	"""
	소비자
		응답 받고 소비하는 것으로 가정 또는 DB 저장
	"""
	while not event.is_set() or not queue.empty():
		message = queue.get()
		logging.info(
			"Consuer storing message: %s (size=%d)", message, queue.qsize()
			)

	logging.info("Consumer received event. Exiting.")



if __name__ == "__main__":
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")

	# 큐를 정의할 때는 사이즈의 정의가 매우 중요.
	pipeline = queue.Queue(maxsize=10)

	# event 초기값 0 설정
	event = threading.Event()

	# with context
	# producer, consumer 각각 스레드를 가지고 있으며, pipeline queue를 통해서 통신함.
	with ThreadPoolExecutor(max_workers=2) as executor:
		executor.submit(producer, pipeline, event)
		executor.submit(consumer, pipeline, event)


		# 실행시간조정
		time.sleep(1)

		logging.info("Main: About to set event")

		event.set()