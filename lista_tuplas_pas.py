""""
número de inscrição,
nome do candidato em ordem alfabética,
escore bruto da parte 1 na primeira etapa,
escore bruto da parte 2 na primeira etapa,
nota na redação na primeira etapa;

escore bruto da parte 1 na segunda etapa,
escore bruto da parte 2 na segunda etapa,
nota na redação na segunda etapa;

escore bruto da parte 1 na terceira etapa,
escore bruto da parte 2 na terceira etapa,
nota na redação na terceira etapa,
argumento final,
classificação final no Sistema Universal,
classificação final no Sistema de Cotas para Negros (se houver) e

classificação final no Sistema de Cotas para Escolas Públicas:
candidatos com renda familiar bruta igual ou inferior a 1,5 salário mínimo per capita que se autodeclararam pretos, pardos ou indígenas (se houver);
candidatos com renda familiar bruta igual ou inferior a 1,5 salário mínimo per capita que se autodeclararam pretos, pardos ou indígenas e que concorrem como pessoas com deficiência (se houver);
candidatos com renda familiar bruta igual ou inferior a 1,5 salário mínimo per capita que não se autodeclararam pretos, pardos ou indígenas (se houver);
candidatos com renda familiar bruta igual ou inferior a 1,5 salário mínimo per capita que não se autodeclararam pretos, pardos ou indígenas e que concorrem como pessoas com deficiência (se houver);
candidatos com renda familiar bruta superior a 1,5 salário mínimo per capita que se autodeclararam pretos, pardos ou indígenas (se houver);
candidatos com renda familiar bruta superior a 1,5 salário mínimo per capita que se autodeclararam pretos, pardos ou indígenas e que concorrem como pessoas com deficiência (se houver);
candidatos com renda familiar bruta superior a 1,5 salário mínimo per capita que não se autodeclararam pretos, pardos ou indígenas (se houver);
candidatos com renda familiar bruta superior a 1,5 salário mínimo per capita que não se autodeclararam pretos, pardos ou indígenas e que concorrem como pessoas com deficiência (se houver)


inscricao
nome
escoreBruPart1Etapa1
escoreBruPart2Etapa1
redacaoEtapa1
escoreBruPart1Etapa2
escoreBruPart2Etapa2
redacaoEtapa2
escoreBruPart1Etapa3
escoreBruPart2Etapa3
redacaoEtapa3
argumentoFinal
classificacaoUniversal
classificacaoUnivNegros
clasEscPubInfCotPret
clasEscPubInfCotPretDef
clasEscPubInf
clasEscPubInfDef
clasEscPubSupCotPret
clasEscPubSupCotPretDef
clasEscPubSup
clasEscPubSupDef

inscricao, nome, escoreBruPart1Etapa1, escoreBruPart2Etapa1, redacaoEtapa1, escoreBruPart1Etapa2,
escoreBruPart2Etapa2, redacaoEtapa2, escoreBruPart1Etapa3, escoreBruPart2Etapa3, redacaoEtapa3, argumentoFinal,
classificacaoUniversal, classificacaoUnivNegros, clasEscPubInfCotPret, clasEscPubInfCotPretDef, clasEscPubInf,
clasEscPubInfDef, clasEscPubSupCotPret, clasEscPubSupCotPretDef, clasEscPubSup, clasEscPubSupDef = lista[0]


"""

import re

dadosBrutos = """17169166, Agatha Poliana Cordeiro Leite, 6.720, 31.360, 7.909, 2.382, 10.321, 8.310, 5.110, 17.033,
9.643, -20.329, 94, -, 5, -, 6, -, 12, -, 21, - / 17133575, Alex Martins de Torres, 5.880, 22.958, 6.107, 3.970,
16.144, 6.379, 3.650, 18.737, 6.233, -23.805, 103, -, -, -, -, -, -, -, -, - / 17171248, Alexandre Nunes Martins,
9.240, 19.879, 6.131, -3.706, 20.908, 6.250, 2.190, 19.223, 6.404, -23.903, 104, -, -, -, -, -, -, -, -,
- / 17192510, Alinie Ferreira Rodrigues, 0.840, 2.238, 1.783, -1.324, 0.792, 4.935, 0.243, 0.730, 6.232, -110.075,
184, -, -, -, -, -, 26, -, 45, - / 17106897, Alissianne Alves Pereira, 4.200, 15.679, 4.652, 0.264, 10.057, 5.818,
3.163, 16.060, 6.145, -47.008, 144, -, -, -, -, -, -, -, -, - / 17105323, Alisson Nune s Elias, 0.000, 17.359, 7.241,
4.234, 20.378, 6.545, 1.703, 9.733, 6.679, -45.749, 141, -, -, -, 10, -, -, -, 37, - / 17130369, Alvaro Ricardo,
0.280, 15.678, 5.753, -0.794, 6.880, 3.205, 0.730, 12.410, 4.666, -71.399, 170, -, -, -, -, -, -, -, 43,
- / 17181576, Ana C arolina Lopes de Medeiros, 5.040, 34.439, 8.058, 5.558, 16.937, 8.400, 5.110, 23.847, 8.673,
1.939, 60, -, -, -, -, -, -, -, -, - / 17101485, Ana Catarina Gomes Correa, 3.360, 31.080, 5.685, 3.176, 26.995,
7.667, 4.380, 33.093, 9.533, 30.718, 33, -, -, -, -, -, 2, -, 2, - / 17194485, Ana Clara Barros Queiroz, 3.360,
15.399, 6.000, 3.970, 21.702, 8.263, 0.243, 22.387, 5.641, -18.805, 88, -, -, -, -, -, -, -, -, - / 17180468,
Ana Luiza Braganca Oliveira Amorim, 6.720, 51.939, 6.190, 7.146, 42.080, 8.610, 8.030, 37.960, 8.462, 80.751 , 3, -,
-, -, -, -, -, -, -, - / 17194361, Anabel Luz Cavalcante, 4.200, 34.438, 8.133, 3.440, 19.320, 0.000, 3.163, 17.763,
6.833, -24.618, 107, -, -, -, -, -, -, -, -, - / 18252826, Andre Leoncio Silva Caetano, 0.000, 0.000, 0.000, -2.118,
22.496, 7.341, 0.973, 8.03 0, 5.867, -61.786, 161, -, -, -, -, -, -, -, -, - / 17107671, Andre Valle Magalhaes,
1.680, 27.719, 7.960, 5.558, 26.995, 6.632, 0.243, 39.907, 6.876, 35.037, 29, -, -, -, -, -, -, -, -, - / 17116701,
Andressa Araujo Dantas, 2.520, 0.000, 5.426, 0.264, 22.496, 5.159, 0.243, 18.737, 4.878, -40.795, 130, -, -, -, -, -,
-, -, -, - / 17122052, Angela Rose do Nascimento Teixeira, 0.000, 22.399, 5.833, -0.794, 6.085, 5.044, 2.190, 14.600,
5.622, -56.203, 154, -, -, -, -, -, -, -, -, - / 17171324, Angelo Gil Lopes da Cunha, 0.000, 25.899 , 6.083, 7.146,
13.231, 5.774, 0.730, 13.627, 7.033, -42.025, 131, -, -, -, -, -, -, -, -, - / """

dadosBrutos = re.sub("\n", "", dadosBrutos)

# print(dadosBrutos.index("/"))
lista = []
ini = 0
fim = 0

for _ in range(dadosBrutos.count("/")):
    fim = dadosBrutos.index("/", fim)
    lista.append(tuple(dadosBrutos[ini:fim].split(",")))
    ini = fim + 1
    fim = ini


print(dadosBrutos)
print(lista)
print()
print()
print(lista[0][0])

