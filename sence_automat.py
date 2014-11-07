#-*- coding:utf-8 -*-
#!/usr/bin/env python

"""  Automatización de sesiones uchile-sence """

__author__ = "Ingeniería TDCLA"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__  = "Iván Jiménez"
__email__ = "ivan.jimenez@tdcla.com"
__status__ = "Development"
__date__ = "25/07/2014"


import csv
import sys
import time
import datetime
from selenium import webdriver 
import pdb


class SenceCSV(object):
    "Clase que procesa los usuarios de Sence"
    def __init__(self,csvfile):
        "Inicializa el fichero CSV"
        self.csvfile = csvfile
        
    
    def process_csv(self):
        " Devuelve una lista con todos los usuarios Sence"
        try:
            self.f = open(self.csvfile)
            self.csvf = csv.reader(self.f)
            return list(self.csvf)
        except Exception as e:
            print "No se puedo leer el CSV"
            print "Razón: ", e

    def imprime_csv(self):
        "Imprime todos los usuarios Sence"
        for row in self.csvf:
            print row
     
class Autentica(object):
    "Clase que realiza la autenticación a Uchile y Sence"
    def __init__(self, list, user,coursenum):
        "Inicializaicón de Rut, Password y Password Sence"
        self.rut = list[user][0]       # Rut
        self.password = list[user][1]  # Password uchile
        self.pwdsence =  list[user][4] # Password Sence
        self.course = [list[user][5],list[user][6],list[user][7],list[user][8]]    # Curso 1
        self.coursenum = coursenum
    
    def login(self):
        "Automatización de la navegación"

        try:
            #self.driver = webdriver.PhantomJS('./phantomjs')  # Para Linux
            self.driver = webdriver.PhantomJS('../bionet/phantomjs/bin/phantomjs')
	    #self.driver = webdriver.PhantomJS()  # Para Mac OS
            #self.driver = webdriver.Firefox()  # En modo visual
            self.driver.get("http://uchile.campustdc.com")
            time.sleep(3)
            self.driver.find_element_by_name('login_userid').send_keys(self.rut)
            self.driver.find_element_by_name('login_pwd').send_keys(self.password)
            time.sleep(3)
            self.driver.find_element_by_name('log_button').click()
            
            ts = time.time()
            fecha_actual = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            

            print "[{0} ==> Procesando usuario: {1}; Curso: {2} ==>".format(fecha_actual, self.rut, self.coursenum),
            #print "[%s ==> Procesando usuario: %d]" % fecha_actual, self.rut
            
            
            # A veces no está en el panel principal y hay que buscar el curso en Completado
                      
            try:
                time.sleep(2)
                self.driver.find_element_by_link_text(self.course[self.coursenum]).click()
            except:
                time.sleep(2)
                self.driver.find_element_by_xpath("//div[@id='tab_content']/div/ul/li[4]/a").click()
                time.sleep(2)
                self.driver.find_element_by_link_text(self.course[self.coursenum]).click()
                
            time.sleep(5)
            self.driver.find_element_by_name('password').send_keys(self.pwdsence)
            self.driver.find_element_by_css_selector('div.ui-dialog-buttonpane > div.ui-dialog-buttonset > button:nth-child(3)').click()
            
            start = datetime.datetime.utcnow()
            
            # 150 minutos cada vez : 2h 30m
            #for i in range(0,150): 
               # self.driver.refresh()
               # time.sleep(60)
            time.sleep(1800) 					#9600 2horas 40 minutos, 3600 por 1h. 1800 por def. 
            end = datetime.datetime.utcnow()

            self.driver.refresh()
            self.driver.find_element_by_class_name('logout').click()
            self.driver.quit()
            time.sleep(3)
            
            total_time = end - start

            print "OK Login {0}: Total Time (H:MM:SS): {1}]".format(self.rut, total_time),
            
        except Exception as e:
            print "Error %s, user: %s, curso: %s]" % e, str(list[user][0]), str(coursenum)
           
            

             
        
 
    



