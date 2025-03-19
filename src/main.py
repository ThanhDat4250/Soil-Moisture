import utime
from machine import I2C, Pin, ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

SOIL_MOISTURE_PIN = 26
I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16 
MIN_MOISTURE = 1324 #fully wet
MAX_MOISTURE = 3604 #fully dry
soil = ADC(Pin(SOIL_MOISTURE_PIN))
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def read_soil_moisture():
    adc_value = soil.read_u16() >> 4  # Scale 16-bit value to 12 bits
    return adc_value

def calculate_moisture_percentage(adc_value):
    moisture = (MAX_MOISTURE - adc_value) * 100 / (MAX_MOISTURE - MIN_MOISTURE)
    return moisture

def display_moisture_and_adc(moisture, adc_value):
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Moisture - ADC")
    lcd.move_to(2, 1)
    lcd.putstr("%.2f%% - %d" % (moisture, adc_value))

def print_moisture_and_adc(moisture, adc_value):
    print("Moisture: " + "%.2f" % moisture + "% (ADC: " + str(adc_value) + ")")

def main():
    read_delay = 1  # Delay between readings (in seconds)
 
    while True:
        adc_value = read_soil_moisture()
        moisture = calculate_moisture_percentage(adc_value)
        display_moisture_and_adc(moisture, adc_value)
        print_moisture_and_adc(moisture, adc_value)
        utime.sleep(read_delay)

if __name__ == "__main__":
    main()
