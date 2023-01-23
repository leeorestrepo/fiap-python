# Tabela de criticidade
senha        =  100000
ajudaDaSenha =  10000
telefone     =  1000
nomes        =  100
email        =  10

# Base de dados
           #     0      ,       1            ,   2   ,   3   ,   4   ,  5    ,    6
ranking = [# Pontuação  ,   Empresa          , Senha , Ajuda ,  Tel , Nomes  ,  E-mail
          [      0      ,  'Facebook'        ,   1   ,   1   ,   1  ,   1    ,    0     ],
          [      0      ,  'LinkedIn'        ,   1   ,   0   ,   0  ,   0    ,    0     ],
          [      0      ,  'Hurb'            ,   1   ,   1   ,   1  ,   0    ,    1     ],
          [      0      ,  'Last.FM'         ,   1   ,   1   ,   0  ,   0    ,    1     ],
          [      0      ,  'Serasa Experian' ,   1   ,   0   ,   0  ,   1    ,    1     ],
          [      0      ,  'MySpace'         ,   1   ,   1   ,   0  ,   1    ,    1     ],
          [      0      ,  'Minecraft'       ,   1   ,   1   ,   1  ,   1    ,    1     ],
          [      0      ,  'YouPorn'         ,   1   ,   0   ,   0  ,   0    ,    0     ],
          [      0      ,  'Adobe'           ,   1   ,   1   ,   1  ,   1    ,    1     ],
          [      0      ,  'Uber'            ,   1   ,   0   ,   0  ,   1    ,    1     ],
          [      0      ,  'Netshoes'        ,   0   ,   0   ,   0  ,   0    ,    0     ],
          [      0      ,  'C&A'             ,   0   ,   1   ,   1  ,   1    ,    0     ],
          [      0      ,  'Renner'          ,   0   ,   0   ,   0  ,   1    ,    1     ],
          [      0      ,  'Riachuelo'       ,   0   ,   0   ,   1  ,   1    ,    1     ],
          [      0      ,  'Google+'         ,   0   ,   1   ,   1  ,   0    ,    1     ],
          [      0      ,  'Ypê'             ,   0   ,   0   ,   1  ,   0    ,    1     ],
          [      0      ,  'Dell'            ,   0   ,   0   ,   0  ,   0    ,    1     ],
          [      0      ,  'Netflix'         ,   0   ,   1   ,   1  ,   1    ,    0     ],
          [      0      ,  'Banco Inter'     ,   0   ,   0   ,   0  ,   0    ,    1     ],
          [      0      ,  'eBay'            ,   0   ,   1   ,   1  ,   0    ,    1     ]
] # close Ranking []

# Functions
def calculaPontos(ranking):
    c = 0
    while c < len(ranking):

        if (ranking[c][2] == 1):
            ranking[c][0] += senha

        if (ranking[c][3] == 1):
            ranking[c][0] += ajudaDaSenha

        if (ranking[c][4] == 1):
            ranking[c][0] += telefone

        if (ranking[c][5] == 1):
            ranking[c][0] += nomes

        if (ranking[c][6] == 1):
            ranking[c][0] += email

        c+=1

def exibeRanking (ranking):
    c = 0

    ranking.sort()
    ranking.reverse()

    if (len(ranking) > 0):
    # Exibe "Ranking: "
        print("Ranking: ")

        # Exibe a lista do ranking
        while c < len(ranking):
            if c < 3:
                print("\033[91m"+f"{c+1}. {ranking[c][1]}") # 3 primeiros em VERMELHO
            else:
                print("\033[37m"+f"{c+1}. {ranking[c][1]}") # Demais em BRANCO
            c+=1
        c = 0
    else:
        print("Não há vazamentos\n")

# Container
calculaPontos(ranking)
exibeRanking(ranking)