# credits go to https://pyftpdlib.readthedocs.io/en/latest/tutorial.html atm...

import os
import sys
import logging
from hashlib import md5
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed

# creation of the dummy authorizer to be formatted with md5 so the password is not exposed in case if
# someone is listening

class DummyMD5Authorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        if sys.version_info >= (3, 0):
            password = md5(password.encode('latin1'))
        hash = md5(password).hexdigest()
        try:
            if self.user_table[username]['pwd'] != hash:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed

try:
    # Generating a hash of the password
    hash = md5('9lGi^W0rjlJ5Ve'.encode('utf-8')).hexdigest()

    # Instantiate an md5 dummy authorizer for managing 'virtual' users
    authorizer = DummyMD5Authorizer()

    # Define a new user having only write and make directory permissions
    # adding a user that can only make a directory and write to the directories that it creates
    authorizer.add_user("logger", hash, str(os.getcwd()), perm="mw")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready.\nConnected!"

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 10
    server.max_cons_per_ip = 1

    # adding a logging location for all logs to be stored
    logging.basicConfig(filename='/var/log/pyftpd.log', level=logging.INFO)

    print('FTP Server Started\n\n')

    # start ftp server
    server.serve_forever()
except:
    print('server is closed now...')