def get_magnetometer_values(IMU):
	magX = IMU.readMAGx()
	magY = IMU.readMAGy()
	magZ = IMU.readMAGz()
	return(magX, magY, magZ)
