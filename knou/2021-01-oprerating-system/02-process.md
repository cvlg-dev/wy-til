# 1. 프로세스

## 1.1. 프로세스란

- 실행중인 프로그램
	- 프로그램이 실행되면 프로세스마다 프로세스 아이디 `pid`를 부여받음
- 프로그램 vs 프로세스
	- 프로그램: 동작을 하지 않는 정적, 수동적 개체
	- 동작을 하는 능동적 개체

- 각각의 프로세스는 운영체제로부터 자원을 할당 받아서 동작함
	- 자원: CPU, 메모리, 입출력장치, 파일 등 모두 자원이 됨.
	- 동작: CPU가 프로세스의 명령을 실행하고 작업을 수행함.

### 1.1.1. 프로세스 관리자의 역할

- 프로세스를 생성 및 삭제
- 프로세스 실행(CPU할당)을 위한 스케쥴 결정
- 프로세스의 상태를 관리하며 상태 전이를 처리함. (상태 전이?)

## 1.2. 프로세스의 상태

### 1.2.1. 프로세스의 **5-상태 모델**

1. 생성: 처음 작업이 시스템에 주어진 상태
	- 작업의 요청이 들어왔을 때 작업의 내용을 인지하고, 작업을 수행하기 위해 필요한 자원이 무엇인지 파악해야함.
2. 준비: 실행 준비가 되어 CPU할당을 기다리는 상태
3. 실행: 프로세스가 처리되는 상태
4. 대기: 프로세스가 특정 자원을 할당받을 때까지 또는 I/O작업이 끝날 때까지 작업이 보류되는 상태
5. 종료: 모든 처리가 완료되어 사용자에게 반환되는 상태

### 1.2.2. **상태의 전이 과정**

- 생성 -> 준비
	- 작업 요청이 되면, 필요한 자원이 준비되고 마지막으로 CPU만 할당하면 되는 상태일 때 거치는 과정
	- 스케줄러가 호출됨
- 준비 -> 실행 
	- 스케불러에 의해 해당하는 프로세스에 CPU가 할당이 되는 과정
	- 디스패치라고 부름
- 실행 -> 준비
	- 다시 준비 상태에서 CPU를 기다리는 과정
	- 할당시간이 만료됐을 때, 또는 더 높은 우선순위의 프로세스가 있을 때 발생함. 
- 실행 -> 대기
	- 어떠한 I/O의 이벤트를 기다리고 있을 때, 
	- 페이지 교환 같은 작업이 발생하기를 기다릴 때,
	- 대기 동안 다른 프로세스에 CPU가 할당될 수 있도록 하기 위함.
- 대기 -> 준비
	- 재개 조건이 만족했을 때
- 실행 -> 종료
	- 모든 작업이 완료되었을 때
	- 강제로 프로세스가 종료될 때.

## 1.3. 프로세스 제어 블록 (PCB)

### 1.3.1. PCB의 역할

- 프로세스의 관리를 위한 목적
- 프로세스의 정보를 보관
- PCB는 각 프로세스마다 존재함.
- 프로세스가 진행함에 따라 내용이 변경됨.

### 1.3.2. PCB가 가지는 정보

- 프로세스 상태
- 프로세스 번호
- 프로세스 카운터
	- 다음 프로세스 명령의 위치 및 주소
- 레지스터
- 메모리
- 프로세스 우선 순위
- 회계정보


## 1.4. 프로세스의 생성과 종료

### 1.4.1. 프로세스의 생성 작업

- 프로세스의 이름 결정 (PID)
- 준비 큐에 삽입
- 초기 우선순위 부여
- 프로세스 제어 블록 생성

**프로세스 생성방법: 시스템 호출**

- 하나의 프로세스가 프로세스 생성 시스템 호출을 통해 새로운 프로세스를 생성함. (예시: `fork()`)
- 호출하는 프로세스: 부모 프로세스
	- 시스템 프로세스, 사용자 프로세스 모두 부모 프로세스가 가능함.
- 생성되는 프로세스: 자식 프로세스

**생성되는 프로세스의 자원**

- 운영체제로부터 직접 얻는 경우
- 부모 프로세스 자원의 일부를 얻는 경우
	- 주로 부모프로세스의 자원으로 제한함
	- 과도한 자식프로세스 생성에 따른 시스템 과부하를 방지하기 위함

### 1.4.2. 프로세스의 종료 작업

-  프로세스의 마지막 명령이 실행을 마치는 경우
- 프로세스 종료 시스템 호출을 통하는 경우 (예: `exit()`)
- 프로세스 종료 후 부모 프로세스에게 실행결과를 되돌려 줌

**프로세스 종료 시스템 호출**

- 부모에 의해서만 호출
- 자식 프로세스가 할당된 자원의 사용을 초과할 때 혹은 더 이상 필요치 않을 때

## 1.5. 프로세스 간의 관계

### 1.5.1. 독립적 프로세스

- 의미
	- 다른 프로세스의 영향을 받지도 않고 주지도 않음
- 프로세스 상태
	- 다른 프로세스와 공유하지 않음
- 실행
	- 결정적, 재생 가능
	- 다른 프로세스와 무관하게 중단 및 재시작 가능
- 데이터
	- 다른 프로세스와 공유하지 않음

### 1.5.2. 유기적 프로세스

- 의미
	- 다른 프로세스와 영향을 주고받음
- 프로세스 상태
	- 다른 프로세스와 공유함
- 실행
	- 비결정적, 재생 불가능 (다른 프로세스에 의존적이라, 결과물이 달라질 수 있음.)
- 데이터
	- 다른 프로세스와 공유함.

# 2. 쓰레드(Thread)

## 2.1. 프로세스의 특징 및 제한

- 처리의 기본 단위 (하나의 처리)
- 자원 소유의 단위 (하나의 주소공간)
- 디스패칭의 단위 (하나의 제어 흐름)

BUT, 단일 프로세스 내에서는 동시처리가 불가능함

## 2.2. 쓰레드의 등장

- 정의
	- 프로세스 내에서의 다중처리를 위해 제안된 개념
	- 하나의 프로세스 내에는 하나 이상의 쓰레드가 존재함.
	- 하나의 쓰레드 내에서는 하나의 실행점만 존재함. (디스패칭의 단위)
	- 실행에 필요한 최소한의 정보만을 가지며, 자신이 속해있는 프로세스의 실행환경을 공유함.

- 장점
	- 멀티 CPU 혹은 멀티코어 시스템에서는 병렬처리가 가능함.
	- 처리 속도 별로 쓰레디가 나눠진 경우 효율적인 처리가 가능하마.


# 3. 스케줄링

## 3.1. 단계별 스케줄링

- 상위단계
- 중간단계
- 하위단계 

### 3.1.1 상위단계 스케줄링

- 시스템에 들어오는 작업들을 선택하여 프로세스를 생성한 후, 프로세스 준비 큐에 전달
- 선택기준:
	- 시스템의 자원을 효율적으로 이용할 수 있도록 하는 것.
- 입출력(I/O) 중심 작업과 연산 중심 작업을 균형있게 선택함.

### 3.1.2. 하위단계 스케줄링

- 사용가능한 CPU를 준비상태의 어느 프로세스에게 배당할지를 결정
- CPU를 배당받은 프로세스는 결국 실행상태가 되어 프로세스가 처리됨.
- 수행주체: 디스패처(dispatcher)

### 3.1.3. 중간단계 스케줄링

- 프로세스를 일시적으로 메모리에서 제거하여 중지시키거나 다시 활성화시킴
- 시스템에 대한 단기적인 부하를 조절함

## 3.2. 스케줄링 정책

### 3.2.1. 스케줄링 기본 목표

- 공정성
	- 모든 프로세스가 적정 수준에서 CPU작업을 할 수 있게 함.
- 균형
	- 시스템의 자원들이 충분히 활용될 수 있게 함.

### 3.2.2. 운영체제의 특징에 맞춘 스케줄링
	
- 일괄처리 운영체제
	- 처리량 극대화
	- 반화시간의 최소화
	- CPU 활용의 극대화

- 대화영 운영체제
	- 빠른 응답시간
	- 과대 대기시간 방지

- 실시간 운영체제
	- 처리기한을 맞춰야 함.

### 3.2.3. 선점 스케줄링 정책 (Preemptive)

- 진행 중인 프로세스에 인터럽트를 걸고 다른 프로세스에 CPU를 할당하는 스케줄링 전략.
	- 이미 사용 중인 프로세스를 다른 프로세스가 빼았을 수 있는 정책
- 높은 우선순위의 프로세스를 긴급하게 처리하는 경우에 유용함.
- 대화식 시분할 시스템에서 빠른 응답시간을 유지하는데 유용함.
- 문맥 교환에 따른 오버헤드가 발생함.
	- 문맥: CPU의 모든 레지스터와 기타 운영체제에 따라 운영되는 프로세스의 상태

### 3.2.4. 비선점 스케줄링 정책 (Nonpreemptive)

- 프로세스가 CPU를 할당받아 실행이 시작되면, 작업 자체가 I/O 인터럽트를 걸거나 작업을 종료할 때까지 실행상태에 있게 됨.
- 모든 프로세스가 공정하게 순서에 따라 실행됨.
	- 응답시간이 예측 가능함.
- 짧은 프로세스가 긴 프로세스를 기다리게 될 수 있음.