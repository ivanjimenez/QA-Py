#-*- coding:utf-8 -*-
#!/usr/bin/env python
import os
import sys
import subprocess
import threading

ncour = 3
#f = open('logs/sence.log','w')

def worker(n):
	subprocess.call('python carga_usuarios.py ' + str(n) + ' ' + sys.argv[1] + ' >> logs/sence.log &',shell=True)

for i in range(1,22):
	t = threading.Thread(target=worker, args=(i,))
	t.start()


