from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from MachineLearning.Metodos.modelo import Modelo

class Avaliador:

    def avaliar(model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = Modelo.preditor(model, X_test)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return accuracy_score(Y_test, predicoes)
                
