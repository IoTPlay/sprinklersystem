# IoTPlay Sprinkler System 2.0

After running my SprinklerSystem 1.0 for 3 yrs, its time formore & new concepts. Find below the still-in-progress functional requirements, to which I am building the system.

## Introduction

A 4 x leg sprinkler system, and borehole pump switching system with RPi &amp; Node-RED, and ESP8266. Where-as Sprinkler 1.0 did all the control from Node-RED on the RPi, the next version - Sprinkler 2.0 will provide the variables of control to the ESP8266, and it will do the control.

## Specifications of the System

Find below the requirements for an edge-based solution:

#### Functional:
- 4 x sprinkler leg valves to be switched on- and off.
- A borehole pump to be switched on before any leg is activated, and switched off afterwards. 
- Switching can either be automatic, or manual.
  - For **automatic**, A schedule of start / stop / in-between leg-rest time will be downloaded to the ESP from the RPi at startup of the ESP.
  - If **manual**, a message will be sent via mqtt for the leg to switch on, and duration it has to be in this state.
- Whilst sprinkling, the ESP will send back a message to show the time left till it switches off.

#### Schedules:
- On the sprinkler `leg schedules`:
  - Able to switch each leg on `twice a day`;
  - Able to choose which legs should sprinkle on `which days`;
  - `Duration between` legs on as a variable- to allow the borehole water to fill-up;  
- The above must be downloaded as variables to the ESP.

//DEPRECATED//- All schedules functions to be `data-driven`, where a json file on the system stores the definitions of all above, to allow this file to be manipulated to change sprinkling time, rest period, sprinkle period, and days,- per leg.

#### Interacting with the System

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

##### Homie
- the ESP8266 will be controlled with the [homie 4.0](https://github.com/homieiot/convention/blob/develop/convention.md) standard, (as at 2019 Aug - not yet promolgated).  
##### Apple HomeKit
- must be able to work with Apple Homekit.


## Implementation

### Systems Components Used

Building blocks are:
- [Node-RED](https://nodered.org) on a Raspberry Pi
- [Mosquitto](https://mosquitto.org) as MQTT server running on the same RPi
- The sprinkler solenoids is controlled with an ESP8266, on a wifi network, using `mqtt` from Node-Red.
- We use ESPEasy on the Node-RED, from the community  [letscontrolit.com](https://www.letscontrolit.com/wiki/index.php/ESPEasy).  
- /DEPRECATED/ A MariaDB instance to track stats of sprinkling.
- All servers running on the RPi, runs in Docker images & containers.


### Notes on Solution Components

- [About the Electronics](READ_electronics.md)
- [About the Screens of the App (old)](READ_old_screens.md)
- [Node-RED & ESP config (old)](READ_old_solcomp.md)

## Todo
The project is not yet completed. Further requirements includes:
- Did it, or is it raining? Is it, or will the rain be enough? Use either barometric pressure, and/or [Darksky](https://flows.nodered.org/node/node-red-node-darksky) forecast, and the IoTPlay ESP8266 rain meter to stop sprinkling for a day;  

- Amount of water to drop based on levels of Soil moisture, using for instance [Tindie's SoilWatch10](https://www.tindie.com/products/pinotech/soilwatch-10-soil-moisture-sensor/?pt=ac_prod_search).

- Change starting time of the cycle with the season's changes.



