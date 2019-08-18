### Older Notes on Solution Components

#### The json file with the leg definitions

Two files defines the function: `rhm_sprinklerlegs` and `rhm_settings`. Examples below:

1. `rhm_sprinklerlegs.ncf`
Example json file on `~/data/rhm_sprinklerlegs.cnf` directory that defined the sprinkling times:

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

2. `rhm_settings.cnf`:

```
{"sprinkler_auto":1,"pool_auto":0,"sprinkler_A_start":"05:15","sprinkler_B_start":"18:00","geyser_auto":1}
```

#### The configuration of the ESPEasy config
Some of the configs:

- See screens 4-6 below, for the Devices.
- Also see the Rules, which mqtt messages trigger in the file [ESP8266_rules](ESP8266_rules.txt).

#### Node-RED config  

##### a) Auto-Switching:
The most complex part of the auto-switching - per rules from the json file, are in the NR section below:

![The auto-switching flow](images/sprinkler_v1.0/NR_SwitchingLogicFlow.png)

Import the json file [NR_autoswitching.json](flows/NR_autoswitching.json) into Node-RED to get these flows into Node-RED.  

##### b) Leg Settings:
The persistent settings of the legs, which should sprinkle on what day, rest for how many minutes before the next leg, and how long the leg must go for, is persisted in a file ` /data/rhm_sprinklerlegs.cnf `. The flow that creates this file for the first time, after which you can edit it, can be found in [LegSettings](/flows/LegSettings.json) under the flows folder.
