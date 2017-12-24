# -*- coding: utf-8 -*-

import csv
import math

ROWS = 1000

def run(filename="sine.csv"):
	fileHandle = open(filename, 'w')
	writer = csv.writer(fileHandle)
	writer.writerow(['angle', 'sine'])
	writer.writerow(['float', 'float'])
	writer.writerow(['', ''])

	for i in range(ROWS):
		angle = (i * math.pi) / 50.0
		sine_value = math.sin(angle)
		writer.writerow([angle, sine_value])

	fileHandle.close()

if __name__ == '__main__':
	run()
