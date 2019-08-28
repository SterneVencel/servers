#!/bin/sh
RUNTIME=$(cd $(dirname $0) && pwd)
DATE=$(date +"%Y-%m-%d-%a")
#DATE=$(date -d yesterday +"%Y-%m-%d-%a")
RZ_DIR=${RUNTIME}"/rz_file"
INITIALIZE_FILE=${RUNTIME}/initialize_data/${DATE}".txt"
CURRENT_FILE=${RUNTIME}/harden_shares/${DATE}".txt"


function rz_file_rename() {
   mv ${RUNTIME}/tmp ${RZ_DIR}/${DATE}".txt"
   TARGET_FILE=${RZ_DIR}/${DATE}".txt"
   cp ${TARGET_FILE} ${INITIALIZE_FILE?}
}

rz_file_rename
sed -i '/^\s*$/d' ${INITIALIZE_FILE?}

function stock_fulter_rule () {
    awk '{if(NR>2 && $4>0.090 && $3>8.50 && $8>100 && (($12/$3-1)<0.3)) {print $0}}' ${INITIALIZE_FILE?} | sort -t' ' -k4 -r  |  awk '{printf "%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s\n", $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13}' | column -t > harden_shares/${DATE}.txt
    awk '{if((NR>2) && ($12/$11-1)>0.095 && ($4>0.070) && ($4<=0.080)i && ($3>8.50) && $8>100 && (($12/$3-1)<0.3)) {print $0}}' ${INITIALIZE_FILE?} | sort -t' ' -k4 -r  |  awk '{printf "%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s%-13s\n", $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13}' | column -t >> harden_shares/${DATE}.txt   
}
stock_fulter_rule
