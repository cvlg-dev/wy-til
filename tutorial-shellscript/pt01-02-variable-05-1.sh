#!/bin/bash
# 위치매개변수

# command : pt01-myshell-05-1.sh Korean English

# 실행된 스크립트 이름
echo "This shell script name is $0"  

# 파라미터 순서대로 
echo "I can speak $1 and $2"

# 전체 인자 값 (1)
echo "This shell script parameters are $*"

# 전체 인자 값 (2)
echo "This shell script parameters are $@"

# 매개변수의 총 개수
echo "This parameter count is $#"