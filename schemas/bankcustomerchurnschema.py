from datetime                           import datetime
from unicodedata import numeric
from pydantic                           import BaseModel
from typing                             import List
from models.tabelas.bankcustomerchurn   import BankCustomerChurn

class BankCustomerChurnViewBodySchema(BaseModel):
    """ Representação da forma de retorno de busca de uma predição de rotatividade de cliente no banco.
    """
    id: int = 0
    client_name: str = ""
    credit_score: int =  0 
    country: str = ""
    gender: str = ""
    age: int = ""
    tenure: int = ""
    balance: float =  0.00
    products_number: int = ""
    credit_card: int = ""
    active_member: int = ""
    estimated_salary: float = 0.00
    churn: int = ""
    churn_result:str = ""
    dtcadastro:datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class BankCustomerChurnAddBodySchema(BaseModel):
    """ Representação da forma de inserção de uma predição de rotatividade de cliente no banco.
    """
    client_name: str = "ANITA"
    credit_score: int =  620 
    country: str = "Alemanha"
    gender: str = "Feminino"
    age: int = 45
    tenure: int = 1
    balance: float =  99495.00 
    products_number: int = 1
    credit_card: int = 1
    active_member: int = 0
    estimated_salary: float = 40910.00
   
class BankCustomerChurnBuscaSchema(BaseModel):
    """ Representação da estrutura para busca de uma lista de predições de rotatividades de clientes no banco.
    """
    likeclient: str = None

class BankCustomerChurnIdBuscaSchema(BaseModel):
    """ Representação da estrutura para busca de uma predição de rotatividade de cliente no banco.
    """
    id: int
        
class ListaBankCustomerChurn(BaseModel):
    """ Define uma lista das predições de rotatividades de clientes no banco, que deverão ser retornados.
    """
    bankcustomerchurn:List[BankCustomerChurnViewBodySchema]

class BankCustomerChurnDeleteSchema(BaseModel):
    """ Representação da estrutura do dado retornado após uma requisição de exclusão de uma predição de rotatividade de cliente no banco.
    """
    mensagem: str

def retorna_churn_result(churn):
    
    churn_result = ""
    
    if churn == 1:
        churn_result = "1-Sim"
    else:
        churn_result = "0-Não"
        
    return churn_result

def retorna_bankcustomerchurn_atualizado(model:BankCustomerChurnAddBodySchema, predictchurn:int):
    return BankCustomerChurn(   model.client_name,      model.credit_score,
                                model.country,          model.gender,      
                                model.age,              model.tenure,  
                                model.balance,          model.products_number,  
                                model.credit_card,      model.active_member,  
                                model.estimated_salary, predictchurn    )

def retorna_bankcustomerchurn(bankcustomerchurn: BankCustomerChurn):
    """ Retorna uma representação de uma predição de rotatividade de cliente no banco, seguindo o schema definido em BankCustomerChurnViewBodySchema.
    """
    return {
       "id": bankcustomerchurn.id,   
       "client_name":bankcustomerchurn.client_name,
       "credit_score": bankcustomerchurn.credit_score,
       "country": bankcustomerchurn.country,
       "gender": bankcustomerchurn.gender,
       "age": bankcustomerchurn.age,
       "tenure": bankcustomerchurn.tenure,
       "balance": bankcustomerchurn.balance,
       "products_number": bankcustomerchurn.products_number,
       "credit_card": bankcustomerchurn.credit_card,
       "active_member": bankcustomerchurn.active_member,
       "estimated_salary": bankcustomerchurn.estimated_salary,
       "churn": bankcustomerchurn.churn,
       "churn_result": retorna_churn_result(bankcustomerchurn.churn),
       "dtcadastro": bankcustomerchurn.dtcadastro.strftime("%Y-%m-%d %H:%M:%S")
    }    

def retorna_bankcustomerchurns(bankcustomerchurns: List[BankCustomerChurnViewBodySchema]):
    """ Retorna uma representação da lista de predições da rotatividades de clientes no banco, seguindo o schema definido em BankCustomerChurnViewBodySchema.
    """
    result = []
    for bankcustomerchurn in bankcustomerchurns:
        result.append({
            "id": bankcustomerchurn.id,   
            "client_name": bankcustomerchurn.client_name,
            "credit_score": bankcustomerchurn.credit_score,
            "country": bankcustomerchurn.country,
            "gender": bankcustomerchurn.gender,
            "age": bankcustomerchurn.age,
            "tenure": bankcustomerchurn.tenure,
            "balance": bankcustomerchurn.balance,
            "products_number": bankcustomerchurn.products_number,
            "credit_card": bankcustomerchurn.credit_card,
            "active_member": bankcustomerchurn.active_member,
            "estimated_salary": bankcustomerchurn.estimated_salary,
            "churn": bankcustomerchurn.churn,
            "churn_result": retorna_churn_result(bankcustomerchurn.churn),
            "dtcadastro": bankcustomerchurn.dtcadastro.strftime("%Y-%m-%d %H:%M:%S")
        })

    return {"bankcustomerchurns": result}
    