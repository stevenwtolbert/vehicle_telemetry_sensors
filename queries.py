import numpy as np
def insert_telemetry_data(read_time, accelerometer_values, gyroscope_values, magnetometer_values, gps_values, obd_values):
	query = f"""INSERT INTO measurements(
			read_time,
			xG,
			yG,
			zG,
			gyrX,
			gyrY,
			gyrZ,
			magX,
			magY,
			magZ,
			longitude,
			latitude,
			speed,
			rpm,
			engine_load,
			absolute_throttle_position,
			relative_throttle_position,
			throttle_pos_b,
			accelerator_pos_d,
			accelerator_pos_e,
			fuel_level)
			VALUES(
			'{read_time}',
			'{np.round(accelerometer_values[0],3)}',
			'{np.round(accelerometer_values[1],3)}',
			'{np.round(accelerometer_values[2],3)}',
			'{gyroscope_values[0]}',
			'{gyroscope_values[1]}',
			'{gyroscope_values[2]}',
			'{magnetometer_values[0]}',
			'{magnetometer_values[1]}',
			'{magnetometer_values[2]}',
			'{gps_values[0]}',
			'{gps_values[1]}',
			'{np.round(obd_values[0],3)}',
			'{np.round(obd_values[1],3)}',
			'{np.round(obd_values[2],3)}',
			'{np.round(obd_values[3],3)}',
			'{np.round(obd_values[4],3)}',
			'{np.round(obd_values[5],3)}',
			'{np.round(obd_values[6],3)}',
			'{np.round(obd_values[7],3)}',
			'{np.round(obd_values[8],3)}')
			"""
	return query