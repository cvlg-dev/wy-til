#!/bin/bash
# 함수 밖에서 선언된 전역변수 출력

language="English"

function print() {
    echo "I can speak $language"
}

print