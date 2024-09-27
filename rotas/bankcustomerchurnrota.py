# from urllib3.util.retry import Retry
import  json
from datetime                               import datetime
from serverapp.flaskapp                     import *
from sqlalchemy.exc                         import IntegrityError
from operator                               import and_
from logger                                 import logger
from models.tabelas.bankcustomerchurn       import BankCustomerChurn
from schemas                                import *
from validador.bankcustomerchurnvalidador   import *  
from database.operacao.database_manuseio    import DatabaseManuseio
from database.operacao.datatabase_operacao  import DatabaseOperacao

from MachineLearning.Metodos.pipeline       import Pipeline
from MachineLearning.Metodos.preprocessador import PreProcessador
from MachineLearning.Metodos.modelo         import Modelo
from MachineLearning.Metodos.avaliador      import Avaliador
from MachineLearning.Metodos.carregador     import Carregador

from MachineLearning.Metodos.limpezadados     import *

#################################################################################################################
#####                                       FUNÇÕES INTERNAS DA ROTA
#################################################################################################################

# Verifica existência da predição da rotatividade de cliente no banco no cadastro
def predicao_rotatividade_id_cliente_existe(dbmanuseio, id):
    
    # variavel de retorno
    bexiste = False
    
    # verifica existência
    filtro      = BankCustomerChurn.id == id
    resultcount = dbmanuseio.get_select_count_number(BankCustomerChurn.id, filtro)

    if resultcount > 0:
        bexiste = True
    
    return bexiste   

# Verifica existência do nome do cliente no banco no cadastro
def predicao_rotatividade_nome_cliente_existe(dbmanuseio, client_name):
    
    # variavel de retorno
    bexiste = False
    
    # verifica existência
    filtro      = BankCustomerChurn.client_name == client_name
    resultcount = dbmanuseio.get_select_count_number(BankCustomerChurn.client_name, filtro)

    if resultcount > 0:
        bexiste = True
    
    return bexiste  

# Busca uma única predição da rotatividade de cliente no banco cadastrada
def retorna_predicao_rotatividade_cliente(dbmanuseio, id):
    
    filtro      = BankCustomerChurn.id == id
    return dbmanuseio.get_select_first(BankCustomerChurn, filtro)


#################################################################################################################
#####                                               ROTAS 
#################################################################################################################

# Lista das predições de rotatividades de clientes no banco
@app.get('/BuscaListaPredicaoRotatividadeCliente', tags=[predicao_cliente_tag],
         responses={const_str_httpstatus_ok: ListaBankCustomerChurn, const_str_httpstatus_bad_request: ErrorSchema})
def busca_lista_predicao_rotatividade_clientes(query: BankCustomerChurnBuscaSchema):
    """Buscar um lista das predições de rotatividades de clientes no banco cadastradas.
    
    Retorna uma representação de uma lista de predições de rotatividades de clientes no banco.
    """
    try:
        
        # recupera nome do cliente para filtro
        likeclient      = None
        if query.likeclient:
            likeclient  = query.likeclient
            
        # recupera objeto de manuseio de banco de dados
        dbmanuseio   = DatabaseManuseio()
        
        # recupera dados das predições de rotatividades de clientes cadastradas
        bankcustomerschurns   = None
        if likeclient == None:
            bankcustomerschurns   = dbmanuseio.get_select_all(BankCustomerChurn, None)    
        else:
            consulta = "%{}%".format(likeclient)
            filtro = BankCustomerChurn.client_name.like(consulta)
            bankcustomerschurns   = dbmanuseio.get_select_all(BankCustomerChurn, filtro)    

        if len(bankcustomerschurns) == 0:
           logger.info(f"Lista predições de rotatividades de clientes sem informações")
           return {"bankcustomerschurns": []}, const_value_httpstatus_ok     
        
        # retorna lista 
        logger.info(f"Lista de {len(bankcustomerschurns)} predições de rotatividades de clientes econtrada(s)")
        return retorna_bankcustomerchurns(bankcustomerschurns), const_value_httpstatus_ok
                
    except Exception as e:
        # exceção fora do previsto
        returnerrormesage = ReturnErrorMesage(f"Erro fora do previsto na busca da lista predições de rotatividades de clientes", "Não foi possível efetuar a busca predições das rotatividades de clientes no banco :/")
        logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
        return {"mesage": returnerrormesage.mesage + "."}, const_value_httpstatus_bad_request
    
# Adicionar uma predição da rotatividade de cliente no banco no cadastro
@app.post('/AdicionaPredicaoRotatividadeCliente', tags=[predicao_cliente_tag],
          responses={const_str_httpstatus_ok:           BankCustomerChurnViewBodySchema, 
                     const_str_httpstatus_conflict:     ErrorSchema, 
                     const_str_httpstatus_bad_request:  ErrorSchema})
def adiciona_predicao_rotatividade_cliente(body: BankCustomerChurnAddBodySchema):
    """Adicionar um nova predição de rotatividade de cliente.

   Representação da forma de retorno da predição de rotatividade de cliente inserida no cadastro.
    """
    try:
        
        # valida informacoes recebidas no body
        validador   = BankCustomerChurnValidador(body)
        error_msg   = validador.mensagemvalidador
      
        if error_msg != "" and error_msg != None:
            logger.warning(f"Erro na solicitação para adicionar uma predição de rotatividade de cliente {error_msg}.")
            return {"mesage": error_msg}, const_value_httpstatus_bad_request
        
        # recupera objeto de manuseio de banco de dados
        dbmanuseio = DatabaseManuseio()

        # critica existência do nome do cliente
        if  predicao_rotatividade_nome_cliente_existe(dbmanuseio, body.client_name):
            # retorna mensagem de erro
            returnerrormesage = ReturnErrorMesage(f"Predição de rotatividade do cliente {body.client_name} já cadastrada", "Erro de na solicitação :/")
            logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
            return {"mesage": returnerrormesage.mesage + "."}, const_value_httpstatus_conflict

        # Recupera predição da rotatividade do cliente
        # Preparando os dados para o modelo
        preprocessador  = PreProcessador();
        
        # Prepara os dados para o modelo
        logger.info(f"Preparando os dados para o modelo.")
        X_input = preprocessador.preparar_form(body)
        
        # Carrega modelo
        logger.info(f"Carregando modelo.")
        modelo = Pipeline.carrega_pipeline("./MachineLearning/pipeline/gb_Churn_pipeline.pkl")
                
        # Efetua predição
        logger.info(f"Realizando a predição de rotatividade do cliente.")
        predictchurn = int(Modelo.preditor(modelo, X_input)[0])
        
        # recupera objeto de inserção da predição de rotatividade de cliente 
        logger.info(f"Adicionando predição de rotatividade do cliente.")
        bankcustomerchurn = retorna_bankcustomerchurn_atualizado(body, predictchurn)    

        # adicionando cadastro da predição de rotatividade de cliente
        dbmanuseio.add_tabela(bankcustomerchurn)
        print(bankcustomerchurn)
        logger.info(f"Adicionado cadastro de predição de rotatividade do cliente")
        
        # retorna objeto    
        return retorna_bankcustomerchurn(bankcustomerchurn), const_value_httpstatus_ok

    except Exception as e:
        # exceção fora do previsto
        returnerrormesage = ReturnErrorMesage(f"Erro fora do previsto ao adicionar predição de rotatividade do cliente", "Não foi possível salvar nova predição da rotatividade de cliente :/")
        logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
        return {"mesage": returnerrormesage.mesage + "."}, const_value_httpstatus_bad_request
    
@app.delete('/RemovePredicaoRotatividadeCliente', tags=[predicao_cliente_tag],
            responses={const_str_httpstatus_ok: BankCustomerChurnDeleteSchema, const_str_httpstatus_bad_request: ErrorSchema, const_str_httpstatus_not_found: ErrorSchema})
def remove_predicao_rotatividade_cliente(query: BankCustomerChurnIdBuscaSchema):
    """Remove uma predição de rotatividade de cliente conforme id informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    
    try:
        # Recupe ids para remoção
        id        = query.id
        
        # Recupera objeto de manuseio de banco de dados
        dbmanuseio = DatabaseManuseio()

        # critica não existência de predição de rotatividade do cliente
        if not predicao_rotatividade_id_cliente_existe(dbmanuseio, id):
            # retorna mensagem de erro
            returnerrormesage = ReturnErrorMesage("Predição da rotatividade do cliente não encontrada.", "Erro de na solicitação :/")
            logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
            return {"mesage": returnerrormesage.mesage + "."}, const_value_httpstatus_not_found

        # Remove predição dea rotatividade de cliente
        logger.info(f"Deletando predição de rotatividade de cliente id {id}")
        
        # removendo registro
        filtro  = BankCustomerChurn.id == id
        count   = dbmanuseio.del_tabela(BankCustomerChurn, filtro)
        logger.info(f"Removendo predição de rotatividade de cliente id {id}." )

        if count:
            # Retorna a representação da mensagem de confirmação
            returnerrormesage = ReturnErrorMesage("Predição de rotatividade do cliente removida", "Solicitação efetuada:/")
            logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
            return {"mensagem": returnerrormesage.mesage + "." }
    
    except Exception as e:
        # exceção fora do previsto
        returnerrormesage = ReturnErrorMesage(f"Erro fora do previsto ao adicionar predição de rotatividade do cliente", "Não foi possível salvar nova predição da rotatividade de cliente :/")
        logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
        return {"mesage": returnerrormesage.mesage + "."}, const_value_httpstatus_bad_request
                 
