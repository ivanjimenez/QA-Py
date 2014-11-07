# -*- coding: utf-8 -*-
  
'''
  Script auth SENCE via uchile
  @Iván Jiménez 

  TDCLA Ingeniería

'''

import mechanize
import cookielib
import sys

# Usuario
user = '126343302'

# Password

password = '1263'

# Password sence

pwdsence = 'UY704681'

# URL de campustdc.com
url = 'http://uchile.campustdc.com'

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()

br.set_cookiejar(cj)

# Opciones del browser
br.set_handle_equiv(True) 
br.set_handle_gzip(True) 
br.set_handle_redirect(True) 
br.set_handle_referer(True) 
br.set_handle_robots(False)

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; es-VE; rv:1.9.0.1)Gecko/2008071615 Debian/6.0 Firefox/9')]

try:
		r = br.open(url)

		br.select_form(nr=0)

		br.form['login_userid'] = user
		br.form['login_pwd'] = password

		response = br.submit()

except: 
		print "Excepción: "
		e = sys.exc_info()[0]
