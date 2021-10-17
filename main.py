from flask import Flask, request
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)

livroDeReceitas = [
    {
        "Titulo": "Bolo de Laranja",
        "Ingredientes":[
            "3 ovos",
            "Suco de 2 laranjas",
            "1 xícara (chá) de óleo",
            "2 xícaras (chá) de açúcar",
            "3 xícaras (chá) de farinha de trigo",
            "1 colher (sopa) de fermento em pó"
        ],
        "Modo de preparo": "Bata no Liquidificador ou na batedeira os ovos, o suco da laranja, o óleo, e o açúcar. Depois despeje em uma tigela e junte com a farinha e o fermento, bata tudo junto até a massa ficar homogênea. Depois colocar em uma assadeira com furo untada com manteiga e farinha e levar para o forno. Asse em forno médio, preaquecido, por cerca de 40 minutos, ou até dourar.",
        "Rendimento": "8 porções"
    },
    {
        "Titulo": "Bolo de Banana",
        "Ingredientes":[
            "2 xícaras de farinha de trigo",
            "2 ovos",
            "2 bananas",
            "1 xícara de açucar",
            "1 xícara de leite",
            "1 colher de fermento",
            "1 colher cheia de manteiga"
        ],
        "Modo de preparo": "Coloque os ovos, farinha de trigo, açúcar, leite, fermento e a manteiga no liquidificador. Deixe batendo por 2 minutos, enquanto isso corte as bananas em rodelas pequenas. Logo a seguir passe manteiga na forma, não é necessário a farinha de trigo, depois despeje a massa que está no liquidificador dentro da forma. Logo após acrescente as rodelas de banana em cima da massa e leve ao forno por 40 minutos.",
        "Rendimento": "10 porções"
    }
]

class Receitas(Resource):
    def get(self):
        return {"status": 200, "data": livroDeReceitas}

    def post(self):
        newReceita = json.loads(request.data)
        livroDeReceitas.append(newReceita)
        return {
            "status": 201,
            "message": "Created!",
            "newValue": newReceita
        }

class Receita(Resource):
    def get(self, indice):
        try:
            return livroDeReceitas[indice]
        except IndexError:
            mensagem = "O índice {} não foi encontrado no array".format(indice)
            return {
                "status": 404,
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido"
            return {
                "status": 400,
                "message": mensagem,
            }

    def put(self, indice):
        try:
            newReceita =json.loads(request.data)
            livroDeReceitas[indice] = newReceita
            return {
                "status": 200,
                "message": "Updated!",
                "newValue": newReceita
            }
        except IndexError:
            mensagem = "O índice {} não foi encontrado no array".format(indice)
            return {
                "status": 404,
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido"
            return {
                "status": 400,
                "message": mensagem,
            }

    def delete(self, indice):
        try:
            livroDeReceitas.pop(indice)
            return {
                "status": 204,
                "message": "Deleted!",
                "arrayAtual": livroDeReceitas
            }
        except IndexError:
            mensagem = "O índice {} não foi encontrado no array".format(indice)
            return {
                "status": 404,
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido"
            return {
                "status": 400,
                "message": mensagem,
            }

api.add_resource(Receitas, "/receitas/")
api.add_resource(Receita, "/receitas/<int:indice>")

if __name__ == '__main__':
    app.run(debug=True)

