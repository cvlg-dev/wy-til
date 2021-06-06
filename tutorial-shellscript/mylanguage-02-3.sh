#!/bin/bash

# command : sh mylanguage-02-3.sh Korean English "Japanese Chinese" 
## "$*"는 매개변수를 그냥 하나의 문자열로 인식함

for language in "$*"
do 
    echo "I can speak $language"
done