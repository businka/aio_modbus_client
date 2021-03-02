# from .DataFormatter import *
from .ModbusDeviceMixin import ModbusDeviceMixin
import asyncio
# import os
# import json
import logging

_logger = logging.getLogger(__name__)


class ModbusDevice(ModbusDeviceMixin):
    file = __file__
    # formatter = DataFormatter
    pass

    def __init__(self, address, protocol, **kwargs):
        ModbusDeviceMixin.__init__(self, address, protocol, **kwargs)

    async def read_param(self, param_id):
        _logger.debug('read_param({})'.format(param_id))
        param = self.config[param_id]
        return await getattr(self, '_read_{}'.format(param['table']))(param_id, param)

    async def write_param(self, param_id, value):
        _logger.debug('write_param({})'.format(param_id))
        param = self.config[param_id]
        return await getattr(self, '_write_{}'.format(param['table']))(param_id, param, value)

    async def close(self):
        await self.protocol.close()

    async def is_device(self):
        raise NotImplemented()

    async def find_devices(self, **kwargs):
        begin = kwargs.get('begin', 1)
        end = kwargs.get('end', 253)
        begin = kwargs.get('begin', 0x6e) #1
        end = kwargs.get('end', 0x70) #253
        notify = kwargs.get('notify')
        timeout_exception = kwargs.get('timeout_exception', asyncio.TimeoutError)
        result = []
        current_slave_id = self.slave_id
        i = begin
        found = 0
        while i <= end:
            self.slave_id = i
            await notify({
                'progress': round((i - begin) * 100 / (end - begin + 1)),
                'message': f'check slave {self.slave_id} {self.__class__.__name__} ',
                'found': found
            })
            try:
                if await self.is_device():
                    result.append(self.slave_id)
                    found += 1
            except timeout_exception:
                pass
            i += 1
        self.slave_id = current_slave_id
        return result
