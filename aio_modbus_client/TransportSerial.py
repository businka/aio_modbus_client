from .Transport import Transport
from serial_asyncio import open_serial_connection


class TransportSerial(Transport):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = kwargs.get('host', 'COM3')
        # self.baud_rate = kwargs.get('baudRate', 9600)
        # self.parity = kwargs.get('parity', 0)
        # self.data_bits = kwargs.get('dataBits', 8)
        # self.stop_bits = kwargs.get('stopBits', 1)
        self._reader = None
        self._writer = None

    async def connect(self, serial):
        try:
            if not self._reader:  # todo check change serial speed
                self._reader, self._writer = await open_serial_connection(
                    url=self.url,
                    baudrate=serial['baudRate'],

                )
                return True
            return True
        except Exception as e:
            raise Exception(str(e)) from None

    async def write(self, data):
        return self._writer.write(data)

    async def read(self, size):
        return await self._reader.read(size)

    async def close(self):
        if self._writer:
            self._writer.close()