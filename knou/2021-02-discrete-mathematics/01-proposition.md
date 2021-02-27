# 1. 명제

명제: 참과 거짓을 구별할 수 있는 문장이나 수학적 식

## 1.1. 명제의 진리값

- 참 / True / T : 명제가 타당한 경우
- 거짓 / False / F : 명제가 타당하지 않은 경우

## 1.2. 명제의 종류

- 합성명제
- 조건명제, 쌍조건명제
- 항진명제, 모순명제

## 1.3. 명제의 예

- 다음 문장이 명제인지 아닌지 구분하시오

  1. 6은 2의 배수다 -> 명제. 진리값이 T
  2. 철수는 공부를 잘 한다 -> 명제가 아님
  3. 2+3 = 7 -> 명제. 진리값이 F
  4. x+2 = 0 -> 
     - 명제가 아님. 
     - x의 값에 따라서 참일 수도 있고 거짓일 수도 있음.
     - 명제함수라고 한다.

  

- 다음 명제의 진리값을 구하여라

  1. 2, 3, 6는 소수(prime number)이다 -> F
  2. 소수의 개수는 무한하다 -> T
  3. 126 = 2^6 -> F
     - 2^6 = 2^3 * 2^3 = 64
     - 126 = 2^7
  4. 지구에서 가장 높은 산은 에베레스트이다 -> T





# 2. 논리연산

## 2.1. 논리연산자 operation, operator

### 2.1.1. 논리상수, 논리변수

- 논리상수
  - T/F 는 논리상수라고 함
- 논리변수
  - p, q 등으로 불리는 명제를 논리변수라고 함
- 합성명제
  - 하나이상의 논리변수(명제), 논리상수(T/F)를 논리연산자와 괄호로 묶은 논리연산식

### 2.1.2. 논리연산

- 논리연산자
  - OR
  - AND
  - NOT
  - XOR

### 2.1.3. 기본 논리연산

1. 논리합 (disjunction; OR, $\vee$)

   - p OR q	
   - 진리표

   |  p   |  q   | p OR q |
   | :--: | :--: | :----: |
   |  T   |  T   |   T    |
   |  T   |  F   |   T    |
   |  F   |  T   |   T    |
   |  F   |  F   |   F    |

2. 논리곱 (conjunction; AND, $\wedge$)

   - p AND q

   - 진리표

     |  p   |  q   | p AND q |
     | :--: | :--: | :-----: |
     |  T   |  T   |    T    |
     |  T   |  F   |    F    |
     |  F   |  T   |    F    |
     |  F   |  F   |    F    |

3. 부정 (negation: NOT, $~$)

	- NOT p

     - 대표적인 1항연산

   - 진리표

     |  p   |  ~p  |
     | :--: | :--: |
     |  T   |  F   |
     |  F   |  T   |

4. 배타적 논리합 (exclusive conjunction: XOR, $\oplus$)

   - p XOR q = (p AND NOT q) OR (NOT p AND q)
   
   - p $oplus$ q = (p $\wedge ~$ q) $\vee$ ($~$ p $\wedge$ q)
   
   - 둘 중 하나는 거짓이어야 함. 
   	
   	|  p   |  q   | p AND NOT q | NOT p AND q | (p AND NOT q) OR (NOT p AND q) | p XOR q |
   	| :--: | :--: | :---------: | :---------: | :----------------------------: | :-----: |
   	|  T   |  T   |      F      |      F      |               F                |    F    |
   	|  T   |  F   |      T      |      F      |               T                |    T    |
   	|  F   |  T   |      F      |      T      |               T                |    T    |
   	|  F   |  F   |      F      |      F      |               F                |    F    |





## 2.2. 조건명제 

### 2.2.1. 조건명제 (conditional proposition; ->)

- 명제 p와 q가 있을 때, 
  - 명제 p가 조건의 역할을 수행하고 
  - 명제 q가 결론의 역할을 수행하는 경우

- p -> q ( p => q)
  - p는 q의 충분조건
  - q는 p의 필요조건

- 진리표

  |  p   |  q   | p -> q |
  | :--: | :--: | :----: |
  |  T   |  T   |   T    |
  |  T   |  F   |   F    |
  |  F   |  T   |   T    |
  |  F   |  F   |   T    |



### 2.2.2. 쌍조건명제 (conditional proposition, <->)

- 명제 p와 q가 있을 때, 

  - 명제 p와 q가 조건의 역할과 결론의 역할을 동시에 수행하는 경우

- p <-> q

  - (p -> q) AND (q -> p)

- 진리표

  |  p   |  q   | p -> q | q -> p | p <-> q |
  | :--: | :--: | :----: | :----: | :-----: |
  |  T   |  T   |   T    |   T    |    T    |
  |  T   |  F   |   F    |   T    |    F    |
  |  F   |  T   |   T    |   F    |    F    |
  |  F   |  F   |   T    |   T    |    T    |

- 쌍조건명제는 NOT XOR의 동치이다.



## 2.3. 동치

### 2.3.1. 논리적 동치 (logical equivalent, $equiv$)

- 두 명제 p와 q가 논리적으로 동등하면, 
  - 논리적 동치라고 하고, p $\equiv$ q로 표시함
  - 논리적으로 동등하다는 말은 두 명제가 항상 동일한 진리값을 가진다는 의미

### 2.3.2. 역, 이, 대우

- 조건명제 p -> q

  - 역 (converse) : q -> p
  - 이 (inverse) : ~p -> ~q
  - 대우 (contrapositive) : ~q -> ~p

  ![](https://i.ibb.co/TkXF3qt/Screen-Shot-2021-02-27-at-2-49-02-PM.png)



### 2.3.3. 논리적 동치 법칙

논리적 동치를 활용하면, 어려운 명제를 의미가 동일한 더 쉬운 명제로 바꾸는 사고를 할 수 있음. 

1. 교환법칙 (commutation law)

   - p OR q  $\equiv$  q OR p
   - p AND q  $\equiv$  q AMD p
   - p <-> q  $\equiv$  q <-> p

2. 결합법칙 (associative law)

   - (p OR q) OR r  $\equiv$  p OR (q OR r)
   - (p AND q) AND r  $\equiv$  p AND (q AND r)

3. 분배법칙 (distributive law)

   - p OR (q AND r)  $\equiv$  (p OR q) AND (p OR r)
   - p AND (q OR r)  $\equiv$  (p AND q) OR (p AND r)

4. 항등법칙 (identity law)

   - p OR F  $\equiv$  p

     |  p   | p OR f |
     | :--: | :----: |
     |  T   |   T    |
     |  F   |   F    |

   - p AND T $\equiv$  p 

	   |  p   | p OR f |
	   | :--: | :----: |
	   |  T   |   T    |
	   |  F   |   F    |

5. 지배법칙 (domination law)
   - p OR T  $\equiv$  T
   - p AND F  $\equiv$  F
6. 부정법칙 (negation law)
   - ~ T  $\equiv$  F
   - ~ F  $\equiv$  T
   - p OR (~ p)  $\equiv$  T
   - p AND (~p)   $\equiv$  F
7. 이중 부정 법칙 (double negation law)
   
   - ~ (~ p)  $\equiv$  p
8. 멱등법칙 (indempotent law)
   - p OR p  $\equiv$  p
   - p AND p  $\equiv$  p
9. 드 모르간 법칙 (de Morgan's law)
   - ~ (p OR q)  $\equiv$  (~p) AND (~q)
   - ~ (p AND q)  $\equiv$  (~p) OR (~q)
   - 예제) 드모르간 법칙을 사용하여 다음 식의 부정을 나타내시오 
     - -2 < x < 3
       - ~ (-2 < x < 3) == ~( (-2 < x) AND ~(x < 3) )
       - (~(-2 < x)) OR (~(x<3))
       - (x <= -2) OR (x >= 3)
10. 흡수법칙 (absorption law)
    - p OR (p AND q)  $\equiv$  p
    - p AND (p OR q)  $\equiv$  p
11. 함축법칙 (implication law)
    
    - p -> q  $\equiv$  ~ p OR q    (조건명제를 달리 표현하면 오른쪽과 같이 표현될 수 있다.)
12. 대우법칙
    
    - p -> q  $\equiv$  ~q -> ~p 



### 2.3.4. 항진명제 & 모순명제 

- 항진명제 (tautology)
  - 합성명제를 구성하는 명제의 진리값과 상관 없이 항상 참(T)인 명제
  - 예) p OR T

- 모순명제 (contradiction)
  - 합성명제를 굿어하는 명제의 진리값과 상관 없이 항상 거짓(F)인 명제
  - 예) p AND F

# 3. 술어논리

## 3.1. 술어논리 & 명제함수

- 논리
  - 명제논리 (proposition) : 명제
  - 술어논리 (predicate logic) : 명제함수

### 3.1.1. 명제함수

- 변수의 값에 의해 함수의 진리값이 결정되는 문장이나 식
- 변수의 경우
  - 변수의 값을 적시 (변수가 무엇인지 알려줌)
  - 변수의 범위를 제시 (기호를 사용하여 한정화)
    - 한정화 quantification 
      - 전체한정자 (universal quantifier, $\forall$)
        - arbitrary, for all ... , "모든", "임의의"
        - $\forall$x P(x)와 같이 사용될 경우, 
          - 정의역의 모든 [임의의] x에 대해서 P(x)가 참임을 의미함.
      - 존재한정자 (existential quantifier, $\exists$)
        - exists, there exists ... , "존재한다"
        - $\exists$x P(x)와 같이 사용될 경우,
          - 정의역의 어떤 x에 대해서 P(x)가 참(T)임을 의미함.
          - there exists x such that P(x) is true

## 3.2. 타당성 검사

### 3.2.1. 명제함수의 타당성

- 벤다이어그램 (Venn diagram)
  - 한정자가 사용된 명제함수의 타당성을 직관적으로 검사할 수 있음. 

# 4. 추론

참으로 알려진 며엦를 기초로 하여 다른 명제를 유도해 내는 과정을 추론이라고 함.

- 결론의 근거를 제공하는 알려진 명제를 전제(premise)라고 함.
- 새로 유도된 명제는 결론(conclusion)

## 4.1. 유효추론

- 유효추론
  - 전제를 참(T)이라고 가정하였을 때 결론이 항상 참(T)이 되는 추론
  - 예 : ((p -> q) AND (q -> r)) -> (p -> r)

- 추론규칙
  - 기본적인 추론규칙은 논리적 동치(항진명제)를 이용함. (언제나 참인 명제)
  - 추론 법칙
    - 선언적 부가 (disjunctive addition)
    - 단순화 (simplication)
    - 긍정논법 (modus ponens)
    - 부정논법 (modus tollens)
    - 선언적 삼단논법 또는 소거 (disjunctive syllogism)
    - 가설적 삼단논법 또는 추이 (hypothetical syllogism)