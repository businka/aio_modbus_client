The main purpose is to create classes of devices connected via modbus by describing their properties.

Not intended to transfer bytes to modbus.

The library allows you to organize work with devices connected to a TCP modbus server, and a serial port. It also assumes the possibility of having devices operating at different speeds and different connection parameters on the bus.

Use
---

1. Create your class inheriting from ModbusDevice. It is important to specify the static variable file in your class file = __file__
2. Create a JSON file with the description of the registers of your device
3. To access the device, use an instance of your class and the package API.

see example: example / Wirenboard / TestWirenBoardDimmer.py

if someone likes the implementation, I will add documentation

async API
---------

read_param(param_id) - gets device property value

write_param(param_id, value) - writes the value to the property of the device

is_device() - should return true if the device at the current address can be served by this class

find_devices() - returns the list of addresses of these devices. The function calls is_device for each modbus address.

Licensing
---------

aiocoap is published under the Apache License 2.0, see LICENSE_ for details.


Copyright (c) 2019 Mikhail Razgovorov

In my work, the code of another library was used to serialize the protocol, unfortunately during the implementation I forgot which one. I apologize to the author. Ready upon request to specify his name here.

.. _LICENSE: LICENSE
