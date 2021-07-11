# 프로세스 메모리 공유 예제 (공유가 되는 패턴)
from multiprocessing import Process, current_process, Value, Array
import os

# Value : 단일값을 공유하는 경우
# Array : List 형태로 데이터를 공유하는 경우


# 실행함수
def generate_update_nums(v: int):
	
	# shared value의 객체에 접근하기 위해서는 .value 로 접근
	for _ in range(50):
		v.value += 1

	print(current_process().name, "data: {}".format(v.value))


def main():
	
	# 디버깅을 위해 부모 프로세스 찍기
	parent_process_id = os.getpid()
	print("Parent process ID: {}".format(parent_process_id))

	# 프로세스 리스트 선언
	ls_process = list()


	# 프로세스 메모리 공유 확인
	## 단일값을 공유하기 때문에 Value 사용
	## data type도 명시해줘야 함.
	### i: int
	### c: character
	### f: float
	### l: long
	share_value = Value('i', 0)

	## List를 공유하는 경우 예시
	## 엄격한 초기값 설정, 데이터타입 명시
	# share_nums = Array('i', range(50))


	# 그외 사용 가능한 공유 메모리 모듈
	## from multiprocessing import shared_memory
	## from multiprocessing import Manager


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
	print("Final data in parent process: {}".format(share_value.value))

if __name__ == "__main__":
	main()