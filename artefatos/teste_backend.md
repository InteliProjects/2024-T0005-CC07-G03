Este documento detalha os procedimentos e resultados dos testes realizados na API hospedada em uma instância EC2 da Amazon Web Services (AWS). Nosso objetivo principal é garantir a funcionalidade e a integridade do sistema, abrangendo uma variedade de métodos de requisição, incluindo GET, POST, PUT e DELETE.

Os testes foram conduzidos com o intuito de validar o comportamento da API em diferentes cenários de requisição, assegurando que as operações CRUD (Create, Read, Update, Delete) sejam executadas corretamente, que os dados sejam processados de forma adequada e que as respostas retornadas estejam em conformidade com as especificações da API.

# Requisições:

## **GET:**

- Rota: [http://34.238.83.102:5000/api/pessoa/1](http://34.238.83.102:5000/api/pessoa/1)
    

Essa Rota é responsável por retornar as informações de um único usuário.

| Parâmetro | Valor |
| --- | --- |
| id_pessoa | 1 |

- Retorno:
    

<img src="https://content.pstmn.io/f4686a40-ed87-455f-902a-3713ab43e559/aW1hZ2UucG5n" alt="Retorno%20da%20requisição%20GET" width="1816" height="853">

## **Post:**

- Rota: [http://34.238.83.102:5000/api/pessoa](http://34.238.83.102:5000/api/pessoa/1)
    

Essa Rota é responsável por criar um usuário.

- Body:
    

``` json
{
    "nome": "Henrique Burle",
    "email": "Henrique.burle@sou.inteli.edu.br",
    "cpf": "54523803476",
    "numero": "75981246307",
    "tipo": "pre-pago",
    "valor": 79.90,
    "consumo": 10
}

 ```

- Retorno:
    

<img src="https://content.pstmn.io/9763f627-3bca-40f2-9c9a-4c5b5e93e502/aW1hZ2UucG5n" alt="Retorno%20da%20requisição%20POST" width="617" height="249">

## **Put:**

- Rota: [http://34.238.83.102:5000/api/pessoa/12](http://34.238.83.102:5000/api/pessoa/6)
    

Essa Rota é responsável por atualizar as informações de um usuário.

| **Parâmetro** | **Valor** |
| --- | --- |
| id_pessoa | 6 |

- Body:
    

``` json
{
    "nome":"Yago Lopes",
    "email":"Yago.lopes@sou.inteli.edu.br"
}

 ```

- Retorno:
    

<img src="https://content.pstmn.io/143eff88-9ad8-4f91-a837-79af50c73ff0/aW1hZ2UucG5n" alt="Retorno%20da%20Requisição%20PUT" width="1828" height="637">

## **Delete:**

- Rota: [http://34.238.83.102:5000/api/pessoa/12](http://34.238.83.102:5000/api/pessoa/1)
    

Essa Rota é responsável por deletar um usuário.

| Parâmetro | Valor |
| --- | --- |
| id_pessoa | 12 |

- Retorno:
    

<img src="https://content.pstmn.io/96568a7b-781b-457a-b782-a611b6b13df5/aW1hZ2UucG5n" alt="Retorno%20da%20requisição%20DELETE" width="1828" height="896">