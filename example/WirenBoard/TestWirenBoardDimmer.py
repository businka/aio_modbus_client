import unittest
import asyncio
import socket
# from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
from example.WirenBoard import async_test
from example.WirenBoard import WirenBoardDimmer as Device
# from buject.ModbusUsrTcp232.backup.ModbusTcpUsr340 import ModbusTcpUsr340 as Modbus
# from aio_modbus_client.ModbusTcpHF5111 import ModbusTcpHF5111 as Modbus
from aio_modbus_client.TransportSocket import TransportSocket as Modbus
from aio_modbus_client.ModbusProtocolRtuHF5111 import ModbusProtocolRtuHF5111 as Protocol
import logging


class TestWirenBoardDimmer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)
        cls.slave_id = 0x78
        cls.address = ('192.168.1.25', 502)
        cls.device = Device(cls.slave_id, Protocol(Modbus(host=cls.address[0], port=cls.address[1])))

    def setUp(self):
        pass

    @async_test
    async def tearDown(self):
        await self.device.close()

    @async_test
    async def test_read_brightness_blue(self):
        result = await self.device.read_param('level_blue')
        print(result)
        result = await self.device.read_param('color')
        print(result)
        pass

    def test_write_brightness_blue(self):
        # self.device.modbus = ModbusTcpChinaGarbage(self.address, framer=ModbusFramer)
        result = self.device.write_param('level_green', 0)
        pass

    @async_test
    async def test_color(self):
        color = [20, 20, 20]
        await self.device.write_param('color', color)
        self.assertEqual(self.device.data['color'], color)
        result = await self.device.read_param('color')
        self.assertEqual(result, color)
        self.assertEqual(self.device.data['color'], color)

    def test_power(self):
        color = [20, 25, 30]
        self.device.write_param('power', False)
        self.assertEqual(self.device.data['power'], False)
        result = self.device.read_param('power')
        self.assertEqual(result, False)
        self.device.write_param('color', color)
        self.device.write_param('power', False)
        result = self.device.write_param('power', True)
        self.assertEqual(self.device.data['color'], color)

    @async_test
    async def test_brightness(self):
        # color = [255, 255, 255]
        brightness = 5
        await self.device.write_param('power', False)
        await asyncio.sleep(1)
        pass
        # self.assertEqual(self.device.data['power'], False)
        # result = self.device.read_param('brightness')
        # self.assertEqual(result, 100)

        # self.device.write_param('power', True)
        await self.device.write_param('brightness', brightness)
        pass
        result = self.device.read_param('brightness')
        pass
        # self.assertEqual(self.device.data['power'], False)
        pass

        # self.device.write_param('brightness', 20)
        # self.device.write_param('brightness', 40)
        # self.device.write_param('brightness', 60)
        # self.device.write_param('brightness', 80)
        # self.device.write_param('brightness', 100)
        # self.assertEqual(self.device.data['brightness'], brightness)
        # self.assertEqual(result, brightness)
        # result = self.device.write_param('power', False)
        # self.device.write_param('brightness', brightness)
        # result = self.device.read_param('brightness')
        # result = self.device.write_param('power', True)
        # self.assertEqual(self.device.data['color'], color)

    def test_get_brightness_by_color(self):
        result = self.device.get_brightness_from_color([255, 255, 255])
        self.assertEqual(100, result)

    def test_get_version(self):
        value = self.device.read_param('version')
        pass
        # self.assertEqual(100, result)

    @async_test
    async def test_read_model(self):
        # self.device.modbus.connect()
        value = await self.device.read_param('model')
        self.assertEqual(value, 'WBMRGB')
        print(value)

    def test_find(self):
        # self.device.modbus.connect()
        value = self.device.find_devices()
        self.assertEqual(value, 'WBMRGB')
        print(value)

    def test_id_device(self):
        # self.device.modbus.connect()
        self.device.transport.timeout = 0.5
        value = self.device.is_device()
        self.assertEqual(value, True)
        print(value)

    def test_simple(self):
        sock = socket.socket()
        sock.connect(self.address)
        # data = b'\x01\x03\x00\x00\x00\x06\x82\x04\x00\xc8\x00\x06'
        # sock.send(data)
        # print(sock.recv(1900))
        data = b'\x82\x04\x00\xc8\x00\x06\xee\x05'
        sock.send(data)
        print(sock.recv(1900))
        sock.close()
        pass
