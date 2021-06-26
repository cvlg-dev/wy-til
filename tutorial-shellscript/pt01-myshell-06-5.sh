#!/bin/bash

OS_TYPE="ubuntu"

echo ${OS_TYPE:?null or not set}
echo ${OS_TYPE?null or not set}


OS_TYPE=""
echo ${OS_TYPE:?null or not set}
echo ${OS_TYPE?null or not set}