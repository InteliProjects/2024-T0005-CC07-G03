

# Modelo do domínio(diagrama de classes)
O modelo de domínio abaixo representa um sistema de gerenciamento de contas para serviços de telecomunicações. Neste sistema, uma entidade fundamental é a classe Conta, que armazena informações básicas do cliente, como nome, e-mail, CPF e número de conta. Um cliente pode ter várias contas associadas a ele, cada uma identificada por um número exclusivo, mas compartilhando o mesmo CPF.

Existem dois tipos principais de contas representados no modelo: Prepago e Pospago. Ambos os tipos de conta são subclasses de Conta e herdam seus atributos básicos.

Para contas Prepago, o sistema registra o consumo total de dados da internet, o consumo atual e o saldo disponível. Essas informações permitem que o cliente gerencie seu uso de dados e recarregue sua conta conforme necessário.

Já para contas Pospago, o sistema registra apenas o consumo total de dados e o valor a ser cobrado pelo serviço prestado. Nesse caso, o cliente é faturado após o uso do serviço, em vez de pagar antecipadamente como no caso do plano pré-pago.

Essa estrutura de classes permite uma organização clara e eficiente das informações relacionadas às contas dos clientes, facilitando o gerenciamento dos serviços de telecomunicações oferecidos pela empresa.
```plantuml
@startuml
left to right direction
' classes
class Conta
class Prepago
class Pospago

' atributos conta
Conta : Nome : string
Conta : Email : string
Conta : CPF : string
Conta : Numero : string

' Atributos Prepago
Prepago : ConsumoTotal : int
Prepago : ConsumoAtual : int
Prepago : Valor : int
Prepago : Saldo : int

' Atributo Pospago
Pospago : Consumo : int
Pospago : Valor : int

' herança
Conta <|-- Prepago
Conta <|--  Pospago
@enduml


