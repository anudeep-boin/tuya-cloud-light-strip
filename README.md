# tuya-cloud-light-strip
This project is developed using Tuya SDK, which enables you to quickly    develop smart devices, branded APP, cloud development project, etc.

For more information, please check Tuya Developer Click and Connect      Challenge: https://pages.tuya.com/develop/ClickAndConnect_TuyaDeveloper?_source=e9684c7ca6b31e7221c8420f5af94631 


Full documentation for this package can be found here: <a href="https://github.com/Octoober/tuya-bulb-control">Link</a><br />
(Use that for API documentation)

<h2>Installation:</h2>
<h4>pip install tuya-bulb-control --upgrade</h4>

<h3>Sample Code:</h3>

```Python
from tuya_bulb_control import Bulb

CLIENT_ID = ''    # Access ID or Client ID
SECRET_KEY = ''   # Access Secret or Client Secret
DEVICE_ID = ''    # Devise id which is online to control
REGION_KEY = ''   # Region key eg: in for india, eu for europe, us for usa, cn for china, etc based on region where the device is there 

bulb = Bulb(
    client_id=CLIENT_ID,
    secret_key=SECRET_KEY,
    device_id=DEVICE_ID,
    region_key=REGION_KEY
)

# Turn on the bulb
bulb.turn_on()

# Change the color to green
bulb.set_colour_v2(rgb=(0, 255, 0))

# Turn off the light bulb after 5 minutes
bulb.set_toggle_timer(value=5)


#rest of the functions can be seen from hte below list, their progrms are present in the folderlight strip control.
```


<br>
<h2>Steps for doing the project:</h2>
1)Make an account here: <a href="https://iot.tuya.com/">New Account</a><br />
2)Go to cloud development, and make a project.<a href="https://iot.tuya.com/cloud/">Cloud->Project</a><br />
3)Fill the details asked and make the project.<br />
4)Goto devices and turn on your device.
<br>

5)Add a device, I am using alight strip.<br />

<br>
6)Save all the details like client id,client secret key, device id, to be used in the project. Dont share these to others.
<br>
7)From the tuna_bulb_control folder you can see all the different functions available with python codes.<br>
8)Enter the client id,client secret key, device id, region code in the fields for each program which you want to execute.<br>
9)After that run the code, see that the device is online and connected to app.
<br>
<br>
<h3>Function available:</h3>
bulb_on<br>
bulb_off<br>
set_bright<br>
set_bright_v2<br>
set_color<br>
set_color_v2<br>
set_color_temp<br>
set_color_temp_v2<br>
set_work_mode<br>
state<br>
functions<br>
toggle<br>
toggle_timer<br>
<br>

<h3>Note:</h3>
The functions vary based on the light selected, so make changes accordingly.
Tutorial videos can be seen in youtube for sample ones to connect.<br>
Even i will upload a video soon to show the demo.


