# -*- coding: utf-8 -*-

import csv
import math



def generateData(num, file_name):
  '''
  Generate Sine wave data.

  Args:
    num: number of data.
    file_name: output csv file name.
  '''

  file_handler = open(file_name, 'w')
  writer = csv.writer(file_handler)
  writer.writerow(['angle', 'sine'])
  writer.writerow(['float', 'float'])
  writer.writerow(['', ''])

  for i in range(num):
    angle = i * math.pi / 50.0
    sine_value = math.sin(angle)
    writer.writerow([angle, sine_value])

  file_handler.close()



if __name__ == '__main__':
  generateData(num=1000, file_name="sine.csv")
