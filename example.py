
from math import radians
import numpy as np


import sys
sys.path.append('C:\\Users\\User\\Documents\\infa 2\\proj 1 hubi\\funckje')

from funkcje import *

wyniki_grs80 = Transformacje(model = "grs80")

plik = 'wsp_inp.txt'
# odczyt z pliku: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.genfromtxt.html
tablica = np.genfromtxt(plik, delimiter=',', skip_header = 4)
# zapis: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.savetxt.html
#np.savetxt("wsp_out.txt", tablica, delimiter=',', fmt = ['%10.2f', '%10.2f', '%10.3f'], header = 'konversja współrzednych geodezyjnych \\ Hubert Mizura')


tablica = np.genfromtxt(plik, delimiter=',', skip_header = 4)
rows,cols = np.shape(tablica)

hirvonen = np.zeros((rows,cols))

flh2xyz = np.zeros((rows,cols))

neu=np.zeros((rows,cols))

u2000 = np.zeros((rows,2))

u1992 = np.zeros((rows,2))

XYZ2elewacja = np.zeros((rows,2))



for i in range(rows):
    
    hirvonen[i] = wyniki_grs80.hirvonen(tablica[i,0],tablica[i,1],tablica[i,2])
    
    flh2xyz[i] = wyniki_grs80.flh2xyz(radians(hirvonen[i,0]),radians(hirvonen[i,1]),(hirvonen[i,2]))
    
    u2000[i] = wyniki_grs80.u2000(radians(hirvonen[i,0]), radians(hirvonen[i,1]))
    
    u1992[i] = wyniki_grs80.u1992(radians(hirvonen[i,0]), radians(hirvonen[i,1]))
    
    XYZ2elewacja[i] = wyniki_grs80.XYZ2elewacja(tablica[i,0],tablica[i,1],tablica[i,2],radians(hirvonen[i,0]), radians(hirvonen[i,1]),hirvonen[i,2])



