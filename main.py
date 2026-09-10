#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: main.py
@created: 2026-08-31
"""
import os
import numpy as np
import matplotlib.pyplot as plt

import Bomba as CB
import Circuito as CC
import Graficos as GR

# se importan las clases
from Circuito import *
from Bomba import *

    
#******************************
# PARAMETROS DE TUBERÍA
#******************************
#epsilon=1.5e-6
#Dint=0.293

#******************************
# PARAMETROS DE CIRUITO
#******************************
#L=165
h=43.5

#******************************
# PARAMETROS DE FLUIDO
#******************************
# Se va a suponer que es agua a 20ºC

#rho=998.21 
#nu=1.005e-3



# VARIABLES GLOBALES


H=43.5

#L=[165,281]

def ImprimeCabecera():
     # Se imprime la cabecera del programa
    os.system('cls' if os.name == 'nt' else 'clear')
    print("********************************************************")
    print("    PROGRAMA DE CREACIóN DE CURVAS DE BOMBAS")
    print("    PBL @ 2026")
    print("********************************************************")
    print()





"""
************************************************************    
    MAIN
************************************************************
"""
def main():
    tub1=tuberia('D=293',1.5e-6,730,0.293)
    tub2=tuberia('D=150',1.5e-6,730,0.150)
    fl1=fluido(998.21,1.005e-3)
    Qmax=0.5
    q=np.linspace(0,Qmax,100)
    k0=[0,11.8]
    k=11.8
    imp=bomba("gravedad",[0,Qmax/2,Qmax],[43.5,43.5,43.5])
    # Se imprime la cabecera del programa
    ImprimeCabecera()


    # Se crea la figura de los gráficos 
    fig, (ax,bx) = plt.subplots(2,1)
    ax.set_title("Curvas H-Q")
    bx.set_title("Curvas de Potencia")

    # Parte principal de los calculos
    #*************************************
    #[v,Re]=CC.CalculoFlujo(q,0.102)
    #f=CC.coefCarga(CC.epsilon,CC.Dint,q,11.8)
    #hf=CC.perdidaCarga(tub1,fl1,Qmax,11.8)
    #hf={k: v + H for k, v in hf.items()}

    # TUBERIA 1
    [v,Re,f,hf]=CC.CalculoPerdidas(fl1,tub1,Qmax,k)
    # Se crean las gráficas de los circuitos
    GR.agregar_curva(ax,q,hf,tub1.id,'red')

    #TUBERIA 2
    [v,Re,f,hf]=CC.CalculoPerdidas(fl1,tub2,Qmax,k)
    # Se crean las gráficas de los circuitos
    GR.agregar_curva(ax,q,hf,tub2.id,'blue')

    
    GR.agregar_curva(bx,q,f,'circuito L=165','red')
    #GR.agregar_curva(ax,q,hf[L[1]],'circuito L=181','blue')
    
    # Se crean las bombas y se calcula el punto de funcionamiento para cada bomba 
    #[hb,etab]=CB.CreaBomba(ax,bx,18,"FRIATEC",'black')
    hb=CB.CreaBomba(ax,bx,q,imp)
    GR.agregar_curva(ax,q,hb,'bomba','black')


    # Calculo del punto de funcionamiento
    etab=0
    texto="tub1"
    [q0,h0,eta0,P_h0,P_E0]=CC.ptoFuncionamiento(q,hb,etab,"FRIATEC",hf,'circuito L=165',fl1)
    print("Interseccion "+imp.id + " - "+texto)
    print("Q:",q0,"m3/s")
    print("H:", h0,"m")
    print("eta:",eta0)
    print("P_h:",P_h0," / P_E",P_E0)

    """
    # Se crea la curva de la bomba
    nombreBomba="FRIATEC"
    texto='circuito L=165'
    [q0,h0,eta0,P_h0,P_E0]=CC.ptoFuncionamiento(hb,etab,"FRIATEC",hf[L[0]],'circuito L=165')
    print("Interseccion "+nombreBomba + " - "+texto)
    print("Q:",q0)
    print("H:", h0)
    print("eta:",eta0)
    print("P_h:",P_h0," / P_E",P_E0)

    texto='circuito L=181'
    [q0,h0,eta0,P_h0,P_E0]=CC.ptoFuncionamiento(hb,etab,"FRIATEC",hf[L[1]],'circuito L=181')
    print("Interseccion "+nombreBomba + " - "+texto)
    print("Q:",q0)
    print("H:", h0)
    print("eta:",eta0)
    print("P_h:",P_h0," / P_E",P_E0)

    
    nombreBomba="32/125"
    texto='circuito L=165'
    [hb,etab]=CB.CreaBomba(ax,bx,18,"32/125",'green')
    [q0,h0,eta0,P_h0,P_E0]=CC.ptoFuncionamiento(hb,etab,"32/125",hf[L[0]],'circuito L=165')
    
    print("Interseccion "+nombreBomba + " - "+texto)
    print("Q:",q0)
    print("H:", h0)
    print("eta:",eta0)
    print("P_h:",P_h0," / P_E",P_E0)

    texto='circuito L=181'
    [q0,h0,eta0,P_h0,P_E0]=CC.ptoFuncionamiento(hb,etab,"32/125",hf[L[1]],'circuito L=181')

    print("Interseccion "+nombreBomba + " - "+texto)
    print("Q:",q0)
    print("H:", h0)
    print("eta:",eta0)
    print("P_h:",P_h0," / P_E",P_E0)
      """
    # Mostrar el resultado final
    plt.show()


if __name__ == '__main__':
    main()

