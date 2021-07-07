#!/bin/bash
# command : pt01-myshell-05-3.sh Korean English "Japanese Chinese" 

# 위치매개변수 $@ : 전체 인자 값(2)
## $@는 매개변수를 모두 개별로 인식함
## `$*`와 동일


for language in $@
do 
    echo "I can speak $language"   
done