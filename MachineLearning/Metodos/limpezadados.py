import numpy as np

class LimpezaDados:
    
    def __init__(self):
        pass

    def limpeza_dados(self, dataset):
        """ Cuida da limpeza dos dados e eliminação de outliers. """
        
        # Substituição das variáveis categóricas para numéricas
        dataset["country"] = dataset["country"].map(self.__mapping_country())
        dataset["gender"]  = dataset["gender"].map(self.__mapping_gender())

        return dataset
    
    def ret_id_numerico_country(self, country):
        
        valor = 0
        
        if country == "França":
            valor = 1
        elif country == "Espanha":
            valor = 2
        elif country == "Alemanha":
            valor = 3
                        
        return valor
                            
    def __mapping_country(self):
        
        mapping_country ={
                            'France'  : 1,
                            'Spain'   : 2,
                            'Germany' : 3
                        }
        
        return mapping_country
    
    def ret_id_numerico_gender(self, gender):
        
        valor = 0
        
        if gender == "Feminino":
            valor = 1
        elif gender == "Masculino":
            valor = 2
        
        return valor;
    
    def __mapping_gender (self):
        
        mapping_gender ={
                            'Female'  : 1,
                            'Male'    : 2
                        }
        
        return mapping_gender 
      
    