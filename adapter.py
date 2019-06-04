""" This program communicates with the OBD adapter present on the vehicle.
    # Add more documentation here.
"""

__author__ = "Dhruv Kool Rajamani"
__email__ = "dhruvkoolrajamani@gmail.com"
__copyright__ = "Copyright 2019, The VDAQ Project"
__date__ = "17 May 2019"

import obd
import numpy as np

obd.logger.setLevel(obd.logging.DEBUG)

ports = obd.scan_serial()  # return list of valid USB or RF ports

if len(ports) == 0:
	is_bluetooth_paired = False
else:
	is_bluetooth_paired = True

if is_bluetooth_paired:
	print("{} Port found, connecting to OBD Port ...".format(ports[0]))
	connection = obd.OBD(portstr=ports[0], baudrate=9600)
else:
	print("No port available on the Bluetooth Port")