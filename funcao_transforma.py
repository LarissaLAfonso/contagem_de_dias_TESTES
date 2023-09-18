from datetime import date
import doctest

dicionario_meses = {"JANEIRO":1, "FEVEREIRO":2, "MARÇO":3, "ABRIL":4, "MAIO":5, "JUNHO":6, 
                    "JULHO":7, "AGOSTO":8, "SETEMBRO":9, "OUTUBRO":10, "NOVEMBRO":11, "DEZEMBRO":12}

def transforma_em_data(data_bruta: str) -> date:
    """
    Parâmetros
    ----------
    data_bruta : str
        data no formato por extenso

    Retorno
    -------
    date
        data no formato datetime
        
    >>> transforma_em_data("25 de Abril de 2026")
    datetime.date(2026, 4, 25)
    """
    
    lista_de_datas = data_bruta.split(" ")
    try:
        dia = int(lista_de_datas[0])
        mes = int(dicionario_meses[lista_de_datas[2].upper()])
        ano = int(lista_de_datas[4])
    except:
        raise Exception("Formato inserido inválido")
    
    data_formatada = date(ano, mes, dia)

    return data_formatada

if __name__ == "__main__":
    doctest.testmod(verbose=True)