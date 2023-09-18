from datetime import date
import doctest

dicionario_meses = {"Janeiro":1, "Fevereiro":2, "Março":3, "Abril":4, "Maio":5, "Junho":6, 
                    "Julho":7, "Agosto":8, "Setembro":9, "Outubro":10, "Novembro":11, "Dezembro":12}

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
    
    dia_1 = int(lista_de_datas[0])
    mes_1 = int(dicionario_meses[lista_de_datas[2]])
    ano_1 = int(lista_de_datas[4])
    
    data_formatada = date(ano_1, mes_1, dia_1)
    
    return data_formatada

if __name__ == "__main__":
    doctest.testmod(verbose=True)