# 0. 자료구조? 알고리즘?

- 자료구조 Data Structure
    - 대량의 데이터를 효율적으로 관리할 수 있는 데이터의 구조
    
<br>

- 체계적인 데이터 구조화의 필요성
    - 코드 상에서 효율적인 데이터 처리하기 위함
    - 어떤 데이터 구조를 사용하느냐에 따라 효율이 달라짐.

<br>

- 알고리즘이란
    - 어떠한 문제를 풀기 위한 절차 / 방법
    - 특정 문제에 해당하는
        - 특정 입력을 넣으면
        - 특정 출력을 얻을 수 있도록 하는 프로그래밍
  
<br>  
        
- 문제를 푸는 방법은 각양각색이지만, 다음을 고려하여 계산을 하고 최적의 방법을 찾는다.
    - 어느 정도의 시간을 쓰는가?
    - 어느 정도의 저장 공간을 활용하는가?
    
<br>    
    
- 자료구조와 알고리즘이 중요한 이유
    - 어떤 자료구조와 알고리즘을 쓰느냐에 따라 성능 면에서 아주 큰 차이가 생김.
    
* * * 

# 1. 배열 : Array

- 같은 종류의 데이터를 순차적으로 저장하는 형태의 데이터타입

## 1.1. 배열의 필요성

- 같은 종류의 데이터를 효율적으로 관리
- 같은 종류의 데이터를 **순차적**으로 데이터를 저장

## 1.2. 배열의 장단점

(파이썬이 아닌 C로 봤을 때)

장점:
- 구현이 쉬움.
- 빠른 접근이 가능함. 
    - 인덱스index가 매겨지기에, 첫 데이터(인덱스 0)의 위치를 기준으로 상대적인 위치의 데이터에 빠르게 접근 가능
    - 즉, 일단 만들어 놓으면 빠른 접근이 가능.
- 검색에 용이함.

<br>

단점:
- 데이터 추가와 삭제가 어려움.
    - 미리 최대 길이를 지정해야 하기 때문
- 데이터를 추가하거나 삭제를 하면 길이에 변화가 생김.
    - 변수를 새로 만드는 수 밖에 없음    
- 즉, 일단 만들어 놓으면 수정이 어렵고 메모리 재사용이 불가함.

## 1.3. 파이썬에서의 배열

- 파이썬에서는 리스트(list) 타입

```python
# 1차원 배열
array_1d = [1, 2, 3, 4, 5]

# 2차원 배열
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(array_1d)
print(array_2d)
```
```pure_text
    [1, 2, 3, 4, 5]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

```python
### 연습(1)
# 2차원 배열에서 9, 8, 7을 순서대로 출력해보기
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(array_2d[2][2])
print(array_2d[2][1])
print(array_2d[2][0])
```
```pure_text
    9
    8
    7
```

```python
### 연습(2)
# 아래 데이터셋에서 전체 이름 안에서 M은 몇 번 나왔는지 빈도수 출력

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']
```

```python
count = 0
for data in dataset:
    for idx in range(len(data)):
        if data[idx]=='M':
            count += 1
            
print(count)
```
```pure_text
    38
```

* * * 

# 2. 큐 : Queue

## 2.1. 큐의 구조

- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
    - FIFO 또는 LILO 정책을 씀. FIFO를 더 많이 씀.
        - FIFO : First in, First out
        - LILO : Last in, Last out
    
    
## 2.2. 큐와 관련된 용어

- Enqueue: 큐에 데이터를 넣는 기능
- Dequeue: 큐에서 데이터를 꺼내는 기능

## 2.3. 큐가 많이 사용되는 예시

- 재귀 알고리즘 
- 역추적을 해야할 때 (i.e. 문서 작업 시 실행 취소)
- 운영체제 멀티태스킹을 위한 프로세스 스케쥴링을 구현할 때

## 2.4. 큐의 시간 복잡도

- 삽입 / 삭제
    - 원소를 삽입하거나 삭제하는 경우 
        - `O(1)`

## 2.5. 큐의 장단점

장점:
- 데이터의 삽입과 삭제가 빠름

<br>

단점:
- 정책에 따라 가장 위쪽의 원소만 접근 가능함. 
    - i.e. FIFO의 경우 맨 위의 원소만 접근이 가능함.
- 탐색이 상당히 비효율적임. 다 꺼내보면서 탐색해야 함.

## 2.6. 파이썬에서의 Queue

- `queue` 라이브러리를 사용.
    - `Queue()` : 가장 일반적인 큐(FIFO) 자료구조
    - `LifoQueue()` : 나중에 입력된 데이터일 수록 먼저 출력되는 구조 (스택)
    - `PriorityQueue()` : 입력된 데이터마다 우선순위를 설정, 우선순위 순으로 데이터 출력

### 2.6.1. `queue.Queue()` : FIFO

```python
# queue 라이브러리
import queue
```

```python
fifo_queue = queue.Queue()  # FIFO

fifo_queue.put(3) # enqueue
fifo_queue.put(15)
fifo_queue.put(26)
fifo_queue.put(56)

print(fifo_queue.qsize()) # 크키
print(fifo_queue.queue)
```
```pure_text
    4
    deque([3, 15, 26, 56])

```python
fifo_queue.get() # dequeue
```

```pure_text
    3

```python
fifo_queue.get()
```

```pure_text
    15
```

```python
fifo_queue.get()
```

```pure_text
    26
```

```python
fifo_queue.get()
```

```pure_text
    56
```

### 2.6.2. `queue.LifoQueue()` : LIFO (Last in, First out)

```python
lifo_queue = queue.LifoQueue()  # LIFO

lifo_queue.put(3) # enqueue
lifo_queue.put(15)
lifo_queue.put(26)
lifo_queue.put(56)

print(lifo_queue.qsize())
print(lifo_queue.queue)
```

```pure_text
    4
    [3, 15, 26, 56]
```

```python
lifo_queue.get() # dequeue
```

```pure_text
    56
```

```python
lifo_queue.get()
```

```pure_text
    26
```

```python
lifo_queue.get()
```

```pure_text
    15
```

```python
lifo_queue.get()
```

```pure_text
    3
```

### 2.6.3. `queue.PriorityQueue()` : 우선순위에 따라 dequeue

```python
pri_queue = queue.PriorityQueue()

pri_queue.put((34, 'a')) # 튜플 형태로 넣음 (우선순위, 데이터)
pri_queue.put((14, 'b'))
pri_queue.put((72, 'c'))
pri_queue.put((11, 'd'))
pri_queue.put((48, 'e'))

print(pri_queue.qsize()) # size
print(pri_queue.queue) # 숫자가 낮을 수록 우선순위가 높음 (i.e. 1순위, 2순위)
```

```pure_text
    5
    [(11, 'd'), (14, 'b'), (72, 'c'), (34, 'a'), (48, 'e')]
```

```python
pri_queue.get() # dequeue
```

```pure_text
    (11, 'd')
```

```python
pri_queue.get()
```

```pure_text
    (14, 'b')
```

```python
pri_queue.get()
```

```pure_text
    (34, 'a')
```

```python
pri_queue.get()
```

```pure_text
    (48, 'e')
```

```python
pri_queue.get()
```

```pure_text
    (72, 'c')
```


**연습**

`queue`라이브러리가 아닌, 파이썬의 리스트를 가지고 enqueue, dequeue 구현해본다.

```python
class queue_list:
    
    def __init__(self):
        
        self.queue = list()
        
    def __size__(self):
        return len(self.queue)
        
    def __items__(self):
        return self.queue
        
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        target_data = self.queue[0]
        del self.queue[0]
        return target_data
```

```python
ls_queue = queue_list()

ls_queue.enqueue(4)
ls_queue.enqueue(9)
ls_queue.enqueue(1)
```

```python
print(ls_queue.__size__())
print(ls_queue.__items__())
```
```pure_text
    3
    [4, 9, 1]
```

```python
ls_queue.dequeue()
```
```pure_text
    4
```

```python
ls_queue.dequeue()
```

```pure_text
    9
```

```python
ls_queue.dequeue()
```

```pure_text
    1
```

* * *

# 3. 스택 : Stack

- 데이터를 제한적으로 넣을 수 있는 구조
    - 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
    
**큐와의 차이점**

- 큐 :  FIFO 정책
- 스택 : LIFO 정책 --> Last in, First out


## 3.1. 스택의 구조

스택은 LIFO, FILO 구조이지만, LIFO, FILO라고 말하기보다는 통상 이러한 구조를 **스택 Stack** 그 자체로 부름.


- 가장 마지막에 넣은 것을 가장 먼저. 가장 먼저 넣은 것을 가장 마지막에.
    - LIFO : 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책.
    - FILO : 처음 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책.
    

## 3.2. 스택 관련 용어

- `push()` : 데이터를 스택에 삽입하는 연산 (넣기)
- `pop()` : 데이터를 스택에서 삭제하는 연산 (꺼내기)|
- `stack underflow` : 비어있는 스택에서 데이터를 꺼내려고 할 때 생기는 오류
- `stack overflow` : 가득 차있는 스택에 데이터를 삽입하려고 할 때 생기는 오류

    
    
## 3.3. 스택의 활용

- 컴퓨터 내부의 프로세스의 함수들이 동작하는 방식에 쓰임
- 실행 취소 : 가장 최근에 했던 작업부터 거슬러 올라가며 취소
- 웹 브라우저 뒤로 가기 기능 : 가장 최근에 봤던 페이지 순으로 거슬러 가며 브라우징

## 3.4. 스택의 구현 방법

1. 배열(array)
    - 장점:
        - 구현이 쉬움
        - 접근이 빠름
    - 단점:
        - 데이터의 최대 개수를 미리 정해야 함.
        - 데이터 삽입/삭제 시 매우 비효율적.
2. 연결리스트(linked list)
    - 장점:
        - 데이터 최대 개수가 정해져 있지 않음.
        - 데이터 삽입 삭제가 용이함.
    - 단점:
        - 데이터 접근이 한번에 가능하지 않음.
        - 따라서 시간이 걸림.

## 3.5. 파이썬에서의 Stack

- 리스트를 통해서 배열(array) 기반의 스택을 구현해볼 수 있음.
    - `.append()` : push
    - `.pop()` : pop

```python
data_stack = list()

data_stack.append(1) # push
data_stack.append(3)

print(data_stack)
```

```pure_text
    [1, 3]
```

```python
data_stack.pop() # pop
```
```pure_text
    3
```

```python
print(data_stack)
```

```pure_text
    [1]
```

# Reference

- Fast Campus 알고리즘 / 기술면접 강의
- [\[자료구조\] 스택(Stack), 큐(Queue), 덱(Deque)](https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue)
