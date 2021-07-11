from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request
from pprint import pprint
import multiprocessing as mp



# 조회 urls
URLS = [
	'http://www.daum.net/',
	'http://www.cnn.com/',
	'http://naver.com',
	'http://ruliweb.com/',
	'http://hiphople.com/',
	'http://www.funda.kr/',
	'http://8percent.kr/',
	'http://rapgenius.com/',
	'http://medium.com/'
]


def load_url(url, timeout):
	# timeout
	with urllib.request.urlopen(url, timeout=timeout) as conn:
		return conn.read()


def main():
	# 프로세스 풀 context 영역
	with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:

		print("Max worker count is {}".format(mp.cpu_count()))

		# Future 로드 (실행하는 것은 아님.)
		# 실행할 작업들을 예약하는 부분.

		# lit comprehension 형식으로 인자 전달
		# submit(실행할 함수, 첫번째 인자, 두번째 인자)
		future_to_url = {executor.submit(load_url, url, 5): url for url in URLS}

		# 중간확인
		pprint(future_to_url)

		# 예약된 작업들을 실행
		for future in as_completed(future_to_url):
			# dict 에서 {future 객체: url}
			url = future_to_url[future]   # 또는 future_to_url.get(future)

			try:
				# 실행 결과 받아오기
				data = future.result()
			except Exception as exc:
				# 예외 처리
				print("{} generated an exception: {}".format(url, exc))
			else:
				# 결과 확인
				print("{} page is {} bytes".format(url, len(data)))



if __name__ == "__main__":
	main()