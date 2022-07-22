import obd
def get_snapshot(connection):
	speed = connection.query(obd.commands.SPEED).value.magnitude
	rpm = connection.query(obd.commands.RPM).value.magnitude
	engine_load = connection.query(obd.commands.ENGINE_LOAD).value.magnitude
	absolute_throttle_position = connection.query(obd.commands.THROTTLE_POS).value.magnitude
	relative_throttle_position = connection.query(obd.commands.RELATIVE_THROTTLE_POS).value.magnitude
	throttle_pos_b = connection.query(obd.commands.THROTTLE_POS_B).value.magnitude
	accelerator_pos_d = connection.query(obd.commands.ACCELERATOR_POS_D).value.magnitude
	accelerator_pos_e = connection.query(obd.commands.ACCELERATOR_POS_E).value.magnitude
	fuel_level = connection.query(obd.commands.FUEL_LEVEL).value.magnitude

	values = (speed,
	            rpm,
	            engine_load,
	            absolute_throttle_position,
	            relative_throttle_position,
	            throttle_pos_b,
	            accelerator_pos_d,
	            accelerator_pos_e,
	            fuel_level)
	return values
