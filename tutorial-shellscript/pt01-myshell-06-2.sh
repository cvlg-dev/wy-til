#!/bin/bash


OS_TYPE="ubuntu"
echo ${OS_TYPE:-redhat}
echo ${OS_TYPE-redhat}

unset OS_TYPE
echo ${OS_TYPE:-redhat}
echo ${OS_TYPE-redhat}

OS_TYPE=""
echo ${OS_TYPE:-redhat}
echo ${OS_TYPE-redhat}