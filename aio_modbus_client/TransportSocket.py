from .Transport import Transport
import asyncio


class TransportSocket(Transport):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = kwargs.get('host', '127.0.0.1')
        self.port = kwargs.get('port', 502)
        self._reader = None
        self._writer = None

    async def connect(self, serial):
        if not self._writer or self._writer._transport.is_closing():
            if not self.host:
                raise KeyError('host')
            if not self.port:
                raise KeyError('port')
            self.logger.debug(f'connection begin {self.host}:{self.port}')
            self._reader, self._writer = await asyncio.open_connection(self.host, self.port)
            self.logger.debug(f'connection complete {self.host}:{self.port}')
            return True
        return True

    async def write(self, data):
        return self._writer.write(data)

    async def read(self, size):
        return await self._reader.read(size)

    async def close(self):
        if self._writer:
            self._writer.close()
