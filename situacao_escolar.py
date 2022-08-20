from statistics import mean


def boletim(* num, sit=False):
    """
    -> Função para gerar um boletim com maior, menor, média e situação do aluno.
    :param num: Acumula todas as notas informadas.
    :param sit: (OPCIONAL) para mostrar ao usúario a situação do aluno.
    :return: retornar o valor da função / boletim do aluno.
    """
    if sit:
        bolet = {'Total':len(num), 'Maior':max(num), 'Menor':min(num), 'Média':mean(num)}
        if bolet['Média'] >= 7:
            bolet['Situação'] = 'BOA'
        elif 5 <= bolet['Média'] < 7:
            bolet['Situação'] = 'RAZOÁVEL'
        else:
            if bolet['Média'] < 5:
                bolet['Situação'] = 'RUIM'
    else:
        bolet = {'Total': len(num), 'Maior': max(num), 'Menor': min(num), 'Média': mean(num)}

    return bolet


anwers = boletim(5.0, 10, 10, sit=True)
print(anwers)
help(boletim)
