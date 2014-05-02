#! /usr/bin/python
#!encoding: UTF-8

import moduloerror
import sys
if((len(sys.argv)==1) or (len(sys.argv)==2)):
  print("No se han encontrado los valores necesarios, por lo que se procederá a ejucutar con los valores predeterminado:")
  print("Veces=10   Intervalo=10   Umbral=0.1")
  veces=10
  n=10
  umbral=0.1
else:
  n=int(sys.argv[2])
  veces=int(sys.argv[1])
  umbral=float(sys.argv[3])

print "Nº de subintervalos\tNº de pruebas a realizar\tTolerancia permitida\tPorcentaje de error"

print "%d\t\t\t%d\t\t\t\t%g\t\t\t\t%g" %(n, veces, umbral, moduloerror.error(n, veces, umbral))