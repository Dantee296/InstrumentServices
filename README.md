# InstrumentServices 
***
> Name: frank francis          Contact way: descosmos@163.com

## Features
***
InstrumentServices is a cross-platform software library used to monitor the apple device without jailbeaking.
Indeed, the internal part of InstrumentServices are libimobiledevice, libplist, usbmuxd and openSSL.

## Developing Enviorment
***
> The InstrumentServices has built libimobiledevice.dll, libplist.dll and other nessceary dynamic linking library file sucessfully,
    Therefore, developer don not need to rebuild these files twice.
- pthon:      python3.7.7
- os:         windows10
- compiler:   pycharm Community Edition 2020.3.2

## Project catalogue
***
- byplist
- libimobiledevice
- zeroconfig
- _init_.py
- afc_service.py
- afc_service_unittesting.py
- app.py
- device_manager.py
- device_manager_unittesting.py
- device_service.py
- device_service_unittesting.py
- diagnostics_relay_service.py
- dtxlib.py
- house_arrest_proxy_service.py
- house_arrest_proxy_service_test.py
- image_mounter_service.py
- image_mounter_service_unittesting.py
- installation_proxy_service.py
- installation_proxy_service_unittesting.py
- instrument_service.py
- lockdown_service.py
- lockdown_service_uinttesting.py
- screenshotr_service_py
- screenshotr_service_unittesting.py
- service.py
- spring_board_service.py
- spring_board_service_unittesting.py
- syslog_realy_service.py
- syslog_relay_service_unittesting.py
- test.py
- utils.py
- utils_unittesting.py

## Usage 
***
Every availiable command can be sent to IOS device by using app.py.
### app.py

#### Utilities
The libirary bundles the following command-line utilities in the tools directory:
| Utility     |     Description     |
| :---------- |  ------------------:|
| devices     | Illustrate the device ID and the type of connection(wireless, USB) |
| applications| List all applications of the device |
| deviceinfo  | Illustrate the information of device(including device_name, cpu_type and so on) |
| syslog      | Print the syslog    |
| ls          | List all connected-device id |
| mkdir       | Create a new directory in device |
| rm          | Remove a file from the device |
| pull        | Pull the specific file from the device |
| push        | Push the specific file to the device |
| lookupimage | Look for images in device and print it |
| mountimage  | Mount an image to device |
| screenshot  | The device operate Screenshot, and the image is saved in current directory |
| geticon     | Get icons from device |
| getvalue    | Get all accessiable values from device, and print it |
| instrument  | Establish the instrument service, after that, sending some specific commands are availiable |
| diagnostics | Request the information of diagnosis from device |
| enableWireless | Enable wireless mode in device |
| heartbeat   | In order to take commnunication via network by Sending "heartbeat" to device |
| install     | Install an application in device |
| uninstall   | Uninstall an application in device |

Please consult th usage information or manual pages of each utility for a documentation of avaliable command
line options and usage examples like this:
'''
python.exe app.py
'''
### instrument_service.py

#### Utilities
The libirary bundles the following command-line utilities in the tools directory:
| Utility     |     Description     |
| :---------- | :|
| channels    | List all aviliable channels in device |
| sysmontap   | Illustrate the CPU_INST_NAME_11 data |
| graphics    | Illustrate the GPU data |
| running     | Get name of all active processes in device and print that |
| codec       | Codec files in device and print it |
| timeinfo    | Get MachineTimeInfo of device and print it |
| execname    | Get name of pid |
| activity    | List activity information of pid |
| networking  | Inllustrate the information of network in device |
| energy      | Monitor energy of pid |
| netstat     | List network-IO data of pid |
| kill        | Kill a specific process |
| launch      | Launch a specific process |
| monitor     | Monitor a specific process |
| corprofile  | List the information of core dynamically |
| power       | Print power of device |
| wireless    | Check the state of wireless mode and print it |
| test        | Just for test |

Please consult th usage information or manual pages of each utility for a documentation of avaliable command
line options and usage examples like this:
'''
python.exe instrument_service.py
'''

## Links
***
- libimobiledevice Repository: [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)
- usbmuxd Repository: [usbmuxd](https://github.com/libimobiledevice/usbmuxd)
- libplist Repository: [libplist](https://github.com/libimobiledevice/libplist)
- openSSL Repository: [openSSL](https://github.com/openssl/openssl)

## Document
***
> Documents for analyse the functions or class in each py file.


