def get_image_by_id(i):
    pass
def get_images(n):
    result = []
    for i in range(n):
        result.append(get_image_by_id(i))
    return result
images = get_images(n)


image_id = -1
def next_image():
    global image_id
    image_id += 1
    return get_image_by_id(image_id)
image0 = next_image()
image1 = next_image()


class ImageRepository:
    def __init__(self):
        self.image_id = -1
    def next_image(self):
        self.image_id += 1
        return get_image_by_id(self.image_id)

repo = ImageRepository()
image0 = repo.next_image()
image1 = repo.next_image()


# 实现__iter__ __next__方法把它变成iterator
class ImageRepository:
    def __init__(self):
        self.image_id = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.image_id += 1
        return get_image_by_id(self.image_id)

for image in ImageRepository():
    pass


# 在python中，只要一个函数使用了yield这个关键字，就代表这个函数是一个生成器generator
# yield的作用相当于让python帮我们把一个串行的逻辑转换成iterator的形式
def image_repository():
    image_id = -1
    while True:
        image_id += 1
        yield get_image_by_id(image_id)

for image in image_repository():
    pass

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = b, a+b
fibos = fibonacci()
next(fibos)
next(fibos)

class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
fibos = Fibonacci()
next(fibos)
next(fibos)

def generator():
    print('1')
    yield 
    print('2')
    yield
    print('3')
    yield

x = generator()
next(x)
next(x)


class API:
    def call_this_first():
        pass
    def call_this_second():
        pass
    def call_this_last():
        pass

def api():
    first()
    yield
    second()
    yield
    last()


def averager():
    sum = 0
    num = 0
    while True:
        sum += (yield sum / num if num > 0 else 0)
        num += 1

x = averager()
x.send(None)
x.send(1)
x.send(2)
x.send(3)

class Averager:
    def __init__(self):
        self.num = 0
        self.num = 0
    
    def avg_num(self, n):
        self.sum += n
        self.num += 1
        return self.sum / self.num

averager = Averager()
averager.avg_num(1)
averager.avg_num(2)
averager.avg_num(3)

def odds(n):
    for i in range(n):
        if i % 2 == 1:
            yield i

def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield if

def odd_even(n):
    for x in odds(n):
        yield x
    for x in evens(n):
        yield x

for x in odd_even(6):
    print(x)

def odd_even(n):
    yield from odds(n)
    yield from evens(n)








