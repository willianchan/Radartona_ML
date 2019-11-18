# Milênio Bus - Radartona_ML
### Apresentação
Esse repositório consiste no tratamento e modelagem de dados para predição dos datasets fornecidos na Radartona, assim como todos os scripts auxiliares.

Foi desenvolvido um modelo capaz de predizer a velocidade de uma via por meio da coleta dos dados dos radares espalhados por São Paulo.

## Instalação no servidor

```bash
git clone https://github.com/willianchan/Radartona_ML.git

cd Radartona_ML

sudo docker build -t api_predict .

sudo docker run --rm -it -d -p 80:80 --name api_predict api_predict
```

## Bases utilizadas

* base_radares
* trajetos
* OpenWeather

## Metodologia

O tratamento dos dados se deu pelo cruzamento da base **trajetos**, na qual foi possível obter os ids dos radares, datas e velocidades dos carros com **base_radares** no qual foi possível obter a velocidade limite da via, além da base **OpenWeather** na qual foi possível obter o índice de chuva em datas específicas. 

## Treinamento

O treinamento do modelo foi realizado em **python** a partir da biblioteca **sklearn**.

O treinamento é detalhado no seguinte Notebook [Jupyter de Treinamento](https://github.com/willianchan/Radartona_ML/blob/master/MachineLearning/ModeloPredi%C3%A7%C3%A3o.ipynb)

## Modelo

O modelo foi gerado e salvo em formato pickle(.pkl)

## Documentação

A aplicação está documentada em OpenAPI 3.0 - [Documentação](https://app.swaggerhub.com/apis-docs/willianchan/API_Milenio_Bus_Radartona_Predicao/1.0.0-oas3)
