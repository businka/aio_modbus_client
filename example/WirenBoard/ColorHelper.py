
class ColorHelper:

    @classmethod
    def get_percent_brightness_from_color(cls, color):
        return int(round(cls.get_gray_by_color(color) * 100 / 255))

    @classmethod
    def get_gray_by_color(cls, color):
        return int(round(0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]))

    @classmethod
    def get_clear_color_by_color(cls, color):
        rate = sorted(color, reverse=True)[0] / 255
        result = []
        for elem in color:
            result.append(int(round(elem / rate)))
        return result

    @classmethod
    def get_rate_color(cls, color, rate):
        result = []
        for elem in color:
            result.append(int(round(elem * rate / 100)))
        return result
