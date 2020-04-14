# -*- coding: utf-8 -*-

def CoefBinomLigneSuivante(CoefBinomLigne):
    rep = [1]
    for compteur in range(len(CoefBinomLigne)-1):
        rep.append(CoefBinomLigne[compteur]+CoefBinomLigne[compteur+1])
    rep.append(1)
    return rep

def CoefBinom(k,n):
    CoefBinomLigne = [1]
    for compteur in range(n):
        CoefBinomLigne = CoefBinomLigneSuivante(CoefBinomLigne)
    return CoefBinomLigne[k]

def ProbBinom(n,p,k):
    return CoefBinom(k,n)*(p**k)*((1-p)**(n-k))

