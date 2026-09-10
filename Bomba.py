# ESTE SCRIPT DIBUJARÁ LA CURVA CARACTERISTICA DE UNA BOMBA A PARTIR DE TRES PUNTOS DE LA CURVA

#En un futuro la idea es generar la curva directamente con el modelo de la bomba.
# Este modelo se podrá coger de la página de GRUNDFOS

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @file: Bomba.py
  @created: 2026-08-31
  """
# MODULOS
#********************
import math
import numpy as np
import matplotlib.pyplot as plt
import Graficos as GR


class bomba:
    def __init__(self, id,q,h):
        self.id = id
        self.q = q
        self.h=h
# VARIABLES GLOBALES
#********************
#bombas={"modelo":"FRIATEC","q":np.array([0,7.5,15.57])/3600,'h':np.array([13,12.17,9.49])}
bombas = [
    {"modelo": "FRIATEC","q":[0,7.5,15.57],"h":np.array([13,12.17,9.49]),"eta":[0,44,53.6]},
    {"modelo": "32/125","q":[1.47,8,17.5],"h":np.array([12.81,12.17,9.54]),"eta":[10.8,42.8,53.6]},
    {"modelo": "32/160","q":[12, 10, 5],"h":[12, 10, 5],"eta":[0,44,53.6]}
]


def CreaBomba(ax,bx,q_curva,bomba):

    coeficientes=np.polyfit(bomba.q,bomba.h,2)
    polinomio=np.poly1d(coeficientes)

    h_curva=polinomio(q_curva)

    return h_curva


"""
def CreaBomba2(ax,bx,Qmax,bomba,col):
    # 2. Ajusta el polinomio de segundo orden (grado = 2)
    # Retorna los coeficientes [a, b, c] para la ecuación: y = ax² + bx + c

    # Se cogen los puntos del diccionario de definición de bombas
    q= [p["q"] for p in bombas if p["modelo"] == bomba][0]    
    res= np.array([p["h"] for p in bombas if p["modelo"] == bomba],dtype='float32')
    h=res[0]

    coeficientes = np.polyfit(q, h, 2)

    #print("Coeficientes (a, b, c):", coeficientes)
    # Crear una función matemática a partir de los coeficientes
    polinomio = np.poly1d(coeficientes)

    # Generar puntos continuos para dibujar la curva suave
    q_curva = np.linspace(min(q), Qmax, 100)
    h_curva = polinomio(q_curva)

    GR.agregar_curva(ax, q_curva, h_curva, bomba, color=col, estilo='-')

    
    res= np.array([p["eta"] for p in bombas if p["modelo"] == bomba],dtype='float32')
    eta=res[0]
    
    # Creamos la curva de rendimiento
    coeficientes = np.polyfit(q, eta, 2)

    polinomio = np.poly1d(coeficientes)

    # Generar puntos continuos para dibujar la curva suave
    q_curva = np.linspace(min(q), Qmax, 100)
    eta_curva = polinomio(q_curva)

    GR.agregar_curva(bx, q_curva, eta_curva, bomba, color=col, estilo='-')

    return h_curva,eta_curva



"""



def CalculaPot(h,q,bomba):

    pot_h0=h*rho*g*q/3600

    res= np.array([p["eta"] for p in bombas if p["modelo"] == bomba],dtype='float32')
    eta=res[0]
    
    # Creamos la curva de rendimiento
    coeficientes = np.polyfit(q, eta, 2)

    eta0=polinomio(q)

    pot_E0=pot_h0/(eta/100)
    polinomio = np.poly1d(coeficientes)

    return pot_h0,eta0,pot_E0



