# Cliente Python para subscrever em um Broker MQTT
#
# Para instalar o paho-mqtt use o comando pip install paho-mqtt
import paho.mqtt.client as mqtt
import json
import socket
import time
from datetime import datetime
import os

# Retorno quando um cliente recebe um  CONNACK do Broker, confirmando a subscricao
def on_connect(client, userdata, flags, rc):
    print("Conectado, com o seguinte retorno do Broker: "+str(rc))

    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("i2wac/#")

# Callback responsavel por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))

    try:
      dados_python = json.loads(msg.payload)
 #    print(dados_python['data'])
 #    print(dados_python['uuid'])
      if dados_python['uuid'] == "d4ddf7b3-aa5d-4d60-a614-571d70788334":
        sensor = dados_python['data']
        #print(sensor)
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
        print (data_e_hora_em_texto)
        message = 'PROJ-INT ' + sensor + " " + str(int(time.time())) + "\n"
        print ('Recebida Mensagem: %s' % message)
#        print(str(dados_python))
        comando = "mosquitto_pub -h localhost -t PI7 -u XXXXX -P XXXXXXXX -m " + "'" + '{"id":  "PROJ-INT", "data": ' + '"' + sensor
        comando2 = comando + '"}' + "'"
        print(comando2)
        os.system(comando2)

      if dados_python['uuid'] == "c784729e-8611-44ad-9540-383f04cc38fc":
        sensor = dados_python['data']
        #print(sensor)
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
        print (data_e_hora_em_texto)
        message = 'PROJ-INT-2 ' + sensor + " " + str(int(time.time())) + "\n"
        print ('Recebida Mensagem: %s' % message)
#        print(str(dados_python))
        comando = "mosquitto_pub -h localhost -t PI7 -u XXXXXX -P XXXXXX -m " + "'" + '{"id":  "PROJ-INT-2", "data": ' + '"' + sensor
        comando2 = comando + '"}' + "'"
        print(comando2)
        os.system(comando2)

    except Exception:
      print("Erro na leitura do JSON via Broker MQTT")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Define um usuário e senha para o Broker, se não tem, não use esta linha
client.username_pw_set("middleware", password="XXXXXXX")

# Conecta no MQTT Broker
client.connect("200.132.103.53", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# Inicia o loop
client.loop_forever()
