#!/bin/bash
# command : sh pt01-myshell-05-5.sh Korean English "Japanese Chinese" 

# 위치매개변수 "$@"
## 쌍따옴표로 감싼 "$@"는 매개변수를 공백을 기준으로 개별의 문자열 별로 인식함
## 단, 따옴표 내의 매개변수를 하나의 문자열로 인식

for language in "$@"  
do 
    echo "I can speak $language"  
done