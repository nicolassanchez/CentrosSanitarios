# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:48:40 2019

@author: Toñi Reina
"""

from collections import namedtuple
import csv
import math

from mapas import *

CentroSanitario = namedtuple('CentroSanitario','nombre,localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci')

def lee_centros(fichero):
    '''
       Lee el fichero de entrada y devuelve una lista de tuplas de tipo CentroSanitario
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci) -> [(str, str, float, float, str, int, bool, bool)]

    Cada línea del fichero se corresponde con los datos de un centro sanitario y se representa con una tupla
    y se representa con una tupla con los siguientes valores:
        - Nombre del centro sanitario
        - Localidad en la que está situado el centro sanitario
        - Latitud 
        - Longitud
        - Estado
        - Número de camas
        - Es accesible 
        - Tiene UCI
    '''
    pass


def num_total_camas_centros_accesibles(centros):
    ''' Calcula el número total de camas de los centros que son accesibles para minusválidos
    
    ENTRADA: 
       - centros: lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci) -> [(str, str, float, float, str, int, bool, bool)]
    SALIDA: 
       - total camas-> int

    Toma como entrada una lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci) y 
    produce como salida un entero correspondiente al número total de camas.
    '''
    pass


def centros_con_uci_cercanos(centros, punto, umbral):
    ''' Selecciona los centros que están a una distancia menor o igual que un umbral
    del punto dado como parámetro
    
    ENTRADA: 
       - centros: lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci) -> [(str, str, float, float, str, int, bool, bool)]
       - punto: tupla con la latitud y logitud del punto -> (float, float) 
       - umbral: distancia mayor en la que deben estar los centros ->float
    SALIDA: 
       - lista de tuplas-> (str, str, float, float)

    Toma como entrada una lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci) y 
    produce como salida una lista con el nombre del centro, la localidad, la latitud y la longitud de los centros situados a una distancia menor o igual que
    el umbral del punto dado como parámetro.
    '''
	pass
	
    
#funcion auxiliar para el cálculo de la distancia
def distancia(latitud1, longitud1, latitud2, longitud2):
    '''
    Función auxiliar.
    ENTRADA:
        -latitud1: latitud de un punto -> float
        -longitud1: longitud de un punto -> float
        -latitud2: latitud de un punto -> float
        -longitud2: longitud de un punto -> float
    SALIDA:
        - distancia -> float
    Toma como entrada la latitud y longitud de dos puntos y devuelve la distancia euclídea
    '''
    pass


def media_coordenadas (centros):
    '''
    Calcula un punto cuya latitud es la media de las latitudes de los centros que
    se pasan como parámetro y cuya longitud es la media de las longitudes de los centros.

    ENTRADA:
        - centros: lista de tuplas (nombre, localidad, latitud, longitud) => (str, str, float, float)
    SALIDA:
        - tupla (latitud, longitud) -> (float, float)      
    Toma como entrada una lista de tuplas (nombre, localidad, latitud, longitud) y devuelve una 
    tupla (media_latitud, media_longitud) con la media de las latitudes de los centros
    y la media de las longitudes
    '''
    pass
	

def generar_mapa(centros, fichero):
    '''
    Genera un archivo html con un mapa en el que están geolocalizados los centros
    que se pasan como parámetro.
 
    ENTRADA:
        - centros: lista de tuplas (nombre, localidad, latitud, longitud) => (str, str, float, float)
        - fichero: nombre del archivo html generado
        
    Toma como entrada una lista de tuplas (nombre, localidad, latitud, longitud) y genera 
    un archivo html con un mapa y los iconos gelocalizados
    
    '''
    pass
