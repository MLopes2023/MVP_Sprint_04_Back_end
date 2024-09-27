import numpy as np
import pickle
import joblib
from MachineLearning.Metodos.preprocessador import PreProcessador

class Modelo:
    
    # TODO: Guardar model como atributo e o preditor receber as entradas.
    # TODO: preditor -> realiza predição cliente
    
    def carrega_modelo(path):
        """Carrega .pkl ou .joblib.
        """
        
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, X_input):
        """Realiza a predição de um cliente com base no modelo treinado
        """
        churn = model.predict(X_input)
        return churn