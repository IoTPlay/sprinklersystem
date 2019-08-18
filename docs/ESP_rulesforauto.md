## The rules run in Auto mode

### The code that we will use

- Internal Variables, 1- 16.
    - Using Internal Variables: `Let,<n>,<value>`

- Outstanding Questions:
    - Can I keep dummy variables - and set them with mqtt?
    - Can we use float varibles for start times?
    - Can I set internal variables with mqtt?

### Possible use of the 16 ESP variables

The Variable names: 

|VAR    |Var Name | Var Description       |   
|----   |-------- |---------------------- |  
|VAR#1  | Leg 1   | Sprinkler Leg 1       |
|VAR#2  | Leg 2   | Sprinkler Leg 2       |
|VAR#3  | Leg 3   | Sprinkler Leg 3       |
|VAR#4  | Leg 4   | Sprinkler Leg 4       |
|VAR#5  | ON dur  | on duration min       |
|VAR#7  | Day 1   | Day - Sunday          |  
|VAR#8  | Day 2   | Day - Monday          |  
|VAR#13 | Day 7   | Day - Saturday        |  
|VAR#14 |rest     | Rest time between legs|    
|VAR#15 |dur      | leg duration on       |        
|VAR#16 |auto     | auto or manual mode?  |    

#### Scenario 1

A possible scenario to use the 16 variables if we upload the variables to the ESP everytime it boots up.

Sprinklers currently on `Auto`, leg duration 14 min, rest between leg on's 20 min, sprinklel legs 1, 3. Current sprinkle time is 11 min. Do this programme on Sun, Tue, Thu, ...

| V1 | V2 | V3 | V4 | V5 | V6 | V7 | V8 | V9 | V10 | V11 | V12 | V13 | V14 | V15 | V16 |   
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  1 |    |  1 |    | 11 |    | 1  |    | 1  |     |  1  |     |  1  |  20 |  14 |  1  |      

Unresolved with this approach:

- var start1 // start time in the morning
- var start2 // start time in the eve
- can minutes of time be stored ie as 11 min?
- days - what about the other schedule, thus remove days from variables, and upload the day's schedule every day...   
- Can we upload the variables with mqtt? 

## Pseudo Code

```
Let,1,[Temp#Value]
```

### References

- Create a rule note based on a device: [Forum](https://www.letscontrolit.com/forum/viewtopic.php?f=6&t=6832&p=37809&hilit=rule+set#p37809)
- ESPEasy Rules, heading 'Internal Variables': [Documentation](https://espeasy.readthedocs.io/en/latest/Rules/Rules.html#internal-variables)