#!/bin/bash

# command : sh mylanguage-02-2.sh Korean English "Japanese Chinese" 
## $@는 매개변수를 모두 개별로 인식함

for language in $@
do 
    echo "I can speak $language"
done