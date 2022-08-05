# Uma API simples feita em FastAPI para trabalhar com grafos

A API é capaz de salvar, recuperar informações, consultar todos os caminhos entre dois vértices dado um valor máximo de paradas e calcula o menor caminho entre dois vértices

Os dados são salvos em um banco de dados PostgreSQL, utilizando docker para o ambiente de desenvolvimento


# Utilização
* Comandos:
  * Iniciar containers : docker compose up --build
  * Pausar containers : docker compose down
  * Remover dados persistidos : sudo chown -R <seu_user> pgdata && rm -rf pgdata (por padrão são protegidos)
    * Execute esse comando caso tenha algum problema de permission denied na pasta pgdata ao fazer o build
  * Executar testes : docker exec api_container pytest test
* Administrar banco de dados:
  * Para acessar o banco com o pgadmin acesse : http://localhost:5050/
    * user : admin@gmail.com
    * senha: admin
  * Dentro de pgadmin crie um novo servidor :
    * hostname/addres : postgresql
    * senha : admin
      * Aparecerar o banco fastapi, onde há a persistência dos graphs

## Mais detalhes do funcionamento de cada endpoint estão disponíveis abaixo.


### Salvar Grafo

Esse endpoint deverá receber as arestas de um grafo e salva-las em um banco de dados para consultas posteriores.
* Endpoint: `http://localhost:8080/graph`
* HTTP Method: POST
* HTTP Success Response Code: CREATED (201)
* Contract:
  * Request payload

```javascript
{​
  "data": [
    {​
      "source": "A", "target": "B", "distance": 6
    }​,
    {​
      "source": "A", "target": "E", "distance": 4
    }​,
    {​
      "source": "B", "target": "A", "distance": 6
    }​,
    {​
      "source": "B", "target": "C", "distance": 2
    }​,
    {​
      "source": "B", "target": "D", "distance": 4
    }​,
    {​
      "source": "C", "target": "B", "distance": 3
    }​,
    {​
      "source": "C", "target": "D", "distance": 1
    }​,
    {​
      "source": "C", "target": "E", "distance": 7
    }​,
    {​
      "source": "D", "target": "B", "distance": 8
    }​,
    {​
      "source": "E", "target": "B", "distance": 5
    }​,
    {​
      "source": "E", "target": "D", "distance": 7
    }​
  ]
}​
```
  * Response payload
```javascript
{​
  "id" : 1,
  "data":[
    {​
      "source": "A", "target": "B", "distance":6
    }​,
    {​
      "source": "A", "target": "E", "distance":4
    }​,
    {​
      "source": "B", "target": "A", "distance":6
    }​,
    {​
      "source": "B", "target": "C", "distance":2
    }​,
    {​
      "source": "B", "target": "D", "distance":4
    }​,
    {​
      "source": "C", "target": "B", "distance":3
    }​,
    {​
      "source": "C", "target": "D", "distance":1
    }​,
    {​
      "source": "C", "target": "E", "distance":7
    }​,
    {​
      "source": "D", "target": "B", "distance":8
    }​,
    {​
      "source": "E",  "target": "B", "distance":5
    }​,
    {​
      "source": "E", "target": "D", "distance":7
    }​
  ]
}​
```

### Recuperar Grafo
Esse endpoint deverá retornar um grafo previamente salvo no banco de dados. Se o grafo não existe, deverá retornar HTTP NOT FOUND.
* Endpoint: `http://localhost:8080/graph/<graphId>`
* HTTP Method: GET
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)
* Contract:
  * Request payload: none
  * Response payload

```javascript
{​
  "id" : 1,
  "data":[
    {​
      "source": "A", "target": "B", "distance": 6
    }​,
    {​
      "source": "A", "target": "E", "distance": 4
    }​,
    {​
      "source": "B", "target": "A", "distance": 6
    }​,
    {​
      "source": "B", "target": "C", "distance": 2
    }​,
    {​
      "source": "B", "target": "D", "distance": 4
    }​,
    {​
      "source": "C", "target": "B", "distance": 3
    }​,
    {​
      "source": "C", "target": "D", "distance": 1
    }​,
    {​
      "source": "C", "target": "E", "distance": 7
    }​,
    {​
      "source": "D", "target": "B", "distance": 8
    }​,
    {​
      "source": "E", "target": "B", "distance": 5
    }​,
    {​
      "source": "E", "target": "D", "distance": 7
    }​
  ]
}​
```
### Encontrar todas rotas disponíveis dado um vértice de origem e outro de destino em um grafo salvo anteriormente
Utilizando um grafo salvo anteriormente, esse endpoint deverá calcular todas as rotas disponíveis de um vértice de origem para outro de destino, dado um número máximo de paradas. Se não existirem rotas possíveis, o resultado deverá ser uma lista vazia. Se o parâmetro "maxStops" não for definido, você deverá listar todas as rotas possíveis. Se o grafo não existir, deverá retornar HTTP NOT FOUND.
Exemplo: No grafo (AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7), as possíveis rotas de A para C com máximo de 3 paradas seriam: ["ABC", "ADC", "AEBC"]
* Endpoint: `http://localhost:8080/routes/<graphId>/from/<town1>/to/<town2>?maxStops=<maxStops>`
* HTTP Method: POST
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)
* Contract:
  * Grafo salvo anteriormente
```javascript
{​
  "data":[
    {​
      "source": "A", "target": "B", "distance": 5
    }​,
    {​
      "source": "B", "target": "C", "distance": 4
    }​,
    {​
      "source": "C", "target": "D", "distance": 8
    }​,
    {​
      "source": "D", "target": "C", "distance": 8
    }​,
    {​
      "source": "D", "target": "E", "distance": 6
    }​,
    {​
      "source": "A", "target": "D", "distance": 5
    }​,
    {​
      "source": "C", "target": "E", "distance": 2
    }​,
    {​
      "source": "E", "target": "B", "distance": 3
    }​,
    {​
      "source": "A", "target": "E", "distance": 7
    }​
  ]
}​
```
  * Request payload: none
  * Response payload
```javascript
{​
  "routes": [
    {​
      "route": "ABC",
      "stops": 2
    }​,
    {​
      "route": "ADC",
      "stops": 2
    }​,
    {​
      "route": "AEBC",
      "stops": 3
    }​
  ]
}​
```

### Determinar a distância mínima entre dois vértices em um grafo salvo

Utilizando um grafo salvo anteriormente, esse endpoint deverá determinar a rota cuja distância seja a mínima possível entre dois vértices. Se os vértices de origem e destino forem iguais, o resultado deverá ser zero. Se não exitir rota possível entre as dois vértices, então o resultado deverá ser -1. Se o grafo não existir, deverá retornar HTTP NOT FOUND.
* Endpoint: `http://localhost:8080/distance/<graphId>/from/<town1>/to/<town2>`
* HTTP Method: POST
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)
* Contract:
  * Grafo salvo anteriormente
```javascript
{​
  "data":[
    {​
      "source": "A", "target": "B", "distance":6
    }​,
    {​
      "source": "A", "target": "E", "distance":4
    }​,
    {​
      "source": "B", "target": "A", "distance":6
    }​,
    {​
      "source": "B", "target": "C", "distance":2
    }​,
    {​
      "source": "B", "target": "D", "distance":4
    }​,
    {​
      "source": "C", "target": "B", "distance":3
    }​,
    {​
      "source": "C", "target": "D", "distance":1
    }​,
    {​
      "source": "C", "target": "E", "distance":7
    }​,
    {​
      "source": "D", "target": "B", "distance":8
    }​,
    {​
      "source": "E",  "target": "B", "distance":5
    }​,
    {​
      "source": "E", "target": "D", "distance":7
    }​
  ]
}​
```
  * Request payload: none
  * Response payload
```javascript
{​
  "distance" : 8,
  "path" : ["A", "B", "C"]
}​
```