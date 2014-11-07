#-+- coding:utf-8 -*-
#!/usr/bin/env python
import pdb
import sys
from sence_automat import *
import logging

#Loggin section is disabled by huge large files
#Directory "logs" is mandatory in project root

#LOG_FILENAME = 'logs/log_sence.log_usuario_'+str(sys.argv[1])
#logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

current = int(sys.argv[1])
course = int(sys.argv[2])

csv_file = 'rut_usuarios_uchile_tramo1.csv' # CSV File

try:
	s = SenceCSV(csv_file)  #Cargamos el CSV
	users = s.process_csv() # Procesamos el CSV
	auth = Autentica(users,current,course)
	auth.login()
             
except Exception as e:

	print "Error: python carga_usuarios usuario curso:",current,course



