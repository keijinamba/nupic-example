#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import time
import csv
import poloniex

polo = poloniex.Poloniex()

DATA_PAIR   = 'USDT_BTC'
DATA_PERIOD = polo.DAY
DATA_SPAN   = 1000


def getChartData(pair = DATA_PAIR, period = DATA_PERIOD, span = DATA_SPAN):
  '''
  Get (Bitcoin) prices by Poloniex API.

  Args:
    period: data interval.
    span: number of days to get.
  Return:
    (Bitcoin) prices data.
  '''

  return polo.returnChartData(pair,
    period = period,
    start  = time.time() - polo.DAY * span,
    end    = time.time()
  )


def saveDataToCSV(file_name):
  '''
  Save prices data to the csv file.

  Args:
    file_name: a file name.
  '''
  
  chart = getChartData()
  fileHandler = open(file_name, "w")
  writer = csv.writer(fileHandler)
  writer.writerow(["date", "price"])
  writer.writerow(["int", "float"])
  writer.writerow(["", ""])

  for data in chart:
      writer.writerow([data['date'], data['close']])

  fileHandler.close()



if __name__ == "__main__":
  # data = getChartData()
  saveDataToCSV("chart.data.csv")

