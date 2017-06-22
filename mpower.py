"""
Test script for Ubiquiti MPower strip.  Tested with Python 3.6

Strip has been pre-configured for the local wifi network,
and set to IP 192.168.1.29

The login & pass are set to "ubnt", "ubnt"

Adam Pletcher, adam.pletcher@gmail.com
"""

import json
import pprint
import requests
import time


class MPower( ):
	"""
	Simple class for managing MPower devices.
	
	Adam Pletcher, adam.pletcher@gmail.com
	"""
	def __init__( self, ip_address, login_name, login_password ):
		self.ip_address = ip_address
		self.login_name = login_name
		self.login_password = login_password

		self.cookies = {
		   # Create 32 character session ID based on IP address. Can be any string.
			'AIROS_SESSIONID': ( self.ip_address.replace( '.', '' ) * 4 )[ :32 ],
		}


	def login( self ):
		data = [
			( 'username', self.login_name ),
			( 'password', self.login_password ),
		]

		result = requests.post( 'http://{ip_address}/login.cgi'.format( ip_address = self.ip_address ), cookies = self.cookies, data = data )

		return result


	def logout( self ):
		result = requests.post( 'http://{ip_address}/logout.cgi', cookies = self.cookies )

		return result


	def get_sensor_data( self ):
		result = requests.get( 'http://{ip_address}/sensors', cookies = self.cookies )

		return json.loads( result.text )


	def set_port_output( self, port, state ):
		data = [
			( 'output', str( int( state ) ) ),
		]

		result = requests.post( 'http://{ip_address}/sensors/{port}'.format( ip_address = self.ip_address, port = port ), cookies = self.cookies, data = data )

		return result



## MAIN ##

if __name__ == '__main__':
	mpower1 = MPower( '192.168.1.29', 'ubnt', 'ubnt' )

	print( 'logging in...' )
	mpower1.login( )

	for i in range( 5 ):
		print( 'turn OFF' )
		mpower1.set_port_output( 5, False )
		time.sleep( 1 )

		print( 'turn ON' )
		mpower1.set_port_output( 5, True )
		time.sleep( 1 )

	mpower1.logout( )