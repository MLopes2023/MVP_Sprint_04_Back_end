from MachineLearning.Metodos.carregador     import *
from MachineLearning.Metodos.avaliador      import *
from MachineLearning.Metodos.limpezadados   import *
from MachineLearning.Metodos.modelo         import *
from MachineLearning.Metodos.pipeline       import *

# Para rodar o teste unitário : pytest -v test_modelo.py

# Instanciação das Classes
modelo       = Modelo()
avaliador    = Avaliador()
limpezadados = LimpezaDados()

# Parâmetros do modelo   
# Desconsiderar o campo customer_id do csv, irrelevante para análise
url_dados   = "./MachineLearning/data/test_dataset_Churn.csv"
colunas     = ['credit_score', 'country', 'gender', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary', 'churn']
        
# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)

# limpeza dos dados e eliminação de outliers
dataset =  limpezadados.limpeza_dados(dataset)
        
# Carrega array dataset
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]

# Acurácia do melhor modelo
acuracia_melhor_modelo = 0.86

# Método para testar pipeline KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando pipeline de KNN
    knn_path    = './MachineLearning/pipeline/knn_Churn_pipeline.pkl'
    modelo_knn  = Pipeline.carrega_pipeline(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn = Avaliador.avaliar(modelo_knn, X, y)
    
    # Testando as métricas do KNN
    assert acuracia_knn  >= acuracia_melhor_modelo

# Método para testar pipeline GradientBoosting a partir do arquivo correspondente
def test_modelo_gb():
    
    # Importando pipeline de GradientBoosting
    gb_path = './MachineLearning/pipeline/gb_Churn_pipeline.pkl'
    modelo_gb = Pipeline.carrega_pipeline(gb_path)

    # Obtendo as métricas do GradientBoosting
    acuracia_gb = Avaliador.avaliar(modelo_gb, X, y)
    
    # Testando as métricas do GradientBoosting
    assert acuracia_gb >= acuracia_melhor_modelo
