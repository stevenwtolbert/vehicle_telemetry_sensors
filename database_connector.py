import mariadb
import sys

def connect_mariadb():
	try:
		conn = mariadb.connect(
			user = "pi",
			password = "root",
			host = "localhost",
			port = 3306,
			database = "vehicle_telemetry"
			)
	except mariadb.Error as e:
		print(f"Error Connecting to MariaDB Platform: {e} ")
		return None
	cur = conn.cursor()

	return(conn, cur)


