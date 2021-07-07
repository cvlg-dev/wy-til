#!/bin/bash
# command : pt01-myshell-05-2.sh Korean English "Japanese Chinese" 

# 위치매개변수 $* : 전체 인자 값(1)
## $*는 매개변수를 모두 개별로 인식함
## 스페이스를 기준으로 문자열을 파라미터로 인식. 큰 따옴표와 상관 없이 동작함


for language in $* 
do 
    echo "I can speak $language"  
done