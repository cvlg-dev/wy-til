from multiprocessing import Process
import logging
import time


# 멀티프로세스 영역
def proc_func(name):
	print("Sub-process {}: starting".format(name))
	time.sleep(3)
	print("Sub-process {}: finishing".format(name))



# main 영역
def main():
	format_ = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format_, 
	                    level=logging.INFO, 
	                    datefmt="%H:%M:%S")

	# 함수 인자 확인
	p = Process(target=proc_func, args=('First', ))
	logging.info("Main-process: before creating process")

	# 프로세스 시작
	p.start()
	logging.info("Main-process: during process")

	# logging.info("Main-process: terminated process")
	# p.terminate()

	logging.info("Main-process: joined process")	
	p.join()
	

	print("Process p is alive {}".format(p.is_alive()))


# main 시작
if __name__ == "__main__":
	main()