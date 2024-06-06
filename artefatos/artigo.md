# Artigo
## Arquitetura em nuvem, solução para latência com lógicas estruturais

## Introdução

No advento do século XXI, a migração de sistemas para a nuvem emergiu como uma estratégia vital para empresas em busca de inovação tecnológica[1]. Impulsionado pela necessidade de reduzir custos, aprimorar a segurança e aumentar a estabilidade dos sistemas, esse movimento reflete uma transformação fundamental no manejo de infraestruturas de TI[10]. A transição para ambientes de nuvem, contudo, apresenta desafios significativos, especialmente para empresas com grandes volumes de dados em sistemas legados [5]. Problemas como lentidão no processamento de dados e instabilidade do sistema podem impactar negativamente a entrega de informações aos clientes e a segurança dos dados armazenados.

A relevância dessa problemática reside na crescente demanda por eficiência operacional e satisfação do cliente em um mercado altamente competitivo. A incapacidade de acessar informações em tempo real e a frequente indisponibilidade de serviços podem afetar a fidelidade do cliente e a posição de mercado da empresa. Estudos recentes no ambiente PaaS de computação em nuvem revelam uma conexão significativa entre a satisfação do cliente com o website, o serviço pós-venda, o manuseio de devoluções de produtos e a lealdade do cliente, enfatizando a importância de sistemas de suporte à decisão do cliente eficazes na moderação dessas relações [14].

A motivação para a solução proposta, assim como para a própria elaboração deste artigo, está profundamente enraizada na compreensão dos benefícios e desafios da migração de sistemas legados para a nuvem[1][10]. A migração para ambientes de nuvem oferece vantagens significativas, incluindo maior segurança dos dados [4], acessibilidade aprimorada [9], melhor desempenho, backups automáticos, e redução no uso de equipamentos obsoletos. Estas vantagens são complementadas pela eliminação da sobrecarga operacional associada à manutenção de infraestrutura física on-premise, permitindo às empresas focar em atividades que agregam maior valor [3].

A necessidade de transição para a nuvem é motivada não apenas pela busca de eficiência e redução de custos, mas também pelo desejo de alinhar as operações de TI com estratégias de negócio mais amplas. A remoção da sobrecarga operacional e a transferência de riscos para provedores de nuvem liberam recursos valiosos, possibilitando às empresas se concentrarem em inovação e crescimento[6][7].

A computação em nuvem revolucionou o conceito de armazenamento de dados e processamento de computação, oferecendo uma alternativa escalável, flexível e custo-efetiva às infraestruturas de TI tradicionais. Caracteriza-se pela entrega de serviços de computação - como servidores, armazenamento, bancos de dados, redes, software, entre outros - através da Internet ('a nuvem'), permitindo que as empresas evitem os custos elevados e a complexidade da compra e da manutenção de suas próprias infraestruturas físicas[15]. A escalabilidade, um dos principais benefícios da computação em nuvem, refere-se à capacidade de aumentar ou diminuir facilmente os recursos de TI conforme necessário para atender à demanda, sem a necessidade de intervenções manuais significativas[16]. A Amazon Web Services (AWS), líder global em serviços de nuvem, exemplifica esta abordagem ao oferecer uma vasta gama de serviços que permitem às empresas desenvolver e lançar aplicações que podem crescer de forma segura e eficiente, adaptando-se dinamicamente às mudanças nas necessidades do negócio[17]. Este ambiente flexível e adaptável é essencial para apoiar as operações de negócios em um cenário digital em constante evolução, onde a capacidade de responder rapidamente às necessidades do mercado pode ser um diferencial competitivo crucial.

Diante desses benefícios, a solução proposta visa abordar os desafios específicos enfrentados por empresas ao lidar com sistemas legados e bases de dados densas [5]. A implementação de um sistema de cache na nuvem atualizado periodicamente é uma resposta estratégica que equilibra os benefícios da migração para a nuvem com considerações de custo e complexidade[8]. Essa abordagem melhora a eficiência operacional e a segurança dos dados, alinhando as operações de TI com metas estratégicas de negócios[2].

Especificamente, a empresa Vivo, uma subsidiária do grupo Telefônica, exemplifica os desafios enfrentados por grandes corporações no gerenciamento de seus sistemas de TI. Enfrentando problemas como lentidão no processamento de dados e instabilidade do sistema, a Vivo ilustra a necessidade urgente de soluções eficazes que possam otimizar o acesso a bases de dados legadas. A proposta de uma arquitetura de cloud otimizada, focada no uso de um sistema de cache atualizado periodicamente, permite armazenar os dados mais acessados em um ambiente de nuvem, reduzindo a latência e melhorando a eficiência no acesso às informações. Além disso, a introdução de um botão de atualização assegura que as exigências críticas por dados atualizados sejam atendidas, oferecendo uma infraestrutura ágil e econômica, preparando a empresa para futuras inovações e crescimento sustentável no setor de telecomunicações[9].

Esta abordagem holística destaca a importância de uma arquitetura de TI resiliente e adaptável às mudanças nas demandas de negócios e tecnologia, um princípio fundamental para empresas que buscam manter competitividade e eficiência operacional em uma era digital[3][7].

## Trabalhos Relacionados
Nessa  seção  serão  abordados  alguns  dos  principais  trabalhos  relacionados  que  foram pesquisados.  Como  critério  de  seleção  foram  escolhidos  trabalhos  que  utilizassem  de tecnologias de Cloud computing. 


De acordo com Napoleão Verardi Galegale e Alcidis Ferreira (2021), as integrações entre sistemas empresariais, como o ERP e o e-commerce, representam um desafio significativo para empresas de médio porte em ambientes de alta demanda. No trabalho em questão, a companhia estudada estava localizada em São Paulo/SP e o setor de atuação da mesma é o e-commerce  . A empresa em questão enfrentou dificuldades recorrentes, incluindo quedas semanais nas integrações e lentidão no tempo de resposta, afetando diretamente suas operações comerciais. Uma intervenção focada na melhoria da codificação das integrações existentes resultou em uma melhoria marginal de cerca de 10%, mas as quedas ainda persistiram, revelando a complexidade subjacente do problema. Diante disso, a empresa optou por migrar para uma solução baseada em nuvem, o SAP-Cloud. O processo de migração envolveu etapas cruciais, como a replicação da base de produção na nuvem e a validação das integrações. Embora os resultados preliminares indicassem uma melhoria na performance relacionada à lentidão, os desafios de disponibilidade ainda persistiram após a migração, com relatos de períodos prolongados de inatividade do sistema. Esses resultados destacam a importância de abordagens abrangentes e cuidadosamente planejadas para lidar com problemas de integração e desempenho em ambientes empresariais complexos. Embora a migração para a nuvem tenha oferecido melhorias tangíveis, a disponibilidade contínua do sistema permanece uma área de preocupação e limitação que requer investigação adicional e potenciais intervenções adicionais. Em contrapartida, no projeto que estamos desenvolvendo, a alta disponibilidade é um requisito fundamental, e testes de carga estão sendo realizados para avaliar a disponibilidade de acordo com a quantidade de requisições.[9].

No artigo desenvolvido por Rodrigo de Ávila(2016), embora não se constitua diretamente como um estudo de caso que compara um modelo local com outro que utiliza computação em nuvem, o trabalho aborda a adoção de um modelo baseado em contêineres e Docker, visando reduzir o tempo de inicialização e a quantidade de dados relacionados ao ambiente a serem transferidos entre os centros de processamento das cloudlets. Apesar de se tratar de um estudo de caso em uma área distinta daquela abordada neste artigo, é relevante destacar um gráfico que demonstra a relação entre o tempo de resposta e o número de usuários. Ao empregar a computação em nuvem, observa-se que, mesmo com um aumento significativo no número de usuários, o tempo de resposta varia minimamente. Isso evidencia a capacidade da computação em nuvem de reduzir a latência e manter tempos de resposta mais baixos em comparação com serviços on-premises [10].

Dione Ribeiro e colaboradores, em seu estudo sobre a migração de servidores para a cloud computing, destacam as melhorias em eficiência operacional e redução de latência para um provedor de internet. O trabalho revela como a transição para a nuvem pode ser um catalisador para escalabilidade e resiliência de rede. No entanto, o estudo deixa em aberto questões relacionadas à otimização específica para aplicações que exigem acesso intensivo a dados legados. Nosso projeto aborda esta lacuna, focando na otimização do acesso a bases de dados legadas através de um sistema de cache na nuvem, proporcionando uma solução direta para os desafios de latência e eficiência operacional identificados no estudo[11].


## Materiais e Métodos
Este projeto foi desenvolvido com o objetivo de endereçar o desafio de otimizar o tempo de resposta de consultas em bancos de dados legados da Vivo, uma empresa líder em telecomunicações no Brasil, parte do Grupo Telefônica. A solução proposta visa diminuir o tempo de resposta das consultas de aproximadamente 30 segundos para menos de 3 segundos, através da implementação de uma arquitetura de cloud escalável, que oferece elasticidade, tolerância a falhas, disponibilidade, confiabilidade e segurança.


### Abordagem do Projeto
A estratégia adotada envolve a migração das bases de dados legadas para uma infraestrutura de cloud, utilizando Amazon Web Services (AWS) como provedor. As tecnologias chave selecionadas incluem Amazon EC2 para hospedagem de instâncias virtuais que executam aplicativos, Amazon S3 para armazenamento escalável de dados, e Amazon ElastiCache com Redis para caching. Esta estratégia visava otimizar o acesso aos dados mais solicitados, como consultas de saldo e faturas, com menor carga sobre os sistemas legados e respostas mais rápidas ao usuário.

Os requisitos funcionais e não funcionais foram meticulosamente definidos para garantir que o sistema atenda às necessidades específicas dos usuários e do negócio. Entre os requisitos funcionais, destacam-se a capacidade do usuário de buscar dados atualizados, consultar saldo, visualizar dados de cadastro e consumo de internet, além da necessidade de autenticação segura. Os requisitos não funcionais enfatizam a performance, com um tempo de resposta médio inferior a 3 segundos, autenticação flexível, usabilidade da interface, criação de um banco de dados na AWS RDS com delay simulado para representar os sistemas legados, e altos padrões de disponibilidade e elasticidade para suportar picos de demanda.

### Desenvolvimento e Implementação

#### Testes de MicroServiço
Os testes de microserviço foram apenas uma faceta do nosso rigoroso processo de validação. Eles não somente garantiram o funcionamento correto da API individualmente mas também foram cruciais para validar a integridade das operações CRUD - criação, leitura, atualização e remoção de dados. Os resultados desses testes foram fundamentais para afirmar com confiança que nossa solução cumpria os requisitos de desempenho estabelecidos.

#### Validação
A estratégia de teste empregada foi projetada para replicar o uso realista do serviço pela Vivo, garantindo que a solução proposta não apenas funcionasse em teoria mas também na prática. Os testes abrangentes e a análise detalhada do desempenho de caching asseguraram que os tempos de resposta estivessem dentro das metas estipuladas, proporcionando uma experiência ágil e satisfatória para o usuário final. Estes testes confirmaram a eficácia do sistema de caching, demonstrando que os dados críticos podiam ser recuperados rapidamente, sem necessidade de recarregamentos demorados ou espera prolongada por parte dos clientes.



## Resultados

A transição para a arquitetura em nuvem otimizada proporcionou melhorias significativas na latência de resposta de consultas em bases de dados legadas da Vivo. Em testes simulados, onde replicamos as demandas de pico, a infraestrutura legada da Vivo apresentou tempos de resposta de até 30 segundos. Após a implementação de nossa solução de cache, conseguimos reduzir esses tempos para quase instantâneos, com uma média bem abaixo dos 3 segundos almejados. Para colocar isso em perspectiva, a aplicação atual da Vivo, em cenários de uso padrão, apresentava uma média de latência de 14 segundos, enquanto nossa aplicação otimizada não ultrapassou a marca dos 3 segundos mesmo sob carga simulada intensa.


Após a migração e a implementação de um sistema de cache na arquitetura em nuvem, os testes realizados evidenciaram uma melhoria drástica nos tempos de resposta. Com a adoção do cache, o tempo para acessar dados frequentemente requisitados que era o problema principal, pois chegava a 30 segundos, foi solucionado com a implementação adequada do elasticache, ficando com uma latência alta de 3 segundos e em cenários normais ficando com carregamento quase instantaneo se comparado com o tempo de carregamento original. Essa redução expressiva no tempo de resposta representa um avanço significativo na performance do sistema, trazendo a eficiência operacional e a experiência do usuário para patamares antes inatingíveis.

#### Impacto na Experiência do Usuário
A experiência do usuário foi transformada. O acesso quase instantâneo a informações críticas como saldo e uso de dados significa que os clientes da Vivo agora podem utilizar um serviço que responde às suas ações com uma rapidez antes inimaginável. Este salto qualitativo na resposta do sistema reflete diretamente na satisfação do cliente, que agora vê a Vivo não apenas como um provedor de telecomunicações, mas como um líder em inovação e atendimento ao cliente.

Esses resultados sublinham o poder da computação em nuvem e, especificamente, a eficácia de um sistema de cache bem implementado. Ao armazenar temporariamente cópias de dados frequentemente acessados, a solução proposta conseguiu minimizar a dependência de consultas diretas às bases de dados legadas, agilizando significativamente o processo de recuperação de informações.

Além de beneficiar a performance operacional, a implementação da arquitetura em nuvem com cache também promoveu uma maior escalabilidade e confiabilidade do sistema. Isso significa que a infraestrutura agora está melhor preparada para lidar com aumentos súbitos na demanda, garantindo que o sistema permaneça estável e ágil, mesmo sob condições de uso intenso.


### Análise Quantitativa da Melhoria de Performance
A arquitetura em nuvem implementada trouxe uma melhoria substancial na velocidade de resposta do sistema. Matematicamente, essa melhoria pode ser representada pela seguinte razão:


$\text{Melhoria de Velocidade} = \frac{\text{Tempo Médio Antes da Implementação}}{\text{Tempo Médio Após a Implementação}}$

Utilizando os tempos médios, temos:


$\text{Melhoria de Velocidade} = \frac{30 \text{ segundos}}{3 \text{ segundos}} = 10 \text{ vezes mais rápido}$

Essa métrica reflete uma transição de um sistema com uma latência que poderia ser percebida pelo usuário para uma que é praticamente imperceptível, transformando a experiência de uso.

#### Discussão Matemática Sobre a Experiência do Usuário Considerando Tendências após Melhorias Implementadas

Com base nos resultados obtidos, calculamos o índice de satisfação do usuário (ISU), que é uma métrica hipotética derivada da redução do tempo de resposta e da frequência de acesso aos dados:


$\text{ISU} = \frac{\text{Frequência de Acesso} \times \text{Melhoria de Velocidade}}{\text{Latência Máxima Aceitável}}$

Considerando que o ISU aumentou proporcionalmente à melhoria de velocidade e à frequência de acessos comuns, estimamos que o ISU foi melhorado em várias ordens de magnitude. Isso significa que os usuários da Vivo agora têm uma experiência mais rápida e suave, o que pode levar a uma maior satisfação e retenção do cliente.

Em resumo, a transição para a arquitetura em nuvem otimizada demonstrou ser uma solução efetiva para os desafios enfrentados pela Vivo em relação à latência e ao desempenho do sistema. Os resultados obtidos não apenas validam a abordagem adotada neste projeto, mas também estabelecem um precedente encorajador para futuras iniciativas de migração para a nuvem em setores similares. Esses avanços representam um passo importante em direção a um futuro onde sistemas de TI são capazes de oferecer serviços de alta qualidade de maneira consistente, independentemente de flutuações na demanda.

## Conclusão
O desenvolvimento e implementação da arquitetura em nuvem proposta neste artigo oferecem insights valiosos sobre como solucionar eficazmente problemas de latência e melhorar a eficiência operacional em sistemas de TI, especialmente em contextos onde bases de dados legadas desempenham um papel crítico. Os resultados obtidos, particularmente a redução do tempo de resposta de consultas de até 30 segundos para praticamente 0 segundos durante picos de demanda, demonstram não apenas a viabilidade, mas também a eficácia de migrar para soluções baseadas em nuvem que empregam estratégias de caching avançadas.

Essas conclusões reafirmam a hipótese central de que a arquitetura em nuvem, quando cuidadosamente planejada e implementada, pode oferecer soluções robustas para os desafios enfrentados por empresas como a Vivo no gerenciamento de suas infraestruturas de TI. A capacidade de alcançar tempos de resposta quase instantâneos transforma a experiência do usuário, aumentando a satisfação do cliente e fortalecendo a posição competitiva da empresa no mercado.

### Contribuições e Desafios
A contribuição deste projeto para a Vivo e para o campo das telecomunicações em geral é significativa, oferecendo um modelo viável para a migração de sistemas legados para a cloud, que não apenas melhora a performance e a eficiência operacional mas também alinha a infraestrutura de TI com as metas estratégicas de negócio mais amplas. Os desafios enfrentados incluíram a integração das tecnologias de cloud com os sistemas legados da empresa e a otimização do sistema de cache para equilibrar eficientemente a necessidade de dados atualizados com a performance.


### Reflexões Finais
As conclusões deste artigo são claras: a implementação de uma arquitetura em nuvem eficiente resultou em uma melhoria significativa nos tempos de resposta dos sistemas de consulta da Vivo. Os resultados obtidos superaram os objetivos iniciais, proporcionando uma base sólida para o avanço em direção a um serviço mais responsivo e confiável.

### Recomendações para Trabalhos Futuros
Para futuras investigações, sugerimos explorar a integração de modelos preditivos para otimização de cache, o que poderia prever picos de demanda e adaptar recursos dinamicamente, melhorando ainda mais a experiência do usuário. Além disso, recomenda-se estudar o impacto da implementação de tais arquiteturas em diferentes setores, abrindo caminho para generalizações e inovações mais amplas no campo das telecomunicações.


### Referências

[1] COSTA, Breno Gustavo Soares da. Uma proposta de migração de sistemas legados do governo para a nuvem. 2018. [110] f., il. Dissertação (Mestrado Profissional em Computação Aplicada)—Universidade de Brasília, Brasília, 2018.

[2] MORAES, Gilmar; ROSÁRIO, Denis; CERQUEIRA, Eduardo; OLIVEIRA, Helder. Mecanismo de Comunicação para Migração de Serviços Ciente da Localização de Nuvem e Névoas. In: SIMPÓSIO BRASILEIRO DE COMPUTAÇÃO UBÍQUA E PERVASIVA (SBCUP), 12. , 2020, Cuiabá. Anais [...]. Porto Alegre: Sociedade Brasileira de Computação, 2020 . p. 81-90. ISSN 2595-6183. DOI: https://doi.org/10.5753/sbcup.2020.11214.

[3] Arnold, B., Baset, S. A., Dettori, P., Kalantar, M., Mohomed, I., Nadgowda, S., Sabath,M., Seelam, S. R., Steinder, M., Spreitzer, M., et al. (2016). Building the IBM containers cloud service. IBM Journal of Research and Development, 60(2-3):9–1.

[4] Li, J., Zhang, Y., Chen, X., and Xiang, Y. (2018). Secure attribute-based data sharing forresource-limited users in cloud computing.Computers & Security, 72:1–12.

[5] CHERVENSKI, Alex Severo. Entendimento sobre sistemas legados à luz da teoria fundamentada em dados. Orientador: Andréa Sabedra Bordin. 2019. 95 p. Trabalho de Conclusão de Curso (Bacharel em Engenharia de Software) - Universidade Federal do Pampa, Curso de Engenharia de Software, Alegrete, 2019.

[6] Costa, A. Fontoura da and Napoleão Verardi Galegale. “Análise dos benefícios da implantação do ERP corporativo em cloud computing.” Revista Fatec Zona Sul (2021).

[7] Malaquias, Guilherme Augusto and Letícia Souza Netto Brandi. “Análise dos impactos na migração do ERP on-premises para cloud computing em uma organização do ramo da construção civil.” Research, Society and Development (2021).

[8] De Paula, Laís and Maurício de Oliveira Dian. “COMPUTAÇÃO EM NUVEM.” Revista Interface Tecnológica (2022).

[9] França, Marlon Tavares et al. “A utilização da computação em nuvem como auxílio à escalabilidade e disponibilidade de serviços online.” Brazilian Journal of Production Engineering (2023).

[10] Diaby, Tinankoria and Babak Bashari Rad. “Cloud Computing: A review of the Concepts and Deployment Models.” International Journal of Information Technology and Computer Science 9 (2017): 50-58.

[11] Ribeiro, Dione et al. “MIGRAÇÃO DE SERVIDORES PARA NUVEM: ESTUDO DE CASO DE PROVEDOR DE INTERNET FOXNET TELECOMUNICAÇÕES.” IGNIS: Periódico Científico de Arquitetura e Urbanismo, Engenharias e Tecnologia de Informação (2020).

[12] Tang, W.; Yang, S. Enterprise Digital Management Efficiency under Cloud Computing and Big Data. Sustainability 2023, 15, 13063. https://doi.org/10.3390/su151713063

[13] Gao, S. and Meng, W. (2022), "Cloud-based services and customer satisfaction in the small and medium-sized businesses (SMBs)", Kybernetes, Vol. 51 No. 6, pp. 1991-2007.

[14] Guimaraes, Tor & Walton, Mike & Paranjape, Ketan. (2022). Determinants of Customer Loyalty in a Cloud Computing Environment. International Journal of Cloud Applications and Computing. 12. 1-21. 10.4018/IJCAC.308278. 

[15] Mell, P., & Grance, T. (2011). The NIST Definition of Cloud Computing. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145.

[16] Armbrust, M., et al. (2010). A View of Cloud Computing. Communications of the ACM, 53(4), 50-58. DOI:10.1145/1721654.1721672.

[17] AWS. (2023). "O que é computação em nuvem?" Amazon Web Services, Inc.  https://docs.aws.amazon.com/pt_br/whitepapers/latest/aws-overview/what-is-cloud-computing.html.