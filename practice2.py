class ImageResizer:
    def __init__(self, width, height, max_width=1000, max_height=1000):
        self._width = width
        self._height = height
        self._max_width = max_width
        self._max_height = max_height

    @property
    def width(self):
        print('property from width')
        return self._width

    @width.getter
    def width(self):
        print('width.getter')
        return self._width

    @width.setter
    def width(self, value):
        print('width.setter')
        if value <= self._max_width:
            self._width = value
        else:
            raise ValueError('bad value')

    @property
    def height(self):
        print('property from height')
        return self._height

    @height.getter
    def height(self):
        print('height.getter')
        return self._height

    @height.setter
    def height(self, value):
        print('height.setter')
        if value <= self._max_height:
            self._height = value
        else:
            raise ValueError('bad value')

    @height.deleter
    def height(self):
        print('hello from deleter')
        del self._height
        #self._height = None


resizer = ImageResizer(0, 0, 1200, 1600)
# resizer.width = 10
# print(resizer.width)

print(resizer.height)
# resizer.height = 10
# del resizer.height
# del resizer.width
