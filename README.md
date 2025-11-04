# DNA Sequencer
![](media/header.png)
A flexible MIDI sequencer powered by a Raspberry Pi Pico 2 (RP2350), inspired by sequencers found in the Korg Volca and Elektron boxes. Aims to be accessible, affordable, repurposable, and expandable.

## Current features
- RPi Pico 2 microcontroller, the brains of the sequencer
- MIDI output via 3.5mm TRS, or USB
- 16 keys for step editing, note input, or other custom macros
- 6 keys for navigation (get ready to menu dive!)
- 8 incremental encoders for CC/parameter adjustment and macros
- 128x64 1.3" OLED display
- All components are through-hole for easy soldering, and readily available

## Planned features
- 8 polyphonic tracks with different modes to facilitate various types of sequencing (e.g drum, chord, arp, euclidian, etc etc), can be assigned to any 16 MIDI channels
- 64 step sequencer with the ability to sequence 8 CC parameters, variable length, microtiming, and randomization/generation features
- 16 patterns with chaining

## Why'd you make this?
Currently the options for standalone hardware MIDI sequencers are either budget sequencers that do not have a vast featureset and, at least to myself, were limiting in terms of potential creativity, or more feature rich sequencers which cost a couple arms and legs. I wanted to make a device that would help bridge the gap between those two mountains and leverage the power of DIY & open source in order to create an accessible, affordable, repurposable, and expandable hardware sequencer. Additionally, this project serves as my first 100% serious hardware project, so all of the processes I learn throughout the journey of creating this device will be invaluable to me and whatever future endeavours lie before me... learning is fun!

## Images/Videos
PCB
![](media/pcb.png)
![](media/pcbnice.png)
Schematic
![](media/schematic.png)

## Bill of Materials

Choice of keycaps is up to you, as long as they're compatible with Cherry MX. You will also need a Micro USB cable for power and USB MIDI, and a 3.5 TRS to DIN converter for regular MIDI

|Item                   |Description                  |Quantity|Unit Price ($)|Total Price ($)|URL                                                                                                              |Running Total ($ incl VAT)|
|-----------------------|-----------------------------|--------|--------------|---------------|-----------------------------------------------------------------------------------------------------------------|--------------------------|
|MBB02070C1009FCT00     |10 Ohm resistor              |5       |$0.1346       |$0.6730        |https://www.lcsc.com/product-detail/C1364448.html?s_z=n_MBB02070C1009FCT00                                       |$0.81                     |
|MBB02070C3309FCT00     |33 Ohm resistor              |5       |$0.0748       |$0.3740        |https://www.lcsc.com/product-detail/C1366513.html?s_z=n_MBB02070C3309FCT00                                       |$1.26                     |
|MCP23018-E/SP          |I/O expander (I2C)           |1       |$3.5955       |$3.5955        |https://www.lcsc.com/product-detail/C647353.html?s_z=n_MCP23018-E%252FSP                                         |$5.57                     |
|PEC12R-3020F-N0024     |Rotary encoder               |8       |$2.5377       |$20.3016       |https://www.lcsc.com/product-detail/C143785.html?s_z=n_PEC12R-3020F-N0024                                        |$29.93                    |
|Gateron Switches KS9   |Key switch (30pcs)           |1       |$12.9500      |$12.9500       |https://www.aliexpress.com/item/1005007474127225.html                                                            |$45.47                    |
|SJ1-3513N              |3.5mm TRS jack               |1       |$1.9911       |$1.9911        |https://www.lcsc.com/product-detail/C4992806.html?s_z=n_SJ1-3513N                                                |$47.86                    |
|SC1631                 |RPi Pico 2 microcontroller   |1       |$8.9800       |$8.9800        |https://www.aliexpress.com/item/1005008201547951.html                                                            |$58.64                    |
|KH-2.54FH-1X20P-H8.5   |Socket (20 pins)             |5       |$0.1722       |$0.8610        |https://www.lcsc.com/product-detail/C2905423.html?s_z=n_2.54mm%2520Through%2520Hole%25208.5mm%2520Brass%25201x20P|$59.67                    |
| PH2.54-1X20P-H25      |Header (20 pins)             |5       |$0.0488       |$0.2440        |https://www.lcsc.com/product-detail/C42431804.html?s_z=n_1x20P%25202.54mm                                        |$59.96                    |
|ICS-328-T              |DIP socket                   |1       |$0.2912       |$0.2912        |https://www.lcsc.com/product-detail/C5656607.html?s_z=n_ICS-328-T                                                |$60.31                    |
|XHHD*TZ*0216           |Standoffs                    |4       |$0.0274       |$0.1096        |https://www.lcsc.com/product-detail/C41379425.html                                                               |$60.44                    |
|C357431                |Hex nut                      |100     |$0.0024       |$0.2400        |https://www.lcsc.com/product-detail/C357431.html                                                                 |$60.73                    |
|SH1106                 |OLED display module          |1       |$3.6800       |$3.6800        |https://www.aliexpress.com/item/1005006072386746.html                                                            |$65.15                    |
|MIDI DIN to 3.5mm TRS  |DIN/TRS converter cable      |1       |$8.2000       |$8.2000        |https://www.aliexpress.com/item/1005009365055437.html                                                            |$74.99                    |
|Ugreen Micro USB Cable |Micro USB for microcontroller|1       |$2.6900       |$2.6900        |https://www.aliexpress.com/item/32391749504.html                                                                 |$78.22                    |
|XDA Profile PBT Keycaps|1U keycaps (30pcs)           |1       |$5.4100       |$5.4100        |https://www.aliexpress.com/item/1005005514406952.html                                                            |$84.71                    |
|11mm Potentiometer Knob|Knobs for encoders (10pcs)   |1       |$2.1000       |$2.1000        |https://www.aliexpress.com/item/1005003991686731.html                                                            |$87.23                    |
|1N4148                 |Diodes                       |50      |$0.0090       |$0.4500        |https://www.lcsc.com/product-detail/C402212.html?s_z=n_1N4148%2520do-35                                          |$87.77                    |





