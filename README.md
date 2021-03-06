## Apresentação

Este é o repositório de trabalho de Projeto Integrador VII. A disciplina acontece no Primeiro Semestre de 2021.


## Equipe

Aluno | Repositório de Trabalho
:--------- | :------ 
|Gabriel Härter Zoppo  | [Repositório](https://github.com/GabrielZoppo/ProjetoIntegrador-VII/blob/main/README.md) |
|Guilherme Baccarin | [Repositório](https://github.com/Baccarin/PI7) |
|Helena Garcia Tavares | [Repositório]() |
|Ícaro Gonçalves Siqueira  | [Repositório](https://github.com/IcaroGSiqueira/pivii) |
|Matheus Gonçalves Stigger   | [Repositório](https://github.com/MGStigger/PI7/tree/main/AVALIACAO-FINAL) |
|Miguel Gut Seara | [Repositório](https://github.com/miguelgut/PI_VII) |


### EXEHDAgateway no GitHub ###
* https://github.com/adenauery/EXEHDA-Gateway-Core
* https://github.com/adenauery/EXEHDA-Gateway

### 23/02/2021
* Discussão da metodologia a ser empregada ao longo do semestre. Identificação dos conteúdos a serem explorados, considerando as disciplinas do semestre.

### 02/03/2021
* Visão geral das atividades a serem desenvolvidas. Discussões sobre a importâncias dos middlewares nas infraestruturas modernas de instrumentação eletrônica.

### 09/03/2021
* Apresentação do middlware EXEHDA enquanto middleware para IoT, com suporte a aquisição remota de dados de sensores, seu armazenamento e processamento.

### 16/03/2021
* Sensores na IoT: principais tipos e desafios associados a sua aquisição, padronização e processamento.

### 23/03/2021
* Definição inicial dos trabalhos a serem desenvolvidos pelos alunos ao longo do semestre.

### 30/03/2021
* Revisão sobre as principais tecnologias a serem utilizadas no semestre

### 06/04/2021
* Conversa sobre os Componentes do EXEHDA: Servidor de Contexto & Gateway

### 13/04/2021 - Konker-Pub

* Explorando funcionalidades da plataforma Konker, e seu emprego no cenário do monitoramento e tratamento de dados.

## Trabalhando com a Plataforma Konker

Site da Plataforma Konker: http://www.konkerlabs.com/

  * **Publicando Dados**
    * Deadline: 20/04/2021  
    * Objetivo: Publicar dados a partir do computador ou de uma ESP32
    * Criar uma conta no Konker
    * Postar informações sensoriadas por uma biblioteca em Python e/ou Bash
    * Computador - CPython: exemplo no [Tutorial do Konker](https://konker.atlassian.net/wiki/spaces/DEV/pages/28180518/Guia+de+Uso+da+Plataforma+Konker)
    * ESP32 - MicroPython: utilizar o exemplo deste [site](https://mjrobot.org/2018/06/13/iot-feito-facil-esp-micropython-mqtt-thingspeak/) (umqtt.simple) - 

### 20/04/2021 - Konker-Rot
* Explorando o roteamento de eventos na plataforma Konker, e seu uso na geração de alertas para os usuários finais.

  * **Roteando Eventos**
    * Deadline: 27/04/2021 
    * Objetivo: Rotear eventos entre dois códigos. Os códigos podem estar em dispositivos diferentes ou não.
    * Utilizar o recurso de Roteamento de Eventos da plataforma Konker
    * Explorar o recurso de Expressão de Filtragem 

### 27/04/2021 - Konker-API
* Explorando a Konker-API para submissão de tarefas na plataforma Konker. Discussão das funcionalidades da API e sua impotância em um cenário de nuvem computacional.
* 
  * **Explorando o uso de APIs**
    * Deadline: 11/05/2021
    * Objetivo: Explorar o uso de APIs na plataforma Konker. Deverá ser utilizada pelo menos uma das funcionalidades disponíveis da API.
    * [O que é API? Explicamos de forma BEM simples, entenda 100%](https://pluga.co/blog/api/o-que-e-api/)
    * [Neil Patel: API (Application Interface Programming): Entenda O Que É](https://neilpatel.com/br/blog/api-o-que-e/) 
    * [Swagger: API Development for Everyone](https://swagger.io/)

### 04/05/2021

* Primeira Avaliação Teórico-Prática, na qual os alunos apresentaram o desenvolvido no primeiro Módulo do Semestre.


### 11/05/2021 - Subscreve-Publica

Explorando o paradigma Subscreve-Publica para a coleta e o tratamento de dados no cenário da Internet das Coisas.

  * **Trabalhar com a leitura, tratamento e publicação de dados na Internet**
    * Deadline: 25/05/2021
    * Objetivo: Exercitar a fusão de dados provenientes de diferentes origens. Empregar como fonte de dados um serviço de previsão do tempo, que disponibilize informações na Internet. A informação de temperatura deverá ser publicada no Broker MQTT da API do Projeto Integrador 7.
  * APIs utilizadas pela turma:
    
    *  https://pypi.org/project/pyowm/ (Miguel)
    *  HG Weather (HG Brasil): https://hgbrasil.com/ - [Seleção de Dados pela URL](https://api.hgbrasil.com/weather?woeid=456524&fields=only_results,temp,city,humidity,wind_speedy)
    *  https://portal.inmet.gov.br/manual/manual-de-uso-da-api-de-previs%C3%A3o - https://servicodados.ibge.gov.br/api/docs/malhas?versao=3#api-bq

### Desafio:
  * Como saber o IP de um equipamento empregando um Broker MQTT. A condição é o equipamento com o IP a ser descoberto estar conectado ao Broker MQTT.


### 18/05/2021
  * Explorando a integração da programação em Python com plataformas públicas que disponibilizam dados


### 25/05/2021
* Revisitando os passos para criação de um servidor na Interneet para a turma desenvolver seus trabalhos de forma cooperativa.


### 01/06/2021
* Explorando funcionalidades do Banco de Dados Graphite e sua integração com o Grafana para armazenamento e visualização dos dados coletados.

  * Ferramentas em Uso:
    * [Banco de Dados Graphite](https://graphite.readthedocs.io/en/latest/)
    * [Framework Grafana](https://grafana.com)

  * Configurando o Servidor da Turma de PI VII
    * [Ubuntu 20.04 Server](https://ubuntu.com/download/server) - Considerar a opção Manual Server Instalattion
    * IP servidor do Projeto Integrador(http://olaria.ucpel.edu.br/registrar_ip/)
    * [Como trocar a porta do SSH](https://www.vivaolinux.com.br/dica/Alterando-Porta-do-Servidor-SSH-no-Ubuntu-Server)
    * Ajustando o Relógio: [Time-Zone](https://linuxconfig.org/how-to-change-timezone-on-ubuntu-20-04-focal-fossa-linux) e [NTP](https://linuxconfig.org/how-to-sync-time-on-ubuntu-20-04-focal-fossa-linux)
    * [Salvando e recuperando regras do iptables](https://www.cyberciti.biz/faq/how-to-save-iptables-firewall-rules-permanently-on-linux/)
    * [Como executar comandos na inicialização do Linux](https://linuxconfig.org/how-to-run-script-on-startup-on-ubuntu-20-04-focal-fossa-server-desktop)
    * [Como proteger o servidor de ataques de força bruta](https://qastack.com.br/ubuntu/32246/how-to-secure-ubuntu-server-from-bruteforce-ssh-attacks)
    * [Como gerenciar as mensagens no login dos usuários](https://goto-linux.com/pt/2019/7/23/como-alterar-a-mensagem-de-boas-vindas-motd-no-servidor-ubuntu-18.04/)
    * [Criando Banners com ASCII](https://manytools.org/hacker-tools/ascii-banner/)
    * [Portas Abertas em um Servidor Linux](http://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-pt_br-4/s1-server-ports.html)
    * [Terminal para MS-Windows](https://www.putty.org/)
    * [Ferramentas de Monitoramento no Ubuntu](https://qastack.com.br/ubuntu/293426/system-monitoring-tools-for-ubuntu)
    * [Monitoramento com Bash](https://www.ti-enxame.com/pt/shell-script/comando-para-exibir-uso-de-memoria-uso-de-disco-e-carga-da-cpu/960818838/)
    * [Como apagar o monitor no modo texto em servidores](https://brightwhiz.com/turn-off-monitor-ubuntu-20-04/)
    * [Instalando Graphite com Docker no Ubuntu 20.04](https://www.osradar.com/how-to-install-graphite-and-graphite-web-on-ubuntu-20-04/)
    * [Instalando Grafana no Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-20-04-pt)
    * [Instalação do Nginx no Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
    * [PuTTY - Terminal para Windows](https://www.chiark.greenend.org.uk/~sgtatham/putty/) - [Gerando Chaves RSA no PuTTY](http://www.dc.ufscar.br/suporte/nossa-rede/acesso-remoto/ssh-usando-putty)
    * [Como desativar/ativar o modo gráfico no Linux com o systemd](https://elias.praciano.com/2017/05/como-desativarativar-o-modo-grafico-no-linux-com-o-systemd/)

### 08/06/2021
* Discutindo a integração do Grafana com o Banco de Dados Relacional PostgreSQL.

### 15/06/2021

* Revisão junto com os alunos do trabalho final a ser desenvolvido pela turma.

**Trabalho Final de Projeto Integrador VII**

Empregando o Servidor Ubuntu 20.04 da turma. Elaborar uma API em Python que promova as seguintes funcionalidades:

  * Receba dados produzidos por sensores e os grave em um Banco de Dados 

  * Os dados deverão ser postados e/ou lidos no Broker empregados pelo Projeto Integrador VII. Considerar a possíbilidade de empregar os dados que já estão sendo postados (PROJ-INT e PROJ-INT-2). Os dados para acesso ao Broker, bem como outras informações informações, podem ser pegos do programa "api-graphite-postgres.py" (vide /home/adenauer)

  * Criar uma tabela no PostgreSQL para publicar os sensores (novos ou já existentes). Esta postagem no PostgreSQL é necessária para gerar a listagem ou gráfico com o Python, publicando na Web. Ententende-se por sensores já existentes o PROJ-INT e PROJ-INT-2. Empregar o PHPPGADIM para auxiliar nesta tarefa. Acessar este serviço pela URL http://pi.exehda.org:3002/dbadmin/ (para login, utilizar os dados de acesso disponibilizados para a turma)

  * Gerar uma listagem ou gráfico em Python correspondentes aos dados coletados. Gerar a listagem ou o gráfico na web publicando em uma URL do tipo http://pi.exehda.org:3002/<username\>

  * Gerar uma listagem ou gráfico empregando o Grafana. Exemplos neste sentido estão disponíveis em http://pi.exehda.org:3000/ (para login, utilizar os dados de acesso disponibilizados para a turma)

Links de Apoio:
  * [Como criar Tabelas: Grafana & Postgres](https://medium.com/analytics-vidhya/grafana-with-postgresql-data-visualization-with-open-source-tool-36f5150fa290)
  * [Visualizando dados do PostgreSQL com Grafana](https://postgresconf.org/system/events/document/000/000/964/Visualizing_Data_in_PostgreSQL_With_Grafana.pdf)
  * [Python & PostGres](https://www.devmedia.com.br/como-criar-uma-conexao-em-postgresql-com-python/34079)
  * [Manipulando dados em PostgreSQL com Python](https://dadosaocubo.com/manipulando-dados-em-postgresql-com-python/)


### 22/06/2021
* Explorando os principais comandos de ferramentas textuais e na web para manipulação do PostgreSQL

### 29/06/2021
* Segunda Avaliação Teórico-Prática, na qual os alunos apresentaram o desenvolvido no segundo Módulo do Semestre.

### 06/07/2021
* Revisão do desenvolvido ao longo do semestre. Organização coletiva dos documentos produzidos.
