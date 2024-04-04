# cache = {(method_name, args, kwargs): result}


class MyMeta(type):
    cache = {}

    def __new__(cls, name, bases, dct):
        for method_name, method in dct.items():
            if callable(method):
                dct[method_name] = cls.cache_decor(method)

        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def cache_decor(method):
        def decord_method(*args, **kwargs):
            cache_data = (method.__name__, *args, tuple(kwargs.items()))

            if cache_data in MyMeta.cache:
                print('Known data')
                return MyMeta.cache[cache_data]

            print("New data")
            result = method(*args, **kwargs)
            MyMeta.cache[cache_data] = result
            return result

        return decord_method


class InfoSystem(metaclass=MyMeta):
    def add(self, num1, num2):
        return num1 + num2


obj = InfoSystem()
print(obj.add(2, 2))
print(obj.add(2, 2))
print(obj.add(3, 5))
print(obj.add(3, 3))
print(obj.add(2, num2=2))
print(obj.add(2, num2=2))

for data, result in MyMeta.cache.items():
    print(data, result)