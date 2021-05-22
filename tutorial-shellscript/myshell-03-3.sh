#!/bin/bash

language="German"

function learn() {
    local learn_language="French"
    echo "I am learning $learn_language"
}

function print() {
    echo "I can speak $1"
}

learn
print $language
print $learn_language