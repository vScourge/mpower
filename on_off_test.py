"""
THIS IS OLD - See mpower.py instead!

192.168.1.29
ubnt
ubnt

http://curl.trillworks.com/
"""

import json
import pprint
import requests
import time


cookies = {
    'AIROS_SESSIONID': '12345678901234567890123456789012',
}

def login( ):
    data = [
        ('username', 'ubnt'),
        ('password', 'ubnt'),
    ]
    
    requests.post( 'http://192.168.1.29/login.cgi', cookies = cookies, data = data )    
    
def logout( ):
    requests.post( 'http://192.168.1.29/logout.cgi', cookies = cookies )    

def get_power( ):
    result = requests.get( 'http://192.168.1.29/sensors', cookies = cookies )    
    return json.loads( result.text )


## MAIN ##

if __name__ == '__main__':
    print( 'logging in...' )
    login( )
    
    #pprint.pprint( get_power( ) )
    
    for i in range( 5 ):
        print( 'turn OFF' )
        requests.post( 'http://192.168.1.29/sensors/5', cookies = cookies, data = [ ( 'output', '0' ) ] )
        time.sleep( 1 )
        print( 'turn ON' )
        requests.post( 'http://192.168.1.29/sensors/5', cookies = cookies, data = [ ( 'output', '1' ) ] )
        time.sleep( 1 )
        
    print( 'logging out...' )
    logout( )