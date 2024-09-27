import pandas as pd

class Carregador:

    def carregar_dados(url: str, atributos: list):
        """ Carrega o dataset e retorna um DataFrame. 
        """
        
        return pd.read_csv(url, names=atributos, header=0,
                           skiprows=0, delimiter=',') 
    