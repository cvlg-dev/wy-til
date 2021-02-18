# 1. 해쉬 테이블 (Hash Table)

## 1.1. 해쉬 테이블의 구조

- 키(Key)에 데이터(Value)가 매핑되어 저장되어 있는 구조
    - Key를 통해 데이터를 바로 받아올 수 있으므로, 속도가 빠름
    - 파이썬에서는 딕셔너리(Dictionary)가 해쉬 테이블의 예시.
    
    ```python
    dict = {"key": "value"}
    ```

## 1.2. 해쉬 테이블의 용어

- 해쉬(Hash)
    - 임의의 값을 고정된 길이로 변환하는 것
- 해쉬 테이블(Hash Table)
    - Key값의 연산에 의해 직접 접근이 가능한 데이터 구조
- 해싱 함수(Hashing Function)
    - Key에 대해 특정 산술 연산을 이용하여 데이터의 위치(해쉬 주소)가 리턴되는 함수
- 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address)
    - Key를 해싱 함수로 연산하여 얻는 값
    - Key를 해싱 함수로 연산하여 해쉬 값이 데이터의 위치.
- 슬롯(Slot)
    - 한 개의 데이터를 저장할 수 있는 공간
    
    
## 1.3. 해시테이블의 장단점

- 장점
    - 데이터 저장/읽기 속도가 빠름
    - 특히 검색 속도가 빠름
    - Key에 대한 데이터가 있는지 확인이 쉬움. 
    - 중복 처리 및 확인이 쉬움
- 단점
    - 일반적으로 저장공간이 많이 요구됨. 공간효윬어이 떨어짐.
        - 해시함수에 따른 값이 저장될 공간이 확보되어야 하기 때문
    - 해싱 함수로 인해 연산된 해시값/해시주소가 동일한 경우 충돌을 해결해야 함.
        - 해시함수에 대한 의존도가 높음.
        - 따라서 별도의 자료구조가 요구됨.


## 1.4. 해시테이블의 용도

- 검색이 많이 필요한 경우
- 저장, 삭제, 읽기가 빈번한 경우
- 캐쉬 구현
    - 이미 데이터가 캐시에 있는지 없는지 중복확인을 할 때 해시테이블이 용이하게 적용됨.



# 2. 파이썬을 통한 해쉬함수 이해

## 2.1. Hash Table

### 2.1.1. Slot

```python
hash_table = list([i for i in range(10)])
hash_table
```

```pure_text
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 2.1.2. Hash Function

- 해쉬 함수에는 다양한 기법들이 있음. 
- Division 방식은 가장 기본적인 형태로 알려져 있음.
    - 특정 값으로 나눈 후 나머지 값을 이용하는 기법.

```python
def hash_func(key):
    return key % 5
```

### 2.1.3. 데이터 준비

```python
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'
## ord(): 문자의 ASCII(아스키)코드 리턴
print (ord(data1[0]), ord(data2[0]), ord(data3[0]))
print (ord(data1[0]), hash_func(ord(data1[0])))
print (ord(data1[0]), ord(data4[0]))
```

```pure_text
    65 68 84
    65 0
    65 65
```

### 2.1.4. 데이터 저장

```python
def storage_data(data, value):
    index_key = ord(data[0])
    hash_address = hash_func(index_key)
    hash_table[hash_address] = value
```

```python
storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')
```

```python
print(hash_table)
```

```pure_text
    ['01055553333', 1, 2, '01044443333', '01022223333', 5, 6, 7, 8, 9]
```

### 2.1.4. 데이터 읽기

```python
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]
```

```python
get_data('Andy')
```

```pure_text
    '01055553333'
```



## 3. 파이썬 예시

- 해시함수를 다르게 설정하고 일괄적으로 저장, 추출까지 설정했을 때.
    - 해시함수 : `key % 8`

```python
hash_table = list([0 for i in range(10)])

def hash_function(key):
    return key & 8

def get_key(data):
    return hash(data)

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
```

```python
# 데이터 저장
save_data('Dave', '01020302000')
save_data('Andy', '01033232200')
```

```python
print(hash_table)
```

```pure_text
    ['01033232200', 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

```python
# 데이터 읽기
read_data('Dave')
```

```pure_text
    '01033232200'
```



# 4. 해시 충돌(Hash Collision) 처리를 위한 문제 접근 방법

![](https://i.stack.imgur.com/Hw21c.png#center)

## 4.1. Separate Chaining 방식

- 해시 테이블 저장공간 이외의 공간을 활용함
- 충돌이 일어났을 때, 데이터를 뒤에 추가로 저장.
    - 이 때, 다양한 자료구조를 활용하며 Linked List가 하나의 예가 될 수 있음. (Separate chaining with linked list)

![](https://he-s3.s3.amazonaws.com/media/uploads/0e2c706.png#center)

### 4.1.1. Separate chaining with Linked List

- 데이터 저장 시, 동일한 hash_address가 존재하여 충돌이 발생하면, Linked list에 노드를 추가하여 값을 추가함. (파이썬으로는 일반 리스트로 구현함)
- 데이터 추출 시, hash_address에 대하여 선형 탐색하며, 해당 key에 대한 데이터를 검색 후 결과를 리턴함.

```python
def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    # 이미 Hash table의 공간이 차있어 충돌이 발생할 경우
    if hash_table[hash_address] != 0:  
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
                return None
        hash_table[hash_address].append([index_key, value]) # 새로 추가
        
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]  # value return
        return None
    else:
        return None
    return hash_table[hash_address]
```

```python
hash_table = list([0 for i in range(10)])
```

```python
# pring hashed index_key for each data

print(hash_function(get_key('Dash')))
print(hash_function(get_key('Donald')))

print(hash_function(get_key('Dave')))

print(hash_function(get_key('David')))
print(hash_function(get_key('Dwayne')))
print(hash_function(get_key('Dusan')))

print(hash_function(get_key('Don')))

print(hash_function(get_key('Dean')))
print(hash_function(get_key('Dingo')))

print(hash_function(get_key('Johnson')))
```

```pure_text
    7
    6
    5
    3
    2
    4
    7
    6
    5
    0
```

```python
# index_key = 1
save_data('Dash', '1111111111')
save_data('Donald', '2222222222')

# index_key = 3
save_data('Dave', '3333333333')

# index_key = 4
save_data('David', '4444444444')
save_data('Dwayne', '5555555555')
save_data('Dusan', '6666666666')

# index_key = 5
save_data('Don', '7777777777')

# index_key = 6
save_data('Dean', '8888888888')
save_data('Dingo', '9999999999')

# index_key = 7
save_data('Johnson', '0000000000')
```

```python
print(hash_table)
```

```pure_text
    [[[-2635316466179689368, '0000000000']],
     0,
     [[6215479457786385290, '5555555555']],
     [[-7904014224011995085, '4444444444']],
     [[1661792002016286988, '6666666666']],
     [[-7424204428908836315, '3333333333'], [2760365508324363629, '9999999999']],
     [[-6894406110985197394, '2222222222'], [-7882665379891136098, '8888888888']],
     [[-8106021915874705937, '1111111111'], [6082400908374278295, '7777777777']],
     0,
     0]
```

```python
read_data('Dusan')
```

```pure_text
    '6666666666'
```

```python
read_data("Dance") # 데이터 존재 하지 않음
```

## 4.2. Open Addressing 방식

- 추가 메모리 공간을 사용하지 않고, 해시 테이블의 빈 공간을 사용하는 방법.
    - Separate chainging에 비해 메모리를 덜 사용함.
    
### 4.2.1. Linear probing

- 충돌이 발생할 시, 해당 hash_address의 다음 hash_address부터 가장 먼저 등장하는 빈 공간에 저장하는 기법
- 장점
    - 저장공간 활용도를 높일 수 있음.
    - 저장 시 별도의 별도의 공간이나 추가 작업이 필요 없음.
- 단점
    - 해시 함수의 퍼포먼스에 따라 해시테이블의 성능이 결정됨.
    - 대신 빈 공간을 미리 확보하기 위해 해시 테이블 저장공간을 다시 확대하거나 미리 마련이 되어 있어야 함..

```python
def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    # 이미 Hash table의 공간이 차있어 충돌이 발생할 경우
    if hash_table[hash_address] != 0:
        
        for index in range(hash_address, len(hash_table)): 
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
            
    else:
        hash_table[hash_address] = [index_key, value]
        
        
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        None
```

```python
hash_table = list([0 for i in range(12)])
```

```python
# index_key = 1
save_data('Dash', '1111111111')
save_data('Donald', '2222222222')

# index_key = 3
save_data('Dave', '3333333333')

# index_key = 4
save_data('David', '4444444444')
save_data('Dwayne', '5555555555')
save_data('Dusan', '6666666666')

# index_key = 5
save_data('Don', '7777777777')

# index_key = 6
save_data('Dean', '8888888888')
save_data('Dingo', '9999999999')

# index_key = 7
save_data('Johnson', '0000000000')
```

```python
print(hash_table)
```

```pure_text
    [[-2635316466179689368, '0000000000'],
     0,
     [6215479457786385290, '5555555555'],
     [-7904014224011995085, '4444444444'],
     [1661792002016286988, '6666666666'],
     [-7424204428908836315, '3333333333'],
     [-6894406110985197394, '2222222222'],
     [-8106021915874705937, '1111111111'],
     [6082400908374278295, '7777777777'],
     [-7882665379891136098, '8888888888'],
     [2760365508324363629, '9999999999'],
     0]
```



## 5. Hash 함수와 Key 생성

### 5.1. 대표적인 해시 함수들

- SHA (Secure Hash Algorithm)
    - 어떠한 데이터도 고정된 크기의 unique한 값으로 리턴하므로, 해시 함수로 유용하게 활용 가능
    - 해시함수들의 모음이기에, 여러가지 함수를 선택할 수 있음.

```python
import hashlib
```

```python
# SHA-1를 사용한 예시
data = 'David'.encode()
hash_object = hashlib.sha1() 
hash_object.update(data)
hash_address = hash_object.hexdigest()
print(hash_address)
```

```pure_text
    d27937f914ebe99ee315f04449678eccfb658191
```

```python
# SHA-256을 사용한 예시
data = 'David'.encode()
hash_object = hashlib.sha256() 
hash_object.update(data)
hash_address = hash_object.hexdigest()
print(hash_address)
```

```pure_text
    a6b54c20a7b96eeac1a911e6da3124a560fe6dc042ebf270e3676e7095b95652
```

## 5.2. SHA-256 알고리즘을 사용한 Linear Probing 방식구현

```python
import hashlib

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hash_address = hash_object.hexdigest()
    return int(hash_address, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    # 이미 Hash table의 공간이 차있어 충돌이 발생할 경우
    if hash_table[hash_address] != 0:
        
        for index in range(hash_address, len(hash_table)): 
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
            
    else:
        hash_table[hash_address] = [index_key, value]
        
        
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        None
```

```python
hash_table = list([0 for i in range(12)])

print(hash_function(get_key('Dash')))
print(hash_function(get_key('Donald')))
print(hash_function(get_key('Dave')))
print(hash_function(get_key('David')))
print(hash_function(get_key('Dwayne')))
print(hash_function(get_key('Dusan')))
print(hash_function(get_key('Don')))
print(hash_function(get_key('Dean')))
print(hash_function(get_key('Dingo')))
print(hash_function(get_key('Johnson')))
```

```pure_text
    3
    6
    0
    2
    2
    5
    5
    4
    6
    6
```

```python
save_data('Dash', '1111111111')
save_data('Donald', '2222222222')
save_data('Dave', '3333333333')
save_data('David', '4444444444')
save_data('Dwayne', '5555555555')
save_data('Dusan', '6666666666')
save_data('Don', '7777777777')
save_data('Dean', '8888888888')
save_data('Dingo', '9999999999')
save_data('Johnson', '0000000000')
```

```python
print(hash_table)
```

```pure_text
    [[58168926492874022204843410240616221587430711422315320988033179720499944676464,
      '3333333333'],
     0,
     [75404257596651192996495076349601554552549513252973852817536161452854420788818,
      '4444444444'],
     [63434467723890717949172920093925024550717963975746208715791640357658818776859,
      '1111111111'],
     [103158016914344531977983463060013032302915828748947913551605310269665217945786,
      '5555555555'],
     [90558914996105951668787733552590627218772546758158603367772415150980389476661,
      '6666666666'],
     [40513459897764969709188365008375736156728765495033312981181177193702355922238,
      '2222222222'],
     [16606146580844896176716406780736496581454102609573324990177790343105877227493,
      '7777777777'],
     [88623518743408414412271740834380503561141448764593279404613947210397492361580,
      '8888888888'],
     [22241017530888154973558349121945220497843199841401728659273049527650898379222,
      '9999999999'],
     [21745812297715092507978491799105903853662369235937786557584049993744107100774,
      '0000000000'],
     0]
```

```python
read_data('Dingo')
```

```pure_text
    '9999999999'
```



# 6. 시간 복잡도

- 저장 (insertion), 삭제 (deletion), 검색(search)
    - Collision이 없는 경우: O(1)
    - Collision이 모두 발생하는 최악의 경우: O(n)

> 해쉬 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에, 시간 복잡도는 O(1) 이라고 말할 수 있음

# 7. Reference


[Hash Table Wikipedia](https://en.wikipedia.org/wiki/Hash_table#Open_addressing)
