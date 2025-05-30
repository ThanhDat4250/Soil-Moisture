# Soil Moisture Monitoring with Raspberry Pi Pico

This project utilizes Raspberry Pi Pico and a Capacitive Soil Moisture Sensor to monitor soil moisture levels, enabling efficient irrigation.

For a farmer to get the best plant growth, the soil needs to be not too wet and not too dry. IoT devices can help with this by measuring soil moisture, allowing a farmer to only water when needed, optimizing watering schedules and promoting healthy plant growth.

> [!note]
> Our Experiment video: [How to measure soil moisture 101 - Group 5](https://www.youtube.com/watch?v=G-8WgRoHzO4)

## Files Structure
```
Soil-Moisture/
├── src/
│   ├── assets/
|       ├── graph/
|       └── img/
│   ├── main.cpp
|   └── main.py
├── LICENSE
└── README.md
```
## Requirements

### Hardware

* LCD 16x2 I2C
* Jumper Wires and Breadboard
* [Raspberry Pi Pico 1](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-1-family)
> Raspberry Pi Pico 1 has an integrated `12-bit ADC` that generates values from `0-4095`
* Capacitive Analog Soil Moisture Sensor
> Capacitive Analog Soil Moisture Sensor only returns analog signal that represents a voltage to indicate soil moisture


### Software

* Thonny IDE: [Thonny Python IDE for beginners](https://thonny.org/)
* MicroPython for Raspberry Pico [MicroPython Pico](https://micropython.org/download/RPI_PICO/)

> Check out [Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf) for more information.

### Dependencies
The project requires the following modules: `pico_i2c_lcd.py` `lcd_api.py`

You can find these in the `module` folder. Download and copy them to your Raspberry Pi Pico's filesystem using Thonny.

You can find the source here: [RPI-PICO-I2C-LCD](https://github.com/T-622/RPI-PICO-I2C-LCD)

## Setup

### 1.  **Hardware Connection:**
   
Connect the soil moisture sensor to the Raspberry Pi Pico according to the provided circuit diagram.

Connect the I2C LCD to the Raspberry Pi Pico.
  
![circuit](./src/assets/img/circuit_diagram.jpg)

### 2.  **Software Setup:**

Download dependencies and install Thonny IDE.

Flash the Raspberry Pi Pico with MicroPython firmware.

Upload the MicroPython code at [main.py](./src/main.py) to the Pico via Thonny. The MicroPython code reads analog values from the soil moisture sensor and processes them to determine the soil moisture level.

> [!note]
> In the `src` folder, there is another `main.cpp` file which is only suitable with Arduino microcontroller and Arduino IDE.
> 
> We only include it here for reference.
> 
  
### 3.  **Sensor Calibration:**

Use the gravimetric method to calibrate the sensor — measuring the weight of water per unit weight of dry soil (kg water/kg dry soil).

We did a simple experiment to measure 4 real soil samples and record the data including weights of wet soil, dry soil, and sensor reading values for the purpose of calibration. 

> Here is the experiment video: [How to measure soil moisture 101 - Group 5](https://www.youtube.com/watch?v=G-8WgRoHzO4)

With the actual data gathered from the abovementioned experiment, here is the linear graph that matches sensor reading values from 0 - 4095 with actual moisture percent present in the soil sample. 

> This is the code [moisture_linear.py](./src/assets/graph/moisture_linear.py) to generate the graph below.

![graph](./src/assets/img/graph_moisture.jpg)

## Credits
Project idea: [Microsoft IoT For Beginners - Detect Soil Moisture](https://github.com/microsoft/IoT-For-Beginners/tree/main/2-farm/lessons/2-detect-soil-moisture)





