from util.util                              import Util
from schemas.bankcustomerchurnschema        import *
from database.operacao.datatabase_operacao  import DatabaseOperacao

# Classe responsável pela validação das informações de entrada de chamadas das api's de predição da rotatividade do cliente do banco.
class BankCustomerChurnValidador:
    def __init__(self, queryvalid):
        
        # Inicializa variaveis 
        self.__body      = queryvalid;
        self.__mensagem   = ""
        
        # Efetua validação
        self.__validar()
        
    @property
    def mensagemvalidador(self):
        return self.__mensagem
    
    def __validar(self):
        
        # valida campos independente da operação    
        if not Util.get_str_tamanho_valido(self.__body.client_name, 1, 20):
            self.__mensagem = "Nome do cliente não informado ou com quantidade de caracteres menor que 3 ou maior que 20."        
        elif not Util.get_numero_valido(self.__body.credit_score):
            self.__mensagem = "Conteúdo do campo Pontuação de crédito deve ser numérico."
        elif self.__body.credit_score < 0 or  self.__body.credit_score > 5000:
            self.__mensagem = "Pontuação de crédito informado não é válido."    
        elif self.__body.country not in ("Alemanha", "Espanha" ,"França"):
            self.__mensagem = "País de residência deve ser Alemanha, Espanha ou França."              
        elif self.__body.gender not in ("Masculino", "Feminino"):
            self.__mensagem = "Gênero dever ser masculino ou feminino."              
        elif not Util.get_numero_valido(self.__body.age):
            self.__mensagem = "Conteúdo do campo idade deve ser numérico."              
        elif self.__body.age < 10 or  self.__body.age > 150:
            self.__mensagem = "Idade informada não é valida."                          
        elif not Util.get_numero_valido(self.__body.tenure):
            self.__mensagem = "Conteúdo do campo tempo de conta bancária em anos deve ser numérico."              
        elif self.__body.tenure <= 0 or  self.__body.tenure > 120:
            self.__mensagem = "Tempo de conta bancária em anos informado não é valido."                          
        elif not Util.get_numero_valido(self.__body.balance):
            self.__mensagem = "Conteúdo do campo saldo da conta bancária deve ser numérico."              
        elif self.__body.balance < 0:
            self.__mensagem = "Saldo da conta bancária informado não é valido."                          
        elif not Util.get_numero_valido(self.__body.products_number):
            self.__mensagem = "Conteúdo do campo quantidade de produtos no banco deve ser numérico."              
        elif self.__body.products_number < 0:
            self.__mensagem = "Quantidade de produtos no banco informado não é valido."                          
        elif not Util.get_numero_valido(self.__body.credit_card):
            self.__mensagem = "Conteúdo do campo indicador detentor de cartão de crèdito deve ser numérico."              
        elif self.__body.credit_card < 0 or self.__body.credit_card > 1:
            self.__mensagem = "Indicador de detentor de cartão de crèdito informado deve conter o valor 0 ou 1."                          
        elif not Util.get_numero_valido(self.__body.active_member):
            self.__mensagem = "Conteúdo do campo cliente ativo deve ser numérico."              
        elif self.__body.active_member < 0 or  self.__body.active_member > 1:
            self.__mensagem = "Cliente ativo informado deve conter o valor 0 ou 1."                          
        elif not Util.get_numero_valido(self.__body.estimated_salary):
            self.__mensagem = "Conteúdo do campo salário estimado deve ser numérico."              
        elif self.__body.estimated_salary < 0:
            self.__mensagem = "Salário estimado informado não é valido."                          
              
       

            
        
       