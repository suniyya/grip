#!/bin/bash
SUB="S02"
AFF="L"
## Need to update two parameter initializations above
MASTERDIR="/cygdrive/e/UCBED/Task_Peripheral/simultaneous-emg-ultrasound/USData/${SUB}"
SOURCEDIR="/cygdrive/e/UCBED/Task_Peripheral/simultaneous-emg-ultrasound/subject-data/${SUB}"
GRASPDIR="${SOURCEDIR}/" #Later set up array of hand grasps to get all relevant folders
UNAFF=""
if [ $AFF = "L" ]; then
	UNAFF="R"
else
	UNAFF="L"
fi

BLOCKS=("1A" "1B" "2A" "2B" "3A" "3B" "4A" "4B" "5A" "5B")
#BLOCKS=("1A" "1B")
GRASPLIST=("iflex" "key" "pinch" "point" "power" "rpower" "tripod" "wrist_ext" "wrist_flex" "wrot")
#GRASPLIST=("iflex")
#**********START of grasp for loop for later***********
##GRASP="iflex" #Hand grasp of interest for loop
for GRASP in "${GRASPLIST[@]}"; do
	GRASPbase=$GRASP
	echo $GRASPbase
	basecountUS=0 #Initialize base count for each grasp
	basecountUS2=0
	for bb in "${BLOCKS[@]}"; do
		#echo $UNAFF
		GRASPFOLDER="$GRASPDIR$bb"
		UpdateUS=0
		UpdateUS2=0
		if [ -d "$GRASPFOLDER" ]; then
			echo "${GRASPFOLDER} exists"
			cd $GRASPFOLDER
			for entry in ./"grasp-${GRASPbase}"*;
			do
				if [ -f "$entry" ]; then
					if [[ "$entry" == *"wrist_"* ]]; then
						#IFS0="wrist_" read -ra file_array <<< "$entry"
						part1=$(echo "$entry" | awk -F 'wrist_' '{print $1}')
						part2=$(echo "$entry" | awk -F 'wrist_' '{print $2}')
						#echo $part2
						entryname="${part1}wrist${part2}"
						if [[ "$GRASP" == *"_"* ]]; then
							graspST=$(echo "${GRASP}" | cut -d '_' -f 1)
							graspEND=$(echo "${GRASP}" | cut -d '_' -f 2)
							GRASP="${graspST}${graspEND}"
						fi
					else
						entryname=$entry
					fi
					IFS="_" read -ra my_array <<< "$entryname"
					SIDE="${my_array[0]: -1}"
					cgrasp=$(echo "${my_array[0]}" | cut -d '-' -f 2)
					cgrasp=${cgrasp%?}
					echo $SIDE
					endfile=$(echo "${my_array[5]}" | cut -d '.' -f 1) #end of file extension
					REPN=$(echo "${my_array[1]}" | cut -d '-' -f 2)
					SUF="" #Suffix corresponding to affected vs. unaffected side
					REAL=""
					if [[ $SIDE = $AFF ]]; then
						SUF="US"
						REAL="RW1"
						REPN=$(($REPN+$basecountUS))
						UpdateUS=1
					else
						SUF="US2"
						REAL="RW2"
						REPN=$(($REPN+$basecountUS2))
						UpdateUS2=1
					fi
					if [ $REPN -lt 10 ]; then
						REPN="0$REPN"
					fi
					if [[ $endfile = $SUF ]]; then #Only copying the relevant suffix here
						#echo $endfile
						cp $entry $MASTERDIR/$GRASP/ #copy file to new location
						mv $MASTERDIR/$GRASP/$entry $MASTERDIR/$GRASP/$cgrasp$REPN$endfile.mat
					elif [[ $endfile = "RW" ]]; then
						cp $entry $MASTERDIR/$GRASP/ #copy file to new location
						mv $MASTERDIR/$GRASP/$entry $MASTERDIR/$GRASP/$cgrasp$REPN$REAL.mat
					fi
				fi
			done
		else
			echo "${GRASPFOLDER} does not exist"
		fi
		
		#Update basecountUS
		if [ $UpdateUS -eq 1 ]; then
			basecountUS=$(($basecountUS+5))
		fi
		#Update basecountUS2
		if [ $UpdateUS2 -eq 1 ]; then
			basecountUS2=$(($basecountUS2+5))
		fi
	done
done