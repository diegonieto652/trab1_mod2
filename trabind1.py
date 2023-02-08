import pandas as pd

def verificador(x):

    y = ''
    if x == nota_entrevista:
        y = 'entrevista'
    elif x == nota_teorico:
        y = 'teste teórico'
    elif x == nota_pratico:
        y = 'teste prático'
    elif x == nota_soft:
        y = 'soft'

    while not x.isdigit():
        print('Dígito inválido. Favor tente novamente!')
        x = input(f'Nota na etapa de {y}')
    nota_correta = x
    return nota_correta



def verificador_nota_min(x):
    y = ''
    if x == notas_e:
        y = 'entrevista'
    elif x == notas_t:
        y = 'teste teórico'
    elif x == notas_p:
        y = 'teste prático'
    elif x == notas_s:
        y = 'soft'

    while not x.isdigit():
        print('Dígito inválido. Favor tente novamente')
        x = input(f'Nota mínima na etapa de {y}')
    nota_correta = x
    return nota_correta



def buscador (notas_x, notas_y, notas_z, notas_a,candidatos):
    aprovados = []
    for chave, valores in candidatos.items():
        if valores[1] >= notas_x and valores[4] >= notas_y and valores[7] >= notas_z and valores[10] >= notas_a:
            aprovados.append(chave)
        elif aprovados == False:
            print('nenhum candidato encontrado')

    print(f'Os candidatos aprovados para a próxima etapa são: ')
    for itens in aprovados:
        print(itens)



candidatos = {}

while True:
    nome = input('Digite o nome do candidato: ')
    while not nome.isalpha():
        nome = input('Digite o nome do candidato ')
    nota_entrevista = input('Nota na etapa de entrevista: ')
    nota_entrevista = verificador(nota_entrevista)
    nota_teorico = input('Nota na etapa de teste teórico: ')
    nota_teorico = verificador(nota_teorico)
    nota_pratico = input('Nota na etapa de teste pratico: ')
    nota_pratico = verificador(nota_pratico)
    nota_soft = input('Nota na etapa de soft skills: ')
    nota_soft = verificador(nota_soft)
    candidatos.update({f'{nome}': f'e{nota_entrevista}_t{nota_teorico}_p{nota_pratico}_s{nota_soft}'})
    df = pd.DataFrame(list(candidatos.items()), columns=['Candidato', 'Resultado'])
    print('*'*40)
    novo_usuário = input('Deseja cadastrar novo candidato? (sim/não)')
    if novo_usuário == 'sim':
        pass
    else:
        print('Lista de candidatos que realizaram as provas e suas respectivas notas: ')
        print(df)
        break
notas_e = input('Nota mínima para a etapa de entrevista: ')
notas_e = verificador_nota_min(notas_e)
notas_t = input('Nota mínima para a etapa de teste teórico: ')
notas_t = verificador_nota_min(notas_t)
notas_p = input('Nota mínima para a etapa de teste prático: ')
notas_p = verificador_nota_min(notas_p)
notas_s = input('Nota mínima para a etapa de avaliação soft: ')
notas_s = verificador_nota_min(notas_s)
print('*'*40)
buscador(notas_e, notas_t, notas_p, notas_s,candidatos)








