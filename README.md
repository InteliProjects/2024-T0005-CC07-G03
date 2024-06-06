<table>
<tr>
<td>
<a href= "https://www.vivo.com.br/"> <img src="artefatos/img/vivo-logo.png" alt="vivo.com.br" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="artefatos/img/inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="50%"></a>
</td>
</tr>
</table>
 
# Introdução

Este é um dos repositórios do projeto de alunos do Inteli em parceria com a VIVO no 1º semestre de 2024. Este projeto está sendo desenvolvido por alunos do Módulo 7 do curso de Ciência da Computação.


# Projeto: *Otimização de consultas em banco de dados utilizando AWS e Cache*

# Grupo: Live

# Integrantes:

* <a href="https://www.linkedin.com/in/bruno-wasserstein/"> Bruno Wasserstein </a>
* <a href="https://www.linkedin.com/in/giuliano-bontempo/"> Giuliano bontempo </a>
* <a href="https://www.linkedin.com/in/henrique-burle/?originalSubdomain=br"> Henrique Burle </a>
* <a href="https://www.linkedin.com/in/marcelomaiaf/?originalSubdomain=br"> Marcelo Maia </a>
* <a href="https://www.linkedin.com/in/yago-phellipe/"> Yago Phellipe </a>


# Descrição

O projeto para a Vivo visa aprimorar a eficiência das consultas em seu banco de dados legado, utilizando a infraestrutura de nuvem da AWS e tecnologias de Cache para enfrentar desafios de escalabilidade e picos de demanda. Por meio da integração de Amazon RDS e Amazon ElastiCache, além da otimização de consultas, a iniciativa busca reduzir significativamente a latência, melhorando o acesso e a gestão dos dados sem comprometer sua segurança. Esta abordagem não apenas promete aprimorar a agilidade operacional da Vivo, mas também a capacidade de escalonar de forma flexível, adaptando-se às demandas dinâmicas do mercado.

# Configuração para o ambiente de desenvolvimento

## Requisitos

- AWS CLI configurado com as credenciais de acesso.
- Python versão atualizada instalada.
- Node versão mais atualizada instalada.


## Execução do Backend

Antes de iniciar o backend do projeto, é importante instalar todas as dependências Python necessárias listadas no arquivo requirements.txt. Este arquivo contém uma lista de todas as bibliotecas que seu projeto depende para funcionar corretamente.

Navegar até a pasta backend
```bash
cd g3/src/backend
```

Uma vez na pasta backend, execute o seguinte comando para instalar todas as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```


Para executar o backend do projeto, navegue até a pasta `backend` no terminal e execute o comando abaixo para iniciar a API em Python:

```bash
python run.py
```

Este comando iniciará o servidor backend de forma local.

## Execução do Frontend

Navegar até a pasta frontend
```bash
cd g3/src/frontend
```

Uma vez na pasta backend, execute o seguinte comando para instalar todas as dependências:

```bash
npm install --force
```


Para executar o frontend do projeto, ainda com a pasta `frontend` aberta no terminal execute o comando abaixo:

```bash
npm run dev
```

Este comando iniciará o servidor frontend de forma local.


# Tags

- SPRINT 1:  
  - Entendimento de Negócio;
  - Entendimento da Experiência do Usuário.
  - MVP com deploy
  - Requisitos funcionais e não funcionais
- SPRINT 2:
  - Criação de Redes e VPC
  - Arquitetura Corporativa;
  - Front-end.
  - Back-end.
  - Artigo (Versão 1)
- SPRINT 3:
  - Relatório técnico
  - Diagrama dos casos de uso
  - Diagramas UML
  - Artigo (Versão 2)
- SPRINT 4:
  - Testes do sistema;
  - Docker;
  - Kubernetes;
  - Filas;
  - Artigo (Versão 3)
  - Cache
- SPRINT 5:
  - Preparação para a entrega;
  - Artigo completo;
  - Apresentação Final;
  - Testes de usabilidade.
  - Cache finalizado

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">

<a property="dct:title" rel="cc:attributionURL">Grupo</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName">Inteli, Marcelo Maia, Yago Phellipe, Henrique Burle, Giuliano Bontempo, Bruno Wasserstein</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" rel="license noopener noreferrer" style="display:inline-block;">Application 4.0 International</a>.</p>
