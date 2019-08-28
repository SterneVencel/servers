#!/bin/bash
#coding=utf-8
RUNTIME=$(cd $(dirname $0) && pwd)
CURRENT_FILE=$(date +"%Y-%m-%d-%a")".txt"
> ${RUNTIME}/preferred_stock/${CURRENT_FILE?}
bash ${RUNTIME}/dataFiltration.bash

function preferred_stock() {
    for M in cat `awk '{print $1}' ${RUNTIME}/harden_shares/${CURRENT_FILE?}`
        do
            grep $M ${RUNTIME}/harden_shares/${BENCHMARK_FILE} | awk '{print $0}' >> ${RUNTIME}/preferred_stock/${CURRENT_FILE?}
        done
}

function preferred_stock_for_downside_forecast_algo() {
    awk '{print $1}' ${RUNTIME}/preferred_stock/${CURRENT_FILE?} | sort -u > ${RUNTIME}/preferred_stock_for_downside_forecast_algo/${CURRENT_FILE?}
}


WEEK=$(date +"%a")
if [ ${WEEK} == "Mon" ];then
    #正常时间可用
    BENCHMARK_FILE=$(date +"%Y-%m-%d-%a" --date '3 days ago')".txt"
    #特殊时间可用，有假期
    #BENCHMARK_FILE=$(date +"%Y-%m-%d-%a" --date '6 days ago')".txt"
    preferred_stock
elif [ ${WEEK} == "Sun" ];then
    exit
elif [ ${WEEK} == "Sat" ];then
    #特殊时间可用
    BENCHMARK_FILE=$(date +"%Y-%m-%d-%a" --date '2 days ago')".txt"
    preferred_stock
    exit
else
    #正常可用
    BENCHMARK_FILE=$(date -d 'last-day' +"%Y-%m-%d-%a")".txt"
    #异常可用
    #BENCHMARK_FILE=$(date +"%Y-%m-%d-%a" --date '2 days ago')".txt"
    preferred_stock
fi

function data_demonstration () {
    awk '{print $1" "$2}' ${RUNTIME}/preferred_stock/${CURRENT_FILE?} | sort -u
}
data_demonstration
preferred_stock_for_downside_forecast_algo
