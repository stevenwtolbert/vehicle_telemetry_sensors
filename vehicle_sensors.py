import IMU
import obd

def init_sensors():
	try:
		OBD = obd.OBD()
	except:
		OBD = None

	return(OBD)
