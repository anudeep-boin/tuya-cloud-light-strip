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


#Sets the brightness of device, Range is 25-255
bulb.set_bright(value=25)