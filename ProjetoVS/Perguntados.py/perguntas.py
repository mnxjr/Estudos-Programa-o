from dados_prgts import dados

perguntas = []
temp = {}


for p in dados:
    str(p)
    pos_alt = p.find('Alternativa') # posição inicial da 'Alternativa'
    alt = p[pos_alt:] # somente Alternativa até o fim

    # PERGUNTA/ENUNCIADO 
    end = p.find('a)')
    enunciado = p[:end].replace('\n', '').strip()
    temp['Pergunta'] = enunciado  # adicionar o enunciado na biblioteca da pergunta

    # OPÇÕES
    op = p[len(enunciado):pos_alt]
    op2 = op.strip().split('\n')
    temp['Opções'] = op2

    # RESPOSTAS
    if 'certa:' in alt:
        resp = alt.replace('Alternativa certa:','')
        resp2 = resp[1]
        temp['Resposta'] = resp2

    else:
        resp = alt.replace('Alternativa','')
        resp2 = resp[1]
        temp['Resposta'] = resp2

    perguntas.append(temp.copy())
