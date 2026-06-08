#!/bin/bash
SUB="S02"
MASTERDIR="../USDATA/${SUB}"
MSG="Directory already exists."
echo $MASTERDIR
if [ -d "$MASTERDIR" ]; then
	echo "Directory already exists."
else
	echo "Directory does not exist. Creating folder."
	mkdir $MASTERDIR
	cd $MASTERDIR
	MV1="power"
	mkdir $MV1
	MV2="rpower"
	mkdir $MV2
	MV3="tripod"
	mkdir $MV3
	MV4="wrot"
	mkdir $MV4
	MV5="iflex"
	mkdir $MV5
	MV6="key"
	mkdir $MV6
	MV7="pinch"
	mkdir $MV7
	MV8="wristext"
	mkdir $MV8
	MV9="wristflex"
	mkdir $MV9
	MV10="point"
	mkdir $MV10
fi
