
import time
from datetime import datetime
import sys
import database_connector
import obd_telemetry
import vehicle_sensors
import accelerometer
import gyroscope
import magnetometer
import queries
import IMU
import traceback 

IMU.detectIMU()
if(IMU.BerryIMUversion == 99):
	IMU = None
else:
	IMU.initIMU()

OBD = vehicle_sensors.init_sensors()
database_connection, cursor = database_connector.connect_mariadb()
exception_counter = 0
while True:
	try:
		if(IMU):
			accelerometer_values = accelerometer.get_gforces(IMU)
			gyroscope_values = gyroscope.get_gyroscope_values(IMU)
			magnetometer_values = magnetometer.get_magnetometer_values(IMU)
			#gps_values = imu_gps(IMU)
			gps_values = (1,1)
		if(OBD):
			print('fetching values')
			obd_values = obd_telemetry.get_snapshot(OBD)
			print(obd_values)
		read_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		query = queries.insert_telemetry_data(read_time,
						      accelerometer_values,
						      gyroscope_values,
						      magnetometer_values,
						      gps_values,
						      obd_values)
		cursor.execute(query)
		database_connection.commit()
		time.sleep(1)
	except:
#		exception_counter += 1
#		if(exception_counter <= 10):
#			continue
		traceback.print_exc()
		print(acclerometer_values)
		print(gyroscope_values)
		print(magnetometer_values)
		database_connection.commit()
		database_connection.close()
		sys.exit(1)
