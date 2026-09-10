#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: Circuito.py
@created: 2026-08-31
"""

# MODULOS
#******************************
import math
import numpy as np

# CLASES
class tuberia:
    def __init__(self,id, epsilon, L,D):
        self.id=id
        self.epsilon = epsilon
        self.L = L
        self.D=D

class fluido:
    def __init__(self, rho, nu):
        self.rho = rho
        self.nu = nu
        
# VARIABLES GLOBALES
g=9.8

#q=np.linspace(0.001/3600,18/3600,100)


"""
FUNCIÓN PARA EL CALCULO DE PERDIDAS TOTALES DEL CIRCUITO

Se pasa como argumento el coeficiente de los accesorios, la longitud de la tubería y la rugosidad
Los datos del fluido (viscosidad y densidad)
se pasa tambien el caudal máximo al que se quiere estudiar
"""
def CalculoPerdidas(fluido,tuberia,Qmax,k):
    # Se genera el vector de flujo
    q=np.linspace(0,Qmax,100)

    # Se calcula para cada flujo el numero de reynolds y la velocidad para al tubería dada
    [v,Re]=CalculoFlujo(q,tuberia.D,fluido)

    # Para cada valor de numero de reynolds y de velocidad se calcula el coeficiente de
    # perdidas sumando ademas el de los accesorios
    f=coefCarga(tuberia,v,Re)

    # A partir del coeficiente de perdidas y de los datos de la tubería se calculan las perdidas
    hf=perdidaCarga(tuberia,v,f,k)

    # Se devuelven todos los valores calculados para los datos dados
    return v,Re,f,hf
    
"""
************************************************************
  FUNCION PARA CALCULAR EL FLUJO
  Para una caudal dado, en m3/h y un diametro de tubería (m)
  se calcula la velocidad y el numero de reynolds del fluido
************************************************************
"""
def CalculoFlujo(Q,D,fluido):
    A=math.pi*D**2/4
    v=np.array(Q/A)

    Re=np.where(v==0,0.1,fluido.rho*v*D/fluido.nu)

    return v,Re


"""
************************************************************
  FUNCION PARA CALCULAR EL COEFICIENTE DE CARGA
  Se evalue el numero de Reynolds. Si es flujo laminar se usa una
  aproximación empirica
  Si es flujo turbulento se usa la ecuación de SAWMEE-JAIN
************************************************************
"""
def coefCarga(tuberia,v,Re):
    #[v,Re]=CalculoFlujo(q,D)
    # Si el flujo es laminar (Re<2300) se usa la ecuacion de pousille y si es laminar la de Swanee-Jain
    f=np.where(Re<=2300,64/Re,0.25/(np.log10((tuberia.epsilon/(3.7*tuberia.D))+(5.74/Re**0.9)))**2)

    return f


"""
************************************************************
  FUNCION PARA CALCULA LA PERDIDA DE CARGA DE UN TUBO
  Se calcula la perdida de carga según la ecuación de
  DARCY-WEISBACH
************************************************************
"""
def perdidaCarga(tuberia,v,f,k):
    #[v,Re]=CalculoFlujo(Q/3600,tuberia.D,fluido)
    #f=coefCarga(tuberia,q,k)

    # Aplicando la ecuación de Darcy
    #i=0
    #hf={}
    #for L_i in tuberia.L:    
    #    hf[L_i]=f*(L_i/tuberia.D)*(v**2/(2*G))
        
    ht=f*(tuberia.L/tuberia.D)*(v**2/(2*g))

    ha=k*(v**2/(2*g))

    hf=ha+ht
    
    return hf


"""
************************************************************
  FUNCION PARA EL CALCULO DEL PUNTO DE FUNCIONAMIENTO
  Se pasan como parametros ambas curvas y el texto que define
  tanto la bomba como el circuito
************************************************************
"""
def ptoFuncionamiento(q,hb,etab,nombreBomba,hf,texto,fluido):
    diff=hb-hf

    sign_change = np.diff(np.sign(diff)) != 0
    idx = np.where(sign_change)[0]

    # Interpolar el valor exacto de x en cada intersección
    x_intersections = []
    y_intersections = []
    z_intersections = []
    for i in idx:
        # Interpolación lineal entre x[i] y x[i+1]
        x_val = np.interp(0, [diff[i], diff[i+1]], [q[i], q[i+1]])
        y_val = hb[i]
        #z_val=etab[i]
        z_val=1
        x_intersections.append(round(x_val,3))
        y_intersections.append(round(y_val,3))
        z_intersections.append(round(z_val,3))
        
    q0=x_intersections[0]
    h0=y_intersections[0]
    eta0=z_intersections[0]
    """
      print("Interseccion "+nombreBomba + " - "+texto)
      print("Q:",x_intersections[0])
      print("H:", y_intersections[0])
      print("eta:",eta0)

    """
    PotH0=h0*fluido.rho*g*q0/3600
    PotE0=PotH0/(eta0/100)
    return q0,h0,eta0,PotH0,PotE0
    
