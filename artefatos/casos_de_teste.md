Esse documento especifica casos de teste para os requisitos funcionais

#### RF1: O usuário deve ser capaz de buscar dados mais atualizados por meio de um botão.

Objetivo: Garantir que o usuário possa atualizar seus dados com sucesso.

Pré-condição: O usuário está autenticado e visualizando a tela principal.

Procedimento de Teste:

1. O usuário clica no botão de atualizar dados na tela principal.

Resultado Esperado: O sistema busca e exibe os dados mais recentes do usuário.

Resultado Obtido: [Essa funcionalidade ainda está sendo implementada]

Pós-condição: Os dados na tela correspondem com os dados armazenados no banco RDS em tempo real.

#### RF2: O sistema deve ter uma função para consultar o saldo do cliente.

Objetivo: Verificar se o saldo do cliente é exibido corretamente.

Pré-condição: O usuário está autenticado.

Procedimento de Teste:

1. O usuário acessa a tela principal, que mostra o saldo.

Resultado Esperado: O saldo atual do usuário é exibido corretamente na tela.

Resultado Obtido: Uma vez logado e na tela principal, o saldo do usuário foi exibido corretamente.

Pós-condição: O usuário visualiza o saldo disponível em sua conta.

#### RF3: O sistema deve mostrar os dados de cadastro do usuário na tela inicial.

Objetivo: Confirmar que os dados de cadastro são exibidos na tela inicial após o login.

Pré-condição: O usuário está autenticado e na tela inicial.

Procedimento de Teste:

1. Verificar a exibição dos dados de cadastro do usuário (nome e telefone) na tela inicial.

Resultado Esperado: Os dados de cadastro do usuário são exibidos corretamente.

Resultado Obtido: Os dados foram exibidos corretamente, correspondendo a conta que foi autenticada.

Pós-condição: O usuário confirma a precisão dos seus dados de cadastro na tela inicial.

#### RF4: O usuário deve ser capaz de visualizar seu consumo de internet.

Objetivo: Assegurar que o usuário pode visualizar o consumo de dados de internet.

Pré-condição: O usuário está autenticado.

Procedimento de Teste:

1. O usuário acessa a seção de consumo de dados de internet.

Resultado Esperado: O consumo atual de internet é exibido, incluindo detalhes como gráficos de uso.

Resultado Obtido: O consumo foi mostrado corretamente, incluindo um gráfico circular mostrando quanto do total já foi utilizado.

Pós-condição: O usuário tem clareza sobre seu consumo de dados de internet.

#### RF5: O sistema deve ter autenticação antes de permitir o acesso do usuário.

Objetivo: Confirmar que o acesso às funcionalidades do sistema requer autenticação.

Pré-condição: O usuário não está autenticado.

Procedimento de Teste:

1. Tentar acessar qualquer funcionalidade protegida sem realizar o login.

Resultado Esperado: O sistema redireciona para a página de cadastro, impedindo o acesso.

Resultado Obtido: Ao tentar acessar o sistema sem login fomos redirecionados para a página de cadastro, confirmando o resultado esperado

Pós-condição: O acesso às funcionalidades do sistema está seguro atrás da autenticação.