import logging
import threading
import time


def thread_func(name, d):
    # 서브스레드의 함수
    logging.info("Sub-thread %s: Starting", name)
    
    for i in d:
        print("{}: ".format(name), i)   
        
    logging.info("Sub-thread %s: Finishing", name)



if __name__ == "__main__":
	# 로깅
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")
	
	# 메인스레드의 영역
	logging.info("Main-thread: Before creating thread")
	
	


	# 서브스레드 함수 선언
	x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
	y = threading.Thread(target=thread_func, args=('Two', range(10000)), daemon=True)
	logging.info("Main-thread: Before running thread")

	# 서브스레드의 시작
	x.start()
	y.start()

	# DaemonThread 확인
	print(x.isDaemon())

	# 서브스레드의 종료까지 기다림.
	# 따라서 데몬스레드의 의도와는 맞지 않아, 절대 best-practice가 아님.
	# x.join()
	# y.join()

	logging.info("Main-thread: Wait for subthread to finish")

	# 메인스레드 종료
	logging.info("Main-thread: All done")    