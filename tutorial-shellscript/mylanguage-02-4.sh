#!/bin/bash

# command : sh mylanguage-02-4.sh Korean English "Japanese Chinese" 
## "$@"는 매개변수를 공백을 기준으로 개별의 문자열 별로 인식함

for language in "$@"
do 
    echo "I can speak $language"
done