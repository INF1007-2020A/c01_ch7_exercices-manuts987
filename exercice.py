#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def Masse_volumique(a :int,b:int,c:int) -> int:
    V = 4/3*(math.pi)*a*b*c
    return V

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    volume = Masse_volumique(12,25,45)
    print(volume)
