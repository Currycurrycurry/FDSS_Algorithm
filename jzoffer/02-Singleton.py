# 设计一个类，我们只能生成该类的一个实例
def singleton(cls):
    _instance = dict()
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
            return _instance(cls)
    return inner

@singleton
class Cls(object):
    def __init__(self):
        pass

cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))

##############################
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@Singleton
class Cls2(object):
    def __init__(self):
        pass

# 用法1
cls1 = Cls2()
cls2 = Cls()
print(id(cls1) == id(cls2))

# 用法2
Cls3 = Singleton(Cls3)
cls3 = Cls3()
cls4 = Cls3()
print(id(cls3) == id(cls4))

##############################
class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        pass

single1 = Single()
single2 = Single()
print(id(single1) == id(single2))

##############################
# meta class type
def func(self):
    print("///")
Klass = type("Klass",(),{"func":func})

c = Klass()
c.func()
# 将metaclass指向Singleton类 让Singleton中的type来创造新的Cls4实例
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kargs)
        return cls._instances[cls]

class Cls4(metaclass=Singleton):
    pass

cls1 = Cls4()
cls2 = Cls4()
print(id(cls1)==id(cls2))
