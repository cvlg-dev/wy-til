 import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
	
	def __init__(self):

		# 스레드는 스택만 별도이고, 나머지는 공유이므로, 
		# self.value는 스레드에서 공유되는 변수이다.
		# 코드영역, 데이터영역, 힙영역에서 공유됨.
		self.value = 0
		self._lock = threading.Lock()


	def update(self, n):
		logging.info("Thread %s: starting udpate", n)

		# mutex 또는 lock이 필요한 지점(thread synch가 필요한 지점)

		# # 방법 1) 
		# self._lock.acquire()
		# logging.info("Thread %s has lock", n)

		# local_copy = self.value
		# local_copy += 1
		# time.sleep(0.1)
		# self.value = local_copy

		# logging.info("Thread %s about to release lock", n)
		# self._lock.release()

		# logging.info("Thread %s: finishing update", n)

		# 방법 2)
		with self._lock:
			logging.info("Thread %s has lock", n)

			local_copy = self.value
			local_copy += 1
			time.sleep(0.1)
			self.value = local_copy

			logging.info("Thread %s about to release lock", n)

		logging.info("Thread %s: finishing update", n)



if __name__ == "__main__":
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")
	

	store = FakeDataStore()
	logging.info("Testing update. Starting value is %d", store.value)


	with ThreadPoolExecutor(max_workers=2) as executor:
		for n in ["First", "Second", "Third", "Four"]:
			executor.submit(store.update, n)

	logging.info("Testing update. Ending value is %d", store.value)

