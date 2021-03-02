import asyncio
from .ModbusProtocolRtu import ModbusProtocolRtu
import logging
_logger = logging.getLogger(__name__)


class Transport:
    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger', _logger)
        pass

    async def connect(self, serial):
        pass

    async def send(self, data):
        pass

    async def receive(self, size):
        pass

    async def close(self):
        pass
