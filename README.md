### API Aplication Bank Customer Churn Prediction

- Projeto seguindo o estilo REST, responsável pelo fornecimento dos endpoints de controle de registro das predições de rotatividade de clientes, cujo o objetivo é prever a rotatividade de clientes no banco, aplicando o melhor modelo de machine learnig, com base nos dados dos correntidas do ABC Multinational Bank fornecidos, tornando possível adicionar, listar e remover predições. 
Fonte dos dados : (https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)

- A api será consumida pelo front-end APP Bank Customer Churn Prediction.

- Tecnologias adotadas:
 - [Python:3.9](https://www.python.org/downloads/release/python-390/)
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [OpenAPI3](https://swagger.io/specification/)

---
### Execução em ambiente de Desenvolvimento 

- Abrir o terminal na pasta da api da aplicação, onde se encontram os arquivo app.py e requirements.txt

- Criar um ambiente virtual

  python -m venv env
  
- Comandos para ativação do ambiente, conforme sistema operacional:

   - env\Scripts\Activate (Sistema Operacional Windows)

     Observação: 
     Antes deverá liberar a execução de script no PowerShell basta seguir os passos abaixo:
     - Va em pesquisar no menu do Windows 10 digite PowerShell e selecione o ícone clicando nele com o botão direito e clique em executar como Administrador.

    - Caso apareça uma janela com a seguinte mensagem “Deseja permitir que esse aplicativo faça alterações no seu dispositivo?”; clique em Sim.

    - No PowerShell digite o  comando abaixo e pressione enter:
      Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
      Será perguntado se deseja aceitar as mudanças, digite s e pressione enter para confirmar: digitar S.

 - source env/Scripts/Activate (Sistema Operacional Mac / Linux)

- Instalar as dependências necessárias para rodar o projeto com base no arquivo requirements.txt, conforme comando abaixo:

  pip install -r requirements.txt

- Levantando o servidor Flask: 

   flask run --host 0.0.0.0 --port 5000

   O serviço poderá ser acessado no browser no link http://127.0.0.1:5000/#/.

---

### Executar através do Docker

- É imprescindível ter o Docker instalado e iniciado em seu computador.

- Após clonar o repositório, navegue para o diretório em que se encontram os arquivos Dockerfile e requirements.txt, executar como **administrador** os comandos abaixo, para construção da imagem Docker:  
  
  - Construir imagem  Docker:
    
    docker build -t back-end-churn .

  - Criar uma rede Docker:
  
    docker network create minha_rede

  - Executar o container
    
    docker run -d --name back-end-churn --network minha_rede -p 5000:5000 back-end-churn

- No mesmo diretório executar como **administrador** o comando abaixo, para execução do container:  
  
  docker run -p 5000:5000 back-end-churn

- API disponível e basta abrir o http://localhost:5000/#/ no navegador.

- Caso haja a necessidade de **parar um conatiner**, basta executar os comandos: 

  Efetuar o comando **docker container ls --all** (vai retornar containers existentes para localização do ID do container para ser utilizado no comando abaixo):

  Efetuar o comando **docker stop CONTAINER_ID**, sendo CONTAINER_ID recuperado no comanddo anterior.

  --- 

### Documentação para consumo da API Bank Customer Churn Prediction

O consumo da API terá permissão dos seguintes procedimentos e respectivos endpoints:

Os campos que forem opcionais no request serão informados na coluna de descrição do layout, e caso não informados serão obrigatórios por padrão.

1.Registra uma nova predição da rotatividade de um cliente.

**Rota do Método**

/AdicionaPredicaoRotatividadeCliente
POST

**Layout**


| **REQUEST BODY JSON**||||
| -- | --| --| --|
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| client_name  |string| 20 | Nome do cliente
| credit_score  |numérico| | Pontuação de crédito
| country  |string| 10 | País de residência do cliente com as seguintes opções ( Alemanha, Espanha ou França)
| gender  |string| 10 | Gênero (feminino ou masculino)
| age  |integer| | idade do cliente
| tenure  |integer| | Há quantos anos tem conta bancária no banco
| balance  |numérico|1-15V2 | Saldo em conta
| products_number  |integer| | Quantidade de produtos no banco
| credit_card  |integer| | Cliente tem cartão de crédito no banco 1 = sim ou 0 = não
| active_member  |integer| | Cliente ativo no banco 1 = sim ou 0 = não
| estimated_salary  |numérico|1-15V2| Salário estimado
| **RESPONSE 200 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| id  |integer|  | Código identificador da predição de rotatividade do cliente
| client_name  |string| 20 | Nome do cliente
| credit_score  |numérico| | Pontuação de crédito
| country  |string| 10 | País de residência do cliente com as seguintes opções ( Alemanha, Espanha ou França)
| gender  |string| 10 | Gênero (Feminino ou Masculino)
| age  |integer| | idade do cliente
| tenure  |integer| | Há quantos anos tem conta bancária no banco
| balance  |numérico|1-15V2 | Saldo em conta
| products_number  |integer| | Quantidade de produtos no banco
| credit_card  |integer| | Cliente tem cartão de crédito no banco 1 = sim ou 0 = não
| active_member  |integer| | Cliente ativo no banco 1 = sim ou 0 = não
| estimated_salary  |numérico|1-15V2| Salário estimado
| churn  |integer| | Cliente saiu do banco durante algum período 1 = sim ou 0 = não
| churn_result  |string| 5 | Retorno do churn formatado "1-Sim" ou "0-Não"
| dtcadastro  |string| 19 | Data do cadastro no formato "YYYY-MM-DD HH:MM:SS"
| **RESPONSE 404, 409 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem

2.Consulta os dados de todas as predições de rotatividade de clientes cadastradas.

**Rota do Método**

/BuscaListaPredicaoRotatividadeCliente
GET

**Layout**

| **REQUEST QUERY**||||
| -- | --| --| --|
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| id  |integer|  | Código identificador da predição de rotatividade do cliente
| **RESPONSE 200 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| id  |integer|  | Código identificador da predição de rotatividade do cliente
| client_name  |string| 20 | Nome do cliente
| credit_score  |numérico| | Pontuação de crédito
| country  |string| 10 | País de residência do cliente com as seguintes opções ( Alemanha, Espanha ou França)
| gender  |string| 10 | Gênero (Feminino ou Masculino)
| age  |integer| | idade do cliente
| tenure  |integer| | Há quantos anos tem conta bancária no banco
| balance  |numérico|1-15V2 | Saldo em conta
| products_number  |integer| | Quantidade de produtos no banco
| credit_card  |integer| | Cliente tem cartão de crédito no banco 1 = sim ou 0 = não
| active_member  |integer| | Cliente ativo no banco 1 = sim ou 0 = não
| estimated_salary  |numérico|1-15V2| Salário estimado
| churn  |integer| | Cliente saiu do banco durante algum período 1 = sim ou 0 = não
| churn_result  |string| 5 | Retorno do churn formatado "1-Sim" ou "0-Não"
| dtcadastro  |string| 19 | Data do cadastro no formato "YYYY-MM-DD HH:MM:SS"
| **RESPONSE 404 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem

3.Remove uma predição da rotatividade do cliente já cadastrada.

**Rota do Método**

/RemovePredicaoRotatividadeClienteemoveGameLista
DELETE

**Layout**

| **REQUEST BODY JSON**||||
| -- | --| --| --|
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| id  |integer|  | Código identificador da predição de rotatividade do cliente
| **RESPONSE 200 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem de predição removida com sucesso
| **RESPONSE 400, 404 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem
