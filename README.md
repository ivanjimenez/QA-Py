#Configuraciones

- HOST: escape 1 / 216.185.158.18
- Base de datos: uchile_docebo
- Tablas: core_users y learning_sence

# Tareas


* La lista de usuarios: url, login, passwd, curso, clave sence, 20 minutos de sesión

* =>Login uchile => seleccionar curso => enviar clave => 20 minutos => logout

#Links de uso
https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/
http://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
http://stackoverflow.com/questions/10126710/python-neat-way-of-creating-multiple-objects


# Preinstalaciones
- sudo pip install selenium
- sudo pip install PhantomJS


#Código base

from selenium import webdriver
browser = webdriver.Firefox() // browser = webdriver.PhantomJS()
browser.get('http://uchile.campustdc.com')
browser.find_element_by_name('login_userid').send_keys('126343302')
browser.find_element_by_name('login_pwd').send_keys('1263')
browser.find_element_by_name('log_button').click()
//browser.find_element_by_xpath('index.php?modname=course&op=aula&idCourse=13').click()

link = browser.find_element_by_link_text('Conceptos Básicos de Evaluación_Sence')
link.click()
browser.find_element_by_name('password').send_keys('UY704681')
browser.find_element_by_css_selector('div.ui-dialog-buttonpane > div.ui-dialog-buttonset > button:nth-child(3)').click()
browser.refresh()
browser.find_element_by_class_name('logout').click()

- Snippet de multinstancia de clase:

object_1, object_2, ... = [MyClass(property=foo, property2=x) for x in (bar,
  bar2, ...)]

- Para el tema de los cursos en Completados
driver.find_element_by_xpath("//div[@id='tab_content']/ul/li[4]/a").click()
#Issues
* 1 Usuarios con problemas de autenticación: 
[ { 1: Ok}
  {2: Elegir curso}
  {3: Ok}
  {4: Ok}
  {5: Problema}
  {6: Ok}
  {7: Ok}
  {8: Problema}
  {9: Ok}
  {10:Ok}
  {11: Ok }
  {12: Ok }
  {13: Ok}
  {14: Problema}
  {15: Problema}
  {16: Problema**no loguea}
  {17: Ok}
  {18: Ok}
  {19: Ok}
  {20: Ok}
  ]
  


#Requerimiento 20-08-2014

RQ1

- Tobar y Tapia nuevos en Sence => 30, Para los cursos:

  * Conceptos Básicos ... Sence
  * Aprendizajes complejos Sence
  * Construcción... Sence

RQ2

 Para todos (mínimo 20 horas)
  * Conceptos Básicos
  * Aprendizajes

RQ3

- Todos los usuarios (incluidos Tobar y Tapia)
   
  *Instrumentación socio afectiva...Sence
  * De 18 AGO al 26 de Septiembre
  * Mínimo 20 horas
    
