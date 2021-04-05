# Docker-101-for Datascientist

## 예시: 파이토치 이미지를 가져와서 주피터 개발환경 만들기 (CPU env)

- 기본
    - 도커 이미지 리스트 보기
        - `docker image ls`
    - 도커 컨테이너 리스트 보기
        - `docker container ps -a` (구식 명령)
        - `docker container ls -a` (docker 1.13 부터 추가) - 사실 상 큰 차이점은 없음
            - -a --all: 현재 띄워져있는 컨테이너 뿐만 아니라 종료된 컨테이너를 포함한 모든 컨테이너의 리스트를 출력
- pytorch 이미지 가져오기
    - docker command
        - `docker pull pytorch/pytorch`
    - 설명
        - `docker pull {image_name}`
            - 원하는 태그를 정하여 pull 한다. 아니면 latest나 default이미지로 pull 받는다.
- 이미지로 컨테이너 만들기
    - docker command
        - docker run {image}
        - `docker run -itd —-name pytorch -v ~/dev/:/workspace -p 8989:8888  pytorch/pytorch`
    - 설명
        - `docker run`
            - `docker create` + `docker start` 의 역할을 한다. 따라서 매번 이 명령어를 통해 컨테이너를 띄우는 것은 바람직하지 못 함
                - create : 최초 이미지에 컨테이너 레이어의 씌움
                - start : 컨테이너를 띄움
        - `-i` : interactive 사용자가 입출력을 할 수 있는 단계 (파이프라이닝, 키보드 입력 등)
        - `-t` : 가상 터미널 환경을 에뮬레이팅 한다 (터미널 제공) → -it 가 가장 보편적
        - `-d`
            - detached 된 상태에서도 컨테이너를 백그라운드에서 실행
            - 이 옵션이 없을 경우, 컨테이너를 나왔을 때 컨테이너가 종료됨
            - run the container in detached mode (in the background)
        - `--name {name}` : 컨테이너의 이름을 지정
        - `-v {local_path}:{remote_path}` : 호스트의 디스크 경로를 컨테이너의 경로와 공유
        - `-p {local_port}:{remote_port}`
            - 호스트의 포트를 컨테이너의 포트와 연결
            - 주피터노트북을 실행하여 로컬에서 작업할 경우를 고려해볼 수 있다.
        - `--restart=always` (optional)
    - Alternative
        - docker create + docker start
            - `docker create -it --name pytorch -v ~/dev/:/workspace -p 8989:8888 pytorch/pytorch`
            - `docker start pytorch`
            - `docker attach pytorch` or `docker exec -i -t pytorch bash`

- 컨테이너 붙이기
    - `docker start {container_id}` → 실행
    - `docker attach {container_id}` → 접속
- 컨테이너 떼기
    - `ctrl + q + p` (순서대로) → 실행 정지하지 않고 떼기
    - `exit` or `ctrl+d` → 컨테이너 종료
- 컨테이너 종료 / 삭제 → 이미지 삭제
    - 도커는 기본적으로 실행 중인 컨테이너 / 이미지는 삭제할 수 없으므로, 우선 중지/종료가 필수임
    - `docker ps -a` → 도커 컨테이너 전체 리스트
        - `docker ps -a -q -f status=exited`
    - `docker stop {container_id}` → 컨테이너 중지
    - `docker rm {container_id}` → 컨테이너 삭제
        - `docker rm $(docker container ls -a -q -f status=exited)`
    - `doker rmi {image_id}` → 이미지 삭제
- 내가 작성한 도커 이미지, 다른 PC에서 쓰기 (도커허브를 사용하지 않는 방법)
    - `docker commit {container_id} {image name}:{tag}` → 현재의 컨테이너를 새로운 이미지로 생성
    - `docker save -o {path for generated tar file} {image_name}` → 이미지를 tar 파일로 젖아
        - 예) `~/dev/sample_test_image.tar pytorch/pytorch`
    - `docker load -i {path to image tar file}` → tar 파일을 이미지로 생성

# 3. Reference

- [Docker Command Documentation](https://docs.docker.com/engine/reference/commandline/run/)
- [https://www.popit.kr/개발자가-처음-docker-접할때-오는-멘붕-몇가지/](https://www.popit.kr/%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%B2%98%EC%9D%8C-docker-%EC%A0%91%ED%95%A0%EB%95%8C-%EC%98%A4%EB%8A%94-%EB%A9%98%EB%B6%95-%EB%AA%87%EA%B0%80%EC%A7%80/)
- [https://joont92.github.io/docker/container-다루기/](https://joont92.github.io/docker/container-%EB%8B%A4%EB%A3%A8%EA%B8%B0/)
- [https://89douner.tistory.com/96?category=878197](https://89douner.tistory.com/96?category=878197)
- [https://www.popit.kr/개발자가-처음-docker-접할때-오는-멘붕-몇가지/](https://www.popit.kr/%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%B2%98%EC%9D%8C-docker-%EC%A0%91%ED%95%A0%EB%95%8C-%EC%98%A4%EB%8A%94-%EB%A9%98%EB%B6%95-%EB%AA%87%EA%B0%80%EC%A7%80/)
- [https://joont92.github.io/docker/container-다루기/](https://joont92.github.io/docker/container-%EB%8B%A4%EB%A3%A8%EA%B8%B0/)
- [https://gyehwancho.github.io/project_1/machinelearning/docker-for-ml/](https://gyehwancho.github.io/project_1/machinelearning/docker-for-ml/)
- [https://www.44bits.io/ko/post/easy-deploy-with-docker](https://www.44bits.io/ko/post/easy-deploy-with-docker)
- [https://hanseokhyeon.tistory.com/entry/Pycharm-Docker로-딥러닝-개발-준비](https://hanseokhyeon.tistory.com/entry/Pycharm-Docker%EB%A1%9C-%EB%94%A5%EB%9F%AC%EB%8B%9D-%EA%B0%9C%EB%B0%9C-%EC%A4%80%EB%B9%84)
- [도커와 쿠버네티스를 이해하기 위한 로드맵 & 가이드](https://moons08.github.io/programming/dockerToK8s/)
- [딥러닝을 위한 도커 시작하기 (Docker for DeepLearning) - 3편](https://youtu.be/xtHOsyLjOlk)