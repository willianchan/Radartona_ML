from flask import Flask, request, jsonify
import _pickle as cPickle
from sklearn.ensemble import RandomForestClassifier

with open('./modelo_rl.pkl', 'rb') as fid:
    modelo = cPickle.load(fid)

app = Flask(__name__)

@app.route('/')
def hello():
    return "bem vindo a API de predicao"

@app.route('/predict')
def predict():
    id_radar = int(request.args.get('id_radar'))
    ano = int(request.args.get('ano'))
    mes = int(request.args.get('mes'))
    dia = int(request.args.get('dia'))
    hora = int(request.args.get('hora'))
    minuto = int(request.args.get('minuto'))
    velocidade_maxima = int(request.args.get('velocidade_maxima'))
    chuva = int(request.args.get('chuva'))

    result = modelo.predict([[id_radar,ano,mes,dia,hora,minuto,velocidade_maxima,chuva]])[0]
    #resultado sai em decimos de metros por segundo
    #convertendo para km/h
    result = result*3.6/10

    return jsonify({"velocidade":result})

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')