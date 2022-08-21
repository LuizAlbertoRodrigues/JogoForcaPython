#!/usr/bin/env python
# coding: utf-8

# In[7]:


# JOGO DA FORCA PYTHON #
# CREATED BY LUIZ ALBERTO #

from random import choice
with open('email.txt') as arquivo:# <-- COLOCAR UM ARQUIVO EXISTENTE .TXT PARA SER A PALAVRA SECRETA #
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')
 
    palavra = choice(lista_de_palavras).upper()
forca = """"
_____
 |
 |
 -"""
vazio = """
"""
cabeca = """
 O
"""
tronco = """
 O
 |
"""
braco_esquerdo = """
 O
 /|
"""
braco_direito = """
 O
 /|\\
"""
perna_esquerda = """
 O
 /|\\
 /
"""
perna_direita = """
 O
 /|\\
 / \\
"""
chances_do_boneco = [
vazio, 
cabeca,
tronco, 
braco_esquerdo, 
braco_direito, 
perna_esquerda, 
perna_direita,
]
print(chances_do_boneco)

acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''
while acertos != len(palavra) and erros != 7:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra} '
 
        else:
            mensagem += '_'
 
    print(forca+chances_do_boneco[erros])
print(mensagem)
 
letra = input('Digite uma Letra : ').upper()
print('=-='*10)
 
if letra in letras_acertadas+letras_erradas:
    print('Você já tentou essa letra!')
continue
 
if letra in palavra:
    print('Você ACERTOU a letra!')
    print('=-='*10)
    letras_acertadas += letra
    acertos += palavra.count(letra)
 
else:
    print('Você ERROU a letra!')
    print('=-='*10)
    letras_erradas += letra
    erros += 1


# In[ ]:




