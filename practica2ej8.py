#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  practica2ej8.py
#  
#  Copyright 2020 adria <adria@DESKTOP-QNDFMPL>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    
    def es_primo(num):
        if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
            return False
        if num == 2:
            return True # si es dos es primo
        for i in range(2, num):  #un rango desde el dos hasta num
            if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
                return False
            return True    #de lo contrario devuelve Verdadero

    cadena = input()
    cadena = cadena.lower()
    diccionario = {}
    for x in cadena:
        if x in diccionario:
            diccionario[x] += 1
        else:
            diccionario[x] = 1
    print(diccionario)
    for x in diccionario:
        if es_primo(diccionario[x]):
            print ('La cantidad de veces que aparece ' + x + ' es un numero primo')
        else:
            print('La cantidad de veces que aparece ' + x + ' no es un numero primo')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
