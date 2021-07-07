#!/bin/bash

OS_TYPE="Redhat Ubuntu Fedora Debian"

echo ${OS_TYPE:14}            # 문자열 14번째부터 끝까지
echo ${OS_TYPE:14:6}        # 문자열 14번째부터 끝까지
echo ${OS_TYPE:(-6)}         # 문자열 끝에서부터 6번째 전 글자부터 문자열 끝까지 출력
echo ${OS_TYPE:(-6):2}     # 문자열 끝에서부터 6번째 전 글자부터 2글자를 출력
echo ${OS_TYPE:(-6):-2}   # 문자열 끝에서부터 6번째 전 글자부터 끄까지의 길이 중 2를 뺀 나머지 길이만큼 출력