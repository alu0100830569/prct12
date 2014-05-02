#! /usr/bin/python
#!encoding: UTF-8

import moduloaprox07
def error (n, veces, umbral):
  fallos = 0
  aprox1 = moduloaprox07.pi
  for vez in range (1, veces+1):
    aprox2 = moduloaprox07.piaprox(n*vez)
    resta = abs(aprox2 - aprox1)
    if (resta > umbral):
      fallos = fallos + 1
      
  porcentaje = (fallos/veces)*100
  return porcentaje

if __name__=="__main__":
  import sys
  if((len(sys.argv)==1) or (len(sys.argv)==2) or (len(sys.argv)==3)):
    print("No se han encontrado los valores necesarios, por lo que se procederá a ejucutar con los valores predeterminados")
    n=10
    veces=10
    umbral = 0.1
  else:
    n=int(sys.argv[2])
    veces=int(sys.argv[1])
    umbral=int(sys.argv[3])
  print ("El porcentaje de error es: ")
  print error(n, veces, umbral)