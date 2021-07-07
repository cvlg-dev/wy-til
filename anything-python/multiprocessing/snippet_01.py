import logging
import threading
import time


def thread_func(name):
    # 서브스레드의 함수
    logging.info("Sub-thread %s: Starting", name)
    time.sleep(3)
    logging.info("Sub-thread %s: Finishing", name)


if __name__ == "__main__":
	# 메인스레드의 영역
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")
	logging.info("Main-thread: Before creating thread")

	# 서브스레드 함수 선언
	x = threading.Thread(target=thread_func, args=('First',))
	logging.info("Main-thread: Before running thread")

	# 서브스레드의 시작
	x.start()
	logging.info("Main-thread: Wait for subthread to finish")

	# 메인스레드 종료
	logging.info("Main-thread: All done")