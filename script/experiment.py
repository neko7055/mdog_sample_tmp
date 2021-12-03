# coding: utf-8
## @package faboMPU9250
#  This is a library for the FaBo 9AXIS I2C Brick.
#
#  http://fabo.io/202.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

from mpu9250 import MPU9250
import time
import sys
import numpy as np

mpu9250 = MPU9250(0x68)

acc_sample = []

gyro_sample = []

mag_sample = []
# 720000
try:
	for i in range(720000):
		accel = mpu9250.readAccel()
		gyro = mpu9250.readGyro()
		mag = mpu9250.readMagnet()
		acc_sample.append([accel['x'], accel['y'], accel['z']])
		gyro_sample.append([gyro['x'],gyro['y'],gyro['z']])
		mag_sample.append([mag['x'],mag['y'],mag['z']])
		time.sleep(0.01)
	acc_sample = np.array(acc_sample).T
	gyro_sample = np.array(gyro_sample).T
	mag_sample = np.array(mag_sample).T
	print "acc_cov :"
	print np.cov(acc_sample, ddof=1)
	print "gyro_cov :"
	print np.cov(gyro_sample, ddof=1)
	print "mag_cov :"
	print np.cov(mag_sample, ddof=1)
		
except KeyboardInterrupt:
    sys.exit()

