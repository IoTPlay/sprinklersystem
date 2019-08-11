
#### ### Systems Components Used - Electronics & Solenoids

The `sprinkler controller` is housed in 2 enclosures, see pictures 1 to 6 below. The 2 housings are:
- Housing A) `ESP8266 controller` - with an 8-way plug with all control signals to -
- Housing B) `Solenoids` for the sprinkler legs, and the pump.

##### Controller A: ESP8266 Controller

It has 3 plugs at the bottom, see picture 1, right enclosure:
- 4-way round steel plug: For the 1" water [flow meter](https://www.ebay.com/itm/G1-1-60L-min-Water-Flow-Sensor-Switch-Hall-Effect-Sensor-Flow-Meter-Sensor/171797057803?hash=item27ffe7110b:g:4WoAAOSw3xJVXXwZ) from the borehole pump.
- 8-way round steel plug: Control cable `to Controller B` - using CAT-5 cable
- 3-way audio plug: To an `DHT22` temp & humidity sensor.
- 220v in (on top side) see picture 2.


###### Controller B: The Solenoids

See picture 1 - left enclosure.
- 8-way steel round plug: From controller A via CAT-5.
- 220v in.
- 8-way green plastic plug: Relays, from left:
  - Pin 1: Relay 1 - leg 1, (to gpio15 on controller A)
  - Pin 2: Relay 2 - leg 2, (to gpio00 on controller A)
  - Pin 3: Relay 3 - leg 3, (to gpio05 on controller A)
  - Pin 4: Relay 4 - leg 4, (to gpio04 on controller A)
  - Pin 5: Relay 5 - pump,  (to gpio02 on controller A)
  - Pin 7: Ground
  - Pin 8: VCC 5v