from flask_openapi3                         import OpenAPI, Info, Tag
from flask                                  import redirect
from flask_cors                             import CORS
from http                                   import HTTPStatus

########################################################################################################
# Define constantes httpstatuscode
########################################################################################################

const_str_httpstatus_ok             = str(HTTPStatus.OK)
const_str_httpstatus_bad_request    = str(HTTPStatus.BAD_REQUEST)
const_str_httpstatus_conflict       = str(HTTPStatus.CONFLICT)
const_str_httpstatus_not_found      = str(HTTPStatus.NOT_FOUND)
const_value_httpstatus_ok           = HTTPStatus.OK
const_value_httpstatus_bad_request  = HTTPStatus.BAD_REQUEST
const_value_httpstatus_conflict     = HTTPStatus.CONFLICT
const_value_httpstatus_not_found    = HTTPStatus.NOT_FOUND

########################################################################################################
# Apresentação documentação API
########################################################################################################

info = Info(title="API Bank Customer Churn Prediction", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True) 

########################################################################################################
# Definição das tags
########################################################################################################

home_tag                = Tag(name="Documentação",  description="Documentação padrão: Swagger")
predicao_cliente_tag    = Tag(name="Rotatividade de Clientes no Banco",          description="Adição, remoção e visualização da predições de rotatividade de clientes no banco")

########################################################################################################
# Redireciona para para /openapi estilo padrão da documentação : swagger
########################################################################################################

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela para visualização estilo padrão de documentação swagger.
    """
    return redirect('/openapi/swagger')