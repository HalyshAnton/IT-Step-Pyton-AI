# class MyDescriptor:
#     def __get__(self, instance, owner):
#         print("Getting the attribute")
#         print(self)
#         print(instance)
#         print(owner)
#
#     def __set__(self, instance, value):
#         print("Setting the attribute")
#
#
# class MyClass:
#     attr = MyDescriptor()
#
#     @classmethod
#     def method(cls):
#         pass
#
#
# obj = MyClass()
# obj.attr

class MyDescriptor:
    def __init__(self, amount):
        print('descriptor init')
        self._amount = amount

    def __get__(self, instance, owner):
        print('descriptor get')
        return self._amount

    def __set__(self, instance, value):
        print('descriptor set')
        if value >= 0:
            self._amount = value
        else:
            raise ValueError('negative value')


class FinancialData:
    amount = MyDescriptor(10)


obj = FinancialData()
print(obj.amount)
obj.amount = 100
print(obj.amount)
