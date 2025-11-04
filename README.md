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

| **_Item_**              | **_Description_**             | **_Quantity_** | **_Unit Price ($)_** | **_Total Price ($)_** | **_URL_**                                                                                                       | **_Running Total ($ incl VAT)_** |
| ----------------------- | ----------------------------- | -------------- | -------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| MBB02070C1009FCT00      | 10 Ohm resistor               | 1              | $0.10                | $0.10                 | https://www.digikey.co.uk/en/products/detail/vishay-beyschlag-draloric-bc-components/MBB02070C1009FCT00/5062945 | $0.12                            |
| MBB02070C3309FCT00      | 33 Ohm resistor               | 1              | $0.10                | $0.10                 | https://www.digikey.co.uk/en/products/detail/vishay-beyschlag-draloric-bc-components/MBB02070C3309FCT00/5063340 | $0.24                            |
| MCP23018-E/SP           | I/O expander (I2C)            | 1              | $2.13                | $2.13                 | https://www.digikey.co.uk/en/products/detail/microchip-technology/MCP23018-E-SP/1999505                         | $2.80                            |
| PEC12R-3020F-N0024      | Rotary encoder                | 8              | $1.19                | $9.55                 | https://www.digikey.co.uk/en/products/detail/bourns-inc/PEC12R-3020F-N0024/6153381                              | $14.26                           |
| MX1A-E1NW               | Key switch                    | 22             | $1.25                | $27.50                | https://www.digikey.co.uk/en/products/detail/cherry-americas-llc/MX1A-E1NW/20180                                | $47.26                           |
| SJ1-3513N               | 3.5mm TRS jack                | 1              | $1.17                | $1.17                 | https://www.digikey.co.uk/en/products/detail/same-sky-formerly-cui-devices/SJ1-3513N/738686                     | $48.66                           |
| SC1631                  | RPi Pico 2 microcontroller    | 1              | $5.00                | $5.00                 | https://www.digikey.co.uk/en/products/detail/raspberry-pi/SC1631/24627136                                       | $54.66                           |
| SSW-120-01-T-S-LL       | Socket (20 pins)              | 2              | $2.38                | $4.76                 | https://www.digikey.co.uk/en/products/detail/samtec-inc/SSW-120-01-T-S-LL/7881604                               | $60.37                           |
| PH1-20-UA               | Header (20 pins)              | 2              | $0.35                | $0.70                 | https://www.digikey.co.uk/en/products/detail/adam-tech/PH1-20-UA/9830398                                        | $61.21                           |
| ICS-328-T               | DIP socket                    | 1              | $0.24                | $0.24                 | https://www.digikey.co.uk/en/products/detail/adam-tech/ICS-328-T/9832859                                        | $61.50                           |
| “971110154”             | Standoffs                     | 4              | $0.85                | $3.40                 | https://www.digikey.co.uk/en/products/detail/w%C3%BCrth-elektronik/971110154/9488627                            | $65.58                           |
| “4707”                  | Hex nut                       | 4              | $0.14                | $0.56                 | https://www.digikey.co.uk/en/products/detail/keystone-electronics/4707/4499300                                  | $66.25                           |
| SH1106                  | OLED display module           | 1              | $3.68                | $3.68                 | https://www.aliexpress.com/item/1005006072386746.html                                                           | $70.67                           |
| MIDI DIN to 3.5mm TRS   | DIN/TRS converter cable       | 1              | $8.20                | $8.20                 | https://www.aliexpress.com/item/1005009365055437.html                                                           | $80.51                           |
| Ugreen Micro USB Cable  | Micro USB for microcontroller | 1              | $2.69                | $2.69                 | https://www.aliexpress.com/item/32391749504.html                                                                | $83.74                           |
| XDA Profile PBT Keycaps | 1U keycaps (30pcs)            | 1              | $5.41                | $5.41                 | [https://www.aliexpress.com/item/1005005514406952.html](https://www.aliexpress.com/item/1005005514406952.html)  | $90.23                           |
| 11mm Potentiometer Knob | Knobs for encoders (10pcs)    | 1              | $2.10                | $2.10                 | https://www.aliexpress.com/item/1005003991686731.html                                                           | $92.75                           |
|1N4148|Diodes|22|$0.03|$0.64|https://www.digikey.co.uk/en/products/detail/onsemi/1N4148/458603|$93.52




