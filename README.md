# BME280USB

- ### Temperature, Humidity, Pressure Sensor BME280 on RPi Pico
If you want to use BME280 sensor on long cable, copy two files bme280_float.py and main.py to RPi Pico.

Connect the BME280 sensor to the i2C RPi Pico port using wiring diagram below.

 - ### Wiring diagram
```
RPi Pico  [GP22 Pin 29]------------------------------ [VCC]  BME280
RPi Pico  [GP16 Pin 21] ----------------------------- [SDA]  BME280
RPi Pico  [GP17 Pin 22] ----------------------------- [SDC]  BME280
RPi Pico  [GND  Pin 38] ----------------------------- [GND]  BME280
RPi Pico  [3v3  Pin 36] ----------------------------- [CS]   BME280
```
Connect PC with the RPi Pico together with the USB cable.
```
BME280 [i2c] <------> [i2C] RPi Pico [USB] <--------------> RPi [USB]
```

Select proper USB port number in RPiMS configuration.


## B.o.M - Bill of Materials

* [BME280](https://botland.store/multifunctional-sensors/13463-bme-humidity-temperature-and-pressure-sensor-i2cspi-33v5v-waveshare-15231.html) - 1 pcs
* [Raspberry Pico](https://botland.store/raspberry-pi-pico-modules-and-kits/18767-raspberry-pi-pico-rp2040-arm-cortex-m0-0617588405587.html) - 1 pcs
* [RPi Pico and Sensor Case](https://www.tme.eu/pl/en/details/pp73g/enclosures-for-alarms-and-sensors/supertronic/) - 1 pcs
* [MicroUSB B-A cable](https://botland.store/usb-20-cables/6417-microusb-b-a-cable-in-white-braid-esperanza-eb181w-2m-5901299920107.html) - 1 pcs
