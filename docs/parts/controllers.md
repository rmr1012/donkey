# Controller Parts

## Local Web Controller

The default controller to drive the car with your phone or browser. This has a web live preview of camera. Control options include:

1. A virtual joystick
2. The tilt, when using a mobile device with supported accelerometer
3. A physical joystick using the web adapter. Support varies per browser, os, and joystick combination.


## Physical Joystick Controller

The default web controller may be replaced with a one line change to use a physical joystick part for input. This uses the os device /dev/input/js0 by default. In theory, any joystick device that the os mounts like this can be used. In practice, the behavior will change depending on the model of joystick ( Sony, or knockoff ), or XBox controller and the bluetooth driver used to support it. The default code has been written and tested with a [Sony brand PS3 Sixaxis controller](https://www.amazon.com/Dualshock-Wireless-Controller-Charcoal-playstation-3). Other controllers may work, but will require alternative bluetooth installs, and tweaks to the software for correct axis and buttons.

These can be used plugged in with a usb cable - but the default code and os driver has a bug polling this configuration. It's been much more stable, and convenient, to setup bluetooth for a wireless, responsive control.

### Change to config.py or run with --js

```
python manage.py drive --js
```

Will enable driving with the joystick. This disables the live preview of the camera and the web page features. If you modify config.py to make USE_JOYSTICK_AS_DEFAULT = True, then you do not need to run with the --js.

### Bluetooth Setup

Follow [this guide](https://pythonhosted.org/triangula/sixaxis.html). You can ignore steps past the 'Accessing the SixAxis from Python' section. I will include steps here in case the link becomes stale.

``` bash
sudo apt-get install bluetooth libbluetooth3 libusb-dev
sudo systemctl enable bluetooth.service
sudo usermod -G bluetooth -a pi
```

Reboot after changing user group.

Plug in the PS3 with usb cable. Hit center PS logo button. Get and build the command line pairing tool. Run it:

```bash
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb
sudo ./sixpair
```

Use bluetoothctl to pair
```bash
bluetoothctl
agent on
devices
trust <MAC ADDRESS>
default-agent
quit
```

Unplug USB cable. Hit center PS logo button.

To test that the Bluetooth PS3 remote is working, verify that /dev/input/js0 exists.

```bash
ls /dev/input/js0
```

### Charging PS3 Sixaxis Joystick

For some reason, they don't like to charge in a powered usb port that doesn't have an active bluetooth control and os driver. So a phone type usb charger won't work. Try a powered linux or mac laptop usb port. You should see the lights blink after plugging in and hitting center PS logo.

After charging, you will need to plug-in the controller again to the Pi, hit the PS logo, then unplug to pair again.

### New Battery for PS3 Sixaxis Joystick

Sometimes these controllers can be quite old. Here's a link to a [new battery](http://a.co/5k1lbns). Be careful when taking off the cover. Remove 5 screws. There's a tab on the top half between the hand grips. You'll want to split/open it from the front and try pulling the bottom forward as you do. Or you'll break the tab off as I did.