from aio_modbus_client.ModbusDevice import ModbusDevice
from .ColorHelper import ColorHelper
import copy


class WirenBoardDimmer(ModbusDevice):
    file = __file__

    async def _read_calc_color(self, param_id, param):
        _color = await self._read_holding(param_id, param)
        color = [_color[1], _color[0], _color[2]]
        color = self._on_change_color(color)
        return color

    def _on_change_color(self, color):
        _power = max(*color) != 0
        if _power:
            _color = copy.deepcopy(color)
        else:   # black
            _color = copy.deepcopy(self.data.get(
                'color',
                self.get_default_param_value('color')
            ))
        self._change_data({
            'power': _power,
            'brightness': ColorHelper.get_percent_brightness_from_color(_color),
            'color': _color
        })
        return color

    async def _write_calc_color(self, param_id, param, value):
        _value = [value[1], value[0], value[2]]
        await self._write_holding(param_id, param, _value)
        self._on_change_color(value)
        return True

    async def _read_calc_power(self, param_id, param):
        return await self.is_power_on()

    async def _write_calc_power(self, param_id, param, value):
        _power = await self.is_power_on()
        if value == _power:
            return value
        if value:
            await self.write_param('color',  self.data['color'])
        else:
            await self.write_param('color', [0, 0, 0])
        return True

    async def _read_calc_brightness(self, param_id, param):
        self.read_param('color')
        return self.data['brightness']

    async def _write_calc_brightness(self, param_id, param, value):
        await self.is_power_on()
        _color = ColorHelper.get_clear_color_by_color(self.data['color'])
        _color = ColorHelper.get_rate_color(_color, value)
        await self.write_param('color',  _color)
        # if not _power:
        #     self.write_param('color', [0, 0, 0])
        return True

    async def is_power_on(self):
        await self.read_param('color')
        return self.data['power']

    async def is_device(self):
        result = await self.read_param('model')
        if result in ['WBMRGB']:
            return True
        return False

