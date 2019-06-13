user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'bangsat' and user == 'errorsystem':

	print "Kamu Berhasil Login"
	
else:

	print "Username atau Password Salah !"