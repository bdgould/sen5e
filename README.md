# Sen5e

Simple project to make use of DHT22 sensors to monitor temperature and
humidity at various locations.  Reports the various data points into 
an InfluxDB time-series database for analysis/monitoring.

## Setup
It is suggested you use a python 3.7 virtual environment and pip3 to
install the necessary requirements.  You can use the install.sh
script to set up the daemon on a running Raspberry Pi.

After hooking up your DHT22 sensors to your GPIO board 
([documentation](https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/))
you can configure this python daemon to monitor and report the sensor
readings. 

 1. Run `install.sh` to install pip3 dependencies and then distribute
 files to necessary locations.
 2. Configure the daemon process to 
 3. Use `systemctl start sen5e` to start the daemon process
 4. Use `systemctl enable sen5e` to auto-start the daemon when the
 pi starts up.