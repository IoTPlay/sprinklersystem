# IoTPlay Sprinkler System


## Introduction

A 4 x leg sprinkler system, and borehole pump switching system with RPi &amp; Node-RED, and ESP8266

## Specifications of the System

Find below the requirements I had when building the flows.

#### Functional:
- 4 sprinkler leg valves to be switched on- and off.
- A borehole pump to be switched on before any leg is activated, and switched off afterwards.  

#### Schedules:
- On the sprinkler `leg schedules`:
  - Able to switch each leg on `twice a day`;
  - Able to choose which legs should sprinkle on `which days`;
  - `Duration between` legs on as a variable- to allow the borehole water to fill-up;  


- All schedules functions to be `data-driven`, where a json file on the system stores the definitions of all above, to allow this file to be manipulated to change sprinkling time, rest period, sprinkle period, and days,- per leg.

#### Web front-end:
A Web front-end to work on a phone, where the sprinkler system can be:  
- **Actions**:
  - put into `auto-mode`, where the data-file is used for the schedule;
  - put in `non-auto mode` or manual, where the schedule does not determine the on/off times;
  - Able to switch any leg `on/off manually`, including the pump;
  - Button to override `All Off` - switching the pump and legs off at once.
- **Reports**:
  - A report to determine the `total sprinkler time per day`;
  - Report on how much `water was pumped` for the day;
  - Report to view the current schedules, times, and rest periods that are set.

## Implementation

### Systems Components Used

Building blocks are:
- [Node-RED](https://nodered.org) on a Raspberry Pi
- [Mosquitto](https://mosquitto.org) as MQTT server running on the same RPi
- The solonoids is controlled with an ESP8266, on a wifi network, using `mqtt` from Node-Red.
- We use ESPEasy on the Node-RED, from the community  [letscontrolit.com](https://www.letscontrolit.com/wiki/index.php/ESPEasy).  
- A MariaDB instance to track stats of sprinkling.


All servers running on the RPi, runs in Docker images & containers, all published on [github IoTPlay](http://github/iotplay).


### Notes on Solution Components

#### The json flatfile with the leg definintions

Example json file in directory that defined the sprinkling times:

```
{"legday":
  [
    [1,1,1,1,1,0,1,"L1A",15,40],
    [0,0,0,0,0,1,0,"L1B",15,40],
    [1,1,1,1,1,0,1,"L2A",15,40],
    [0,0,0,0,0,0,0,"L2B",15,40],
    [0,0,0,0,0,0,0,"L3A",15,40],
    [1,1,1,1,1,1,1,"L3B",15,40],
    [0,0,0,0,0,0,0,"L4A",15,40],
    [1,1,1,1,1,1,1,"L4B",15,40]
  ]
}
```

Row 1 explained: sprinkle leg 1, morning, for 15 minutes, then rest 40 minutes for the borehole to fill-up, and sprinkle all days except Friday (our grass is cut on this day).

#### The configuration of the ESPEasy config

See screens 4-6 below, for the Devices. Also see the Rules, which mqtt messages trigger in the file [ESP8266_rules](ESP8266_rules.txt).


## Todo
The project is not yet completed. Further requirements includes:
- Did it, or is it raining? Is it, or will the rain be enough? Use either barometric pressure, and/or [Darksky](https://flows.nodered.org/node/node-red-node-darksky) forecast, and the IoTPlay ESP8266 rain meter to stop sprinkling for a day;  

- Amount of water to drop based on levels of Soil moisture, using for instance [Tindie's SoilWatch10](https://www.tindie.com/products/pinotech/soilwatch-10-soil-moisture-sensor/?pt=ac_prod_search).

- Change starting time of the cycle with the season's changes.

### Notes on Implementation



## The Screens of Dashboard, Node-RED, and Photos of the Electronics

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
