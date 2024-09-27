from    MachineLearning.Metodos.limpezadados import *
from    sklearn.model_selection import train_test_split
import  pickle
import  numpy as np

class PreProcessador:
    
    def __init__(self):
        self.__limpezadados = LimpezaDados();

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        
        # limpeza dos dados e eliminação de outliers
        dataset =  self.__limpezadados.limpeza_dados(dataset)

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                  percentual_teste,
                                                                  seed)
        # normalização/padronização
        
        return (X_train, X_test, Y_train, Y_test)
          
    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """

        dados   = dataset.values
        X       = dados[:, 0:-1]
        Y       = dados[:, -1]
        
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
    
    def preparar_form(self, body):
        """ Prepara os dados recebidos do método do backend, chamado pelo front-end, para serem usados no modelo. """
        X_input = np.array([ body.credit_score, 
                             self.__limpezadados.ret_id_numerico_country(body.country),
                             self.__limpezadados.ret_id_numerico_gender(body.gender), 
                             body.age, 
                             body.tenure, 
                             body.balance, 
                             body.products_number, 
                             body.credit_card, 
                             body.active_member, 
                             body.estimated_salary
                           ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def scaler(X_train):
        """ Normaliza os dados. """
        # normalização/padronização
        scaler = pickle.load(open('./MachineLearning/scaler/minmax_scaler_Churn.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train
