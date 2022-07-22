def get_gyroscope_values(IMU):
	gyrX = IMU.readGYRx()
	gyrY = IMU.readGYRy()
	gyrZ = IMU.readGYRz()
	return(gyrX, gyrY, gyrZ)
