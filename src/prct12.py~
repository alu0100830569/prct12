#ecoding: UTF-8
#!/usr/bin/python

import platform
import os
import timeit
import time
import moduloerror

def SOFTinfo():
  infosoft={}
  infosoft={'several':platform.uname() , 'S.O':platform.platform, 'Pythons Version' :platform.python_version(), 'Date' :platform.python_build()}
  
  return infosoft
  
def CPUinfo():
  infofile = '/proc/cpuinfo'
  cpu = {} 
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpu['CPU type'] = value
      elif name == 'cache size':
	cpu['cache size'] = value
      elif name == 'cpu MHz':
	cpu['CPU speed'] = value + ' Hz '
      elif name == 'vendor_id':
	cpu['vendor ID'] = value
    f.close()
  return cpu
    
if __name__ == '__main__':
  softinfo = SOFTinfo()
  for keys in softinfo.keys():
    print softinfo[keys]
  cpuinfo = CPUinfo()
  for keys in cpuinfo.keys(): #los devuelve las claves del directorio y despues lo usamos como indice
    print cpuinfo[keys]

  print"Introduzca el nombre del fichero en el que desea almacenar los resultados:"
  nombre_fichero = raw_input ();
  f = open(nombre_fichero,"w")
  for keys in softinfo.keys():
    if type (softinfo[keys])is list:
      f.write('\n'.join(softinfo[keys]))
    else: 
      f.write(str(softinfo[keys]))
      f.write('\n')
  for keys in cpuinfo.keys():
    if type (cpuinfo[keys]) is list:
      f.write('\n'.join(cpuinfo[keys]))
    else:
      f.write(str(cpuinfo[keys]))
      f.write('\n')
  f.close()
	
  print "Introduzca 5 umbrales de error:"
  umbral =[]
  for i in range(5):
    i= float(raw_input('Introduzca el umbral '))
    umbral = umbral + [i]
  print"Introduce el nombre fichero de resultados"
  veces = 10
  intervalos = 10
if (veces>0):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  aproximaciones = 10
  fichero.write("num de intervalos: %d\n"%(intervalos))
  for i in range (5):
    start=time.time()
    moduloerror.error(intervalos, veces, umbral[i])
    finish=time.time() - start
    t=timeit.Timer('moduloerror.error(intervalos, veces, umbral)', setup='import moduloerror')
    print t.timeit(10)
    fichero.write("%2.10f\n"%(finish))
    fichero.close()
  else:
    print "El valor de los intervalos debe ser mayor que 0"