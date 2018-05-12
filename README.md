# IoTPlay Sprinkler System


## Introduction

A 4 x leg sprinkler system, and borehole pump switching system with RPi &amp; Node-RED, and ESP8266

## Systems Components Used

- [Node-RED](https://nodered.org) on a Raspberry Pi
- [Mosquitto](https://mosquitto.org) as MQTT server running on the same RPi
- The solonoids is controlled with an ESP8266, on a wifi network, controlled by mqtt from Node-Red.
- We use ESPEasy on the Node-RED, from the community  [letscontrolit.com](https://www.letscontrolit.com/wiki/index.php/ESPEasy).
- All servers running on the RPi, runs in Docker images & containers.

## Description of the Requirements
todo.


### The Node-RED Dashboard
![Dashboard 1](images/Node-RED_Dashboard_Screen1.png)   
  Screen 1: Node-RED dashboard screen 1

![Dashboard 2](images/Node-RED_Dashboard_Screen2.png)
Screen 2: Node-RED dashboard screen 2

### The Node-RED Admin screen
![Node-RED Admin](images/Node-RED_Flows.png)
Screen 3: Node-RED Admin flows

### The ESP8266 Config Screens

![ESPEasy config1](images/ESP8266_config_1.png)
Screen 4: ESPEasy config screeen 1

![ESPEasy config2](images/ESP8266_config_2.png)
Screen 5: ESPEasy config screeen 2

![ESPEasy config3](images/ESP8266_config_3.png)
Screen 6: ESPEasy config screeen 3

### The Sprinkler Controller

![](images/Sprinkler_controller_AandB.jpg)
Picture 1: Left - The Solenoids, Right - the ESP controller

![](images/Sprinkler_controllerA_1-Inside.jpg)
Picture 2: ESP controller Inside

![](images/Sprinkler_controllerB_2a-Inside.jpg)
Picture 3: Solonoid controller Inside view 1

![](images/Sprinkler_controllerB_2a-Inside.jpg)
Picture 4: Solonoid controller Inside view 1

![](images/Sprinkler_controllerB_2b-Inside.jpg)
Picture 5: Solonoid controller Inside view 2

![](images/Sprinkler_controllerB_2c-Inside.jpg)
Picture 6: Solonoid controller Inside view 3
