#!/bin/bash

OS_TYPE=""

echo ${OS_TYPE:-redhat}
echo $OS_TYPE

echo ${OS_TYPE:=redhat}
echo $OS_TYPE