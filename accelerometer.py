def get_gforces(IMU):
	ACCx = IMU.readACCx()
	ACCy = IMU.readACCy()
	ACCz = IMU.readACCz()
	xG = (ACCx * 0.244)/1000
	yG = (ACCy * 0.244)/1000
	zG = (ACCz * 0.244)/1000
	return(xG, yG, zG)
