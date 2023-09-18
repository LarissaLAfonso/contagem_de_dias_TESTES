import doctest

def leitor_de_arquivos(path_do_arquivo: str) -> str:
    
    """
    Parâmetros
    ----------
    nome_do_arquivo : string
        nome do arquivo .txt que contém as datas.

    Retorno
    -------
    datas : string
        as duas datas que estão dentro do arquivo.

    >>> leitor_de_arquivos("teste.txt")
    '21 de Abril de 2022 - 35 de Setembro de 2005'
    """

    with open(path_do_arquivo) as arquivo:
        datas = arquivo.readlines()
    
    return datas[0]

if __name__ == "__main__":
    doctest.testmod(verbose=True)