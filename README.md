## Apresentação

Este é o repositório de trabalho de Projeto Integrador VII. A disciplina acontece no Primeiro Semestre de 2021.


## Equipe

Aluno | Repositório de Trabalho
:--------- | :------ 
|Gabriel Härter Zoppo  | [Repositório](https://github.com/GabrielZoppo/ProjetoIntegrador-VII/blob/main/README.md) |
|Guilherme Baccarin | [Repositório](https://github.com/Baccarin/PI7) |
|Helena Garcia Tavares | [Repositório]() |
|Ícaro Gonçalves Siqueira  | [Repositório](https://github.com/IcaroGSiqueira/pivii) |
|Matheus Gonçalves Stigger   | [Repositório]() |
|Miguel Gut Seara | [Repositório](https://github.com/miguelgut/PI_VII) |


### EXEHDAgateway no GitHub ###
* https://github.com/adenauery/EXEHDA-Gateway-Core
* https://github.com/adenauery/EXEHDA-Gateway


### 16/03/2021
* Introdução à disciplina, com a discusão da metodologia de trabalho a ser desenvolvida
* Apresentação do middlware EXEHDA
* Visão geral das atividades a serem desenvolvidas

### 23/03/2021
* Definição inicial dos trabalhos a serem desenvolvidos

### 30/03/2021
* Revisão sobre tecnologias a serem utilizadas

### 06/04/2021
* Conversa sobre os Componentes do EXEHDA: Servidor de Contexto & Gateway

## Trabalhando com a Plataforma Konker

Site da Plataforma Konker: http://www.konkerlabs.com/

### 13/04/2021 - Konker-Pub

  * **Publicando Dados**
    * Deadline: 20/04/2021  
    * Objetivo: Publicar dados a partir do computador ou de uma ESP32
    * Criar uma conta no Konker
    * Postar informações sensoriadas por uma biblioteca em Python e/ou Bash
    * Computador - CPython: exemplo no [Tutorial do Konker](https://konker.atlassian.net/wiki/spaces/DEV/pages/28180518/Guia+de+Uso+da+Plataforma+Konker)
    * ESP32 - MicroPython: utilizar o exemplo deste [site](https://mjrobot.org/2018/06/13/iot-feito-facil-esp-micropython-mqtt-thingspeak/) (umqtt.simple) - 

### 20/04/2021 - Konker-Rot
  * **Roteando Eventos**
    * Deadline: 27/04/2021 
    * Objetivo: Rotear eventos entre dois códigos. Os códigos podem estar em dispositivos diferentes ou não.
    * Utilizar o recurso de Roteamento de Eventos da plataforma Konker
    * Explorar o recurso de Expressão de Filtragem 

### 27/04/2021 - Konker-API
  * **Explorando o uso de APIs**
    * Deadline: 11/05/2021
    * Objetivo: Explorar o uso de APIs na plataforma Konker. Deverá ser utilizada pelo menos uma das funcionalidades disponíveis da API.
    * [O que é API? Explicamos de forma BEM simples, entenda 100%](https://pluga.co/blog/api/o-que-e-api/)
    * [Neil Patel: API (Application Interface Programming): Entenda O Que É](https://neilpatel.com/br/blog/api-o-que-e/) 
    * [Swagger: API Development for Everyone](https://swagger.io/)

### 04/05/2021 - Subscreve-Publica
  * **Trabalhar com a leitura, tratamento e publicação de dados na Internet**
    * Deadline: 25/05/2021
    * Objetivo: Exercitar a fusão de dados provenientes de diferentes origens. Empregar como fonte de dados um serviço de previsão do tempo, que disponibilize informações na Internet. A informação de temperatura deverá ser publicada no Broker MQTT da API do Projeto Integrador 7.
  * APIs utilizadas pela turma:
    
    *  https://pypi.org/project/pyowm/ (Miguel)
    *  HG Weather (HG Brasil): https://hgbrasil.com/ - [Seleção de Dados pela URL](https://api.hgbrasil.com/weather?woeid=456524&fields=only_results,temp,city,humidity,wind_speedy)
    *  https://portal.inmet.gov.br/manual/manual-de-uso-da-api-de-previs%C3%A3o - https://servicodados.ibge.gov.br/api/docs/malhas?versao=3#api-bq

### 01/06/2021

  * Ferramentas em Uso:
    * Banco de Dados Graphite: https://graphite.readthedocs.io/en/latest/
    * Framework Grafana: https://grafana.com

  * Configurando o Servidor da Turma de PI VII
    * Ubuntu 20.04 Server - https://ubuntu.com/download/server
    * IP do servidor: http://olaria.ucpel.edu.br/registrar_ip/
    * Como trocar a porta do SSH: https://www.vivaolinux.com.br/dica/Alterando-Porta-do-Servidor-SSH-no-Ubuntu-Server
    * Criando Banners com ASCII: https://manytools.org/hacker-tools/ascii-banner/
    * Ajustando o Relógio: [Time-Zone](https://linuxconfig.org/how-to-change-timezone-on-ubuntu-20-04-focal-fossa-linux) e [NTP](https://linuxconfig.org/how-to-sync-time-on-ubuntu-20-04-focal-fossa-linux)
    * Salvando e recuperando regras do iptables: https://www.cyberciti.biz/faq/how-to-save-iptables-firewall-rules-permanently-on-linux/
    * Como executar comandos na inicialização do Linux: https://linuxconfig.org/how-to-run-script-on-startup-on-ubuntu-20-04-focal-fossa-server-desktop
    * Como proteger o servidor de ataques de força bruta: https://qastack.com.br/ubuntu/32246/how-to-secure-ubuntu-server-from-bruteforce-ssh-attacks
    * Como gerenciar as mensagens no login: https://goto-linux.com/pt/2019/7/23/como-alterar-a-mensagem-de-boas-vindas-motd-no-servidor-ubuntu-18.04/
    * Portas Abertas em um Servidor Linux: http://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-pt_br-4/s1-server-ports.html
    * [Terminal para MS-Windows](https://www.putty.org/)
    * [Monitoramento no Ubuntu](https://qastack.com.br/ubuntu/293426/system-monitoring-tools-for-ubuntu)
    * [Monitoramento com Bash](https://www.ti-enxame.com/pt/shell-script/comando-para-exibir-uso-de-memoria-uso-de-disco-e-carga-da-cpu/960818838/)

### Desafio:
  * Como saber o IP de um equipamento empregando um Broker MQTT. A condição é o equipamento com o IP a ser descoberto estar conectado ao Broker MQTT.

https://manytools.org/hacker-tools/ascii-banner/
