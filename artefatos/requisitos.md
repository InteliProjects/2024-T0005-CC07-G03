# Requisitos Funcionais
Os requisitos funcionais descrevem ações que o sistema deve realizar ou que o usuário deve ser capaz de fazer, geralmente eles são focados no "o que" o sistema deve fazer

#### RF1: 
    O usuário deve ser capaz de buscar dados mais atualizados por meio de um botão.
#### RF2:
    O sistema deve ter uma função para consultar o saldo do cliente.
#### RF3:
    O sistema deve mostrar os dados de cadastro do usuário na tela inicial.
#### RF4:
    O usuário deve ser capaz de visualizar seu consumo de internet
#### RF5:
    O sistema deve ter autenticação antes de permitir o acesso do usuário.

# Requisitos Não Funcionais:
Os requisitos não funcionais descrevem como o sistema deve ser em aspectos de segurança, desempenho, confiabilidade, usabilidade, etc. Tais aspectos devem seguir a ISO25010.

#### RNF1:
    O tempo de resposta do sistema deve ser, em média, inferior a 3 segundos.
##### Plano de teste:
    Objetivo: Validar se o tempo de resposta do sistema está inferior a 3 segundos.
###### Metodologia:
    Utilizar uma ferramenta de automação de testes para realizar requisições ao sistema e medir o tempo de resposta.
    Realizar testes em diferentes cenários (ex: carga baixa, carga alta).
###### Critérios de Aceitação:
    O tempo de resposta médio do sistema deve ser inferior a 3 segundos em 90% dos casos.
    O tempo de resposta máximo do sistema não deve ultrapassar 5 segundos em nenhum caso.
#### RNF2:
    Os usuários devem conseguir se autenticarem utilizando seus repectivos CPF, número de telefone ou e-mail.
##### Plano de teste:
    Objetivo: Validar se os usuários conseguem se autenticar utilizando seus respectivos CPF, número de telefone ou e-mail.
###### Metodologia:
    Realizar testes manuais de autenticação com diferentes combinações de CPF, número de telefone e e-mail.
    Testar a autenticação em diferentes cenários (ex: usuário inexistente).
###### Critérios de Aceitação:
    O usuário deve conseguir se autenticar com sucesso utilizando seus dados corretos.
    O sistema deve apresentar mensagens de erro claras e informativas em caso de falha na autenticação.
#### RNF3:
    A interface do sistema deve ser de fácil entendimento e utilização.
##### Plano de teste:
    Objetivo: Validar se a interface do sistema é de fácil entendimento e utilização.
###### Metodologia:
    Realizar testes de usabilidade com usuários reais do sistema.
Observar a interação dos usuários com o sistema e identificar pontos de melhoria.
    Coletar feedback dos usuários sobre a usabilidade da interface.
###### Critérios de Aceitação:
    A interface do sistema deve ser intuitiva e fácil de usar.
    Os usuários devem conseguir realizar as tarefas desejadas sem dificuldades.
    O sistema deve apresentar mensagens de ajuda e instruções claras para os usuários.
#### RNF4:
    O banco de dados deve ser criado na AWS RDS e deve ter um delay de aproximadamente 30 segundos, para simular os bancos legados da Vivo.
##### Plano de teste:
    Objetivo: Validar se o banco de dados está funcionando de acordo com o esperado.
###### Metodologia:
    Utilizar uma ferramenta de monitoramento de desempenho para verificar o tempo de resposta das queries ao banco de dados.
    Realizar testes de carga no banco de dados para avaliar sua capacidade de lidar com um grande número de requisições.
###### Critérios de Aceitação:
    O tempo de resposta das queries ao banco de dados deve ser inferior a 30 segundos em 90% dos casos.
    O banco de dados deve ser capaz de lidar com um grande número de requisições sem apresentar falhas
#### RNF 5
    O sistema deve estar disponível 99.9% do tempo.
##### Plano de teste:
    Objetivo: Validar se o sistema está disponível 99.9% do tempo.
###### Metodologia:
    Utilizar uma ferramenta de monitoramento de tempo de atividade para monitorar a disponibilidade do sistema.
    Coletar dados sobre o tempo de atividade do sistema por um período significativo de tempo (ex: um mês).
###### Critérios de Aceitação:
    O sistema deve estar disponível 99.9% do tempo.
    O tempo de inatividade do sistema não deve ultrapassar o limite especificado.
#### RNF 6
    O sistema deve ser elástico para suportar picos de demanda.
##### Plano de teste:
    Objetivo: Validar se o sistema é capaz de suportar picos de demanda.
###### Metodologia:
    Utilizar uma ferramenta de teste de carga para simular um grande número de requisições simultâneas ao sistema.
    Monitorar o desempenho do sistema durante a realização dos testes.
    Verificar se o sistema consegue escalar horizontalmente para acomodar o aumento da carga.
###### Critérios de Aceitação:
    O sistema deve manter o tempo de resposta adequado mesmo sob alta carga.
    O sistema não deve apresentar falhas ou erros durante a realização dos testes.
    O sistema deve ser capaz de escalar horizontalmente para aumentar sua capacidade.

