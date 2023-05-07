# LoRa-Gateway-Logger
A logging service application that tracks network health for an IoT gateway
---

# Getting Started
1. Rasperry Pi/ Virtual IoT device (CounterFit)
2: Visual Studio Code
3. Python 3.0^

## 1. IoT device
An IoT device is ideal for this project to mimic real-world performance of the logger and interact with sensors and actuators. Two options are available:
    + On Raspberry Pi, boot the device as usual and code directly on the Python IDE to create the script
    + On simulation, install CounterFit as described in this article (Hello World - CounterFit)[https://github.com/CounterFit-IoT/CounterFit/tree/main/samples/grove/light-sensor-controlled-led]
The Python virtual environment creates an isolated instance of an IoT device in your chosen folder. This tutorial uses CounterFit

## 2. Visual Studio Code
Install Visual Studio Code from Microsoft Store or the applications official page. VS Code comes with a built-in terminal for quick development. I highly recommend a **Git Bash** terminal for easy shell scripting, which can be made default for your VS Code by selecting settings in the terminal window.
![Terminal](https://user-images.githubusercontent.com/71793888/236683812-15480412-3a62-4d57-b92e-87a82ac45352.png)


## 3. Python 
Python 3.0 and above provides support for more modern functionality and high quality code scripting. To begin, ensure the following libraries are installed:
Counter Fit `pip install counterfit`
MQTT `pip install paho-mqtt`

### Create Virtual Environment
These commands create it in a .venv folder (No coding is done in this folder). Activate it with the following and launch the CounterFit application.
```
python3 -m venv .venv 
source ./.venv/bin/activate
counterfit
```
### Create logging app
![Code](https://user-images.githubusercontent.com/71793888/236684874-a57f9214-63bc-4c0f-a56f-2d0be86d61da.png)
The datetime and time modules provide timestamp and sleep functions respectively. Json parses and loads content for transmission on different networks and devices.
![Initialization](https://user-images.githubusercontent.com/71793888/236685068-4c9dd097-b364-4c6e-9974-6d6e78fef26a.png)
Counterfit: It is initiated on localhost at port 5000. Optionally, you can setup a light sensor and LED actuator in the browser app to get dummy data if you want to send to a broker.
MQTT: A unique ID identifies the client machine when servers/clients subscribe to its topics. The connection parameters like username, host etc are laid out here.

![Variables and Functions](https://user-images.githubusercontent.com/71793888/236687130-4f4e43d1-1284-47f1-bcc7-f4c0254e5dc0.png)

`lost_connection` and `got_connection` are string variables that hold connection timestamps. The connected flag indicates if there is an ongoing connection
`reconnect_delay` and `retries` define the interval time(seconds) and count for reconnection attempts respectfully

![Main Loop](https://user-images.githubusercontent.com/71793888/236687730-d8e2519b-f68c-43f9-997a-71ec3f0399c1.png)
The network message is created and parsed as a json object for telemetry. When the client is disconnected, it attemps to reconnect every 3 seconds. 
Open another bash terminal in the same environment and run `python log_service.py` 


