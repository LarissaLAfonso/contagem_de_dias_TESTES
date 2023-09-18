from datetime import date
import doctest

def contagem_dias(data_1: date, data_2: date) -> int:
    '''
    Parâmetros
    -----------
    data_1 : datetime.date
        Uma data do tipo datetime.date
    data_1 : datetime.date
        Uma data do tipo datetime.date
    
    Retorna
    ---------
    dias : int
        Quantidade de dias entre data_1 e data_2
    
    >>> contagem_dias(date(2023, 9, 18), date(2023, 8, 18))
    31

    >>> contagem_dias(date(2022, 9, 18), date(2023, 9, 18))
    365
    '''
    return abs((data_1 - data_2).days)

if __name__ == "__main__":
    doctest.testmod(verbose = True)