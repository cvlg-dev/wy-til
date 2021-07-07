#!/bin/bash
# command : sh pt01-myshell-05-4.sh Korean English "Japanese Chinese" 

# 위치매개변수 "$*"
## 매개변수 전체를 하나의 문자열로 인식
## 쌍따옴표로 감싼 "$*"는 매개변수를 그냥 하나의 문자열로 인식함


for language in "$*"  
do 
    echo "I can speak $language"
done