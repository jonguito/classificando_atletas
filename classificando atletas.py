anoNascimento = int(input('ano de nascimento:  '))
idadeAtleta = 2024 - anoNascimento

if idadeAtleta >0 and idadeAtleta <9 :
    print(f'''O atleta tem {idadeAtleta}anos\n
classificação: MIRIM   ''')
    
elif idadeAtleta >=9 and idadeAtleta <14:
    print(f'''O atleta tem {idadeAtleta}anos\n
classificação: INFANTIL''')
    
elif idadeAtleta >=14 and idadeAtleta< 19:
    print(f''' O atleta tem {idadeAtleta} anos\n
classificação: JUNIOR  ''')
    
elif idadeAtleta >= 19 and idadeAtleta < 25:
    print(f''' O atleta tem {idadeAtleta}anos\n
classificação: SÊNIOR ''')

elif idadeAtleta >=25:
    print(f''' O atleta tem {idadeAtleta}anos\n
classificação: MASTER ''')
