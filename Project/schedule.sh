#!/bin/sh
#AUTHER: SHUBHAM NAGURE
#PURPOSE: CHECK FILE EXIST AT LOCATION
#RETURN: BOOLEAN VALUE'

checkFile(){
	echo "hello world"
	filename=$(date +"%d%m%y")
	cd /home/shubham/BhavCopy-Report-Analysis/Project/util/data
	if [ -d "$filename" ];then
		echo "file exist"
		retval=0
	else
		echo "File don't exist..."
		retval=1
	fi
}

checkFile
retval=$?
cd ../../

if [ "$retval" == 0 ]
then
	echo "Loding data to REDIS..."
	./insertoRedis.py
	flag=0
else
	echo "PLEASE WAIT.... GETTING FILE FROM BSE SERVER..."
	./getData.py
	echo "File downloaded now inserting to redis"
	./insertoRedis.py
	flag=1
fi

if [ "$flag" == 0 ]
then
	echo "flag is 0 hence only insertion happened"
else
	echo "FLAG is 1 hence extract and insertion both are success !!"
fi

echo "Successully ran $(date)" >> ./log


