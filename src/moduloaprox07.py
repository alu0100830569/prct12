#! /usr/bin/python
#!encoding: UTF-8
pi = 3.1415926535897931159979634685441852
def piaprox(n):
  suma = 0
  if (n!=0):
    for i in range(1,n+1):
      #a = float (i-1)/n
      #b = float(i)/n
      #print 'Subintervalo: (%f , %f) ' % (a, b)
      x = (i-0.5)/n
      f = 4/(1+x*x)
      suma = suma + f
  aprox = suma / n
  return aprox

if __name__=="__main__":
  import sys
  if((len(sys.argv)==1) or (len(sys.argv)==2)):
    print("No se han encontrado los valores necesarios, por lo que se procederá a ejucutar con los valores predeterminados")
    n=10
    veces=10
  else:
    n=int(sys.argv[2])
    veces=int(sys.argv[1])
  a = []
  for vez in range (1,veces+1):
    unaAprox = piaprox(n*vez)
    a=a+[unaAprox]
  print a