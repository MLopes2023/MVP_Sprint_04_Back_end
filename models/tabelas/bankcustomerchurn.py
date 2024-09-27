from unicodedata    import numeric
from sqlalchemy     import Column, DateTime, Float, Integer, Numeric, String
from datetime       import datetime
from typing         import Union
from models.base    import Base

#Tabela predição da rotatividade do cliente no banco
class BankCustomerChurn(Base):
    
    __tablename__ = "bankcustomerchurn"

    id              = Column(Integer,           primary_key=True, autoincrement=True)
    client_name     = Column(String(20),        unique=True)
    credit_score    = Column(Integer,           nullable=False)
    country         = Column(String(10),        nullable=False)
    gender          = Column(String(10),        nullable=False)
    age             = Column(Integer,           nullable=False)
    tenure          = Column(Integer,           nullable=False)
    balance         = Column(Numeric(15, 2),    nullable=False)
    products_number = Column(Integer,           nullable=False)
    credit_card     = Column(Integer,           nullable=False)
    active_member   = Column(Integer,           nullable=False)
    estimated_salary= Column(Numeric(15, 2),    nullable=False)
    churn           = Column(Integer,           nullable=False)
    dtcadastro      = Column(DateTime,          nullable=False)
    
    # construtor
    def __init__(self,  client_name:str,    credit_score:int,           country:str,                    gender:str,     
                        age:int,            tenure:int,                 balance:float,                products_number:int, 
                        credit_card:int,    active_member:int,          estimated_salary:float,       churn:int,
                        dtcadastro:Union[DateTime, None] = None):
        """
        Inseri dados da predição de rotatividade de cliente no banco

        Arguments:
            id: Id do cliente 
            client_name: Nome do cliente
            credit_score: Pontuação de crédito
            country: País de residência (Alemanha, Espanha ou França)
            gender: Gênero (Feminino ou Masculino)
            age: Idade
            tenure: Há quantos anos tem conta bancária no banco
            balance: Saldo da conta
            products_number: Quantidade de produtos no banco
            credit_card: Indicador detentor de cartão de crèdito (1=sim ou 0=não)
            active_member: Cliente ativo (1=sim ou 0=não)
            estimated_salary: Salário estimado
            churn: Idicador se o cliente saiu do banco no período (1=sim ou 0=não)
            dtcadastro: Data/hora do cadastro
        """
        
        self.credit_score       = credit_score        
        self.client_name        = client_name
        self.country            = country
        self.gender             = gender
        self.age                = age
        self.tenure             = tenure
        self.balance            = balance
        self.products_number    = products_number
        self.credit_card        = credit_card
        self.active_member      = active_member
        self.estimated_salary   = estimated_salary
        self.churn              = churn
                
        if not dtcadastro:
            self.dtcadastro = datetime.now()
        else:
            self.dtcadastro = dtcadastro
 
    def to_dict(self):
        """
        Retorna dicionário do objeto bankcustomerchurn.
        """
        return{
            "id": self.id,
            "client_name": self.client_name,
            "credit_score": self.credit_score,
            "country": self.country,
            "gender": self.gender,
            "age": self.age,
            "tenure": self.tenure,
            "balance": self.balance,
            "products_number": self.products_number,
            "credit_card": self.credit_card,
            "active_member": self.active_member,
            "estimated_salary": self.estimated_salary,
            "churn": self.churn,
            "dtcadastro": self.dtcadastro,
        }

    def __repr__(self):
        """
        Retorna bankcustomerchurn em forma de texto.
        """
        return f"BankCustomerChurn( id={self.id},                         client_name={self.client_name},           credit_score={self.credit_score},\
                                    country={self.country},               gender={self.gender},                     age={self.age},\
                                    tenure={self.tenure},                 balance={self.balance},                   products_number={self.products_number},\
                                    credit_card={self.credit_card},       active_member={self.active_member},       estimated_salary={self.estimated_salary}\
                                    churn={self.churn},                   dtcadastro={self.dtcadastro})"            
    