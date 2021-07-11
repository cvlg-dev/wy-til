# 프로세스 메모리 공유 예제 (공유가 되지 않는 패턴)

from multiprocessing import Process, current_process
import os



# 실행함수
def generate_update_nums(v: int):
	
	for _ in range(50):
		v += 1

	print(current_process().name, "data: {}".format(v))


def main():
	
	# 디버깅을 위해 부모 프로세스 찍기
	parent_process_id = os.getpid()
	print("Parent process ID: {}".format(parent_process_id))

	# 프로세스 리스트 선언
	ls_process = list()

	# 프로세스 메모리 공유 확인
	share_value = 0

	for _ in range(1, 10 + 1):
		# 생성
		p = Process(target=generate_update_nums, args=(share_value,))

		# 프로세스 객체를 담기
		ls_process.append(p)

		# 실행
		p.start()

	# join
	for p in ls_process:
		p.join()

	# 최종 프로세스 부모 변수 확인. 공유가 되었는지 확인.
	print("Final data in parent process: {}".format(share_value))


if __name__ == "__main__":
	main()