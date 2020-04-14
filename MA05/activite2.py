# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
import random
import math

def preleve():
    n = random.randint(0,10000)
    if n < 8000:
        return 1
    else:
        return 0

def échantillon(tailleEchantillon) :
    ech = []
    for compteur in range(tailleEchantillon):
        ech.append(preleve())
    return ech

def fréquence(liste01) :
    somme = 0
    for nb in liste01:
        somme = somme + nb
    return somme / len(liste01)


def sérieEchantillons(nbEchantillons,tailleEchantillon):
    serieEch = []
    for compteur in range(nbEchantillons):
        serieEch.append(échantillon(tailleEchantillon))
    return serieEch

def sérieFréquences(nbEchantillons,tailleEchantillon):
    serieFreq = []
    for compteur in range(nbEchantillons):
        freq = fréquence(échantillon(tailleEchantillon))
        serieFreq.append(freq)
    return serieFreq

