
import urllib.request
import timeit

class Cache:
    myvar = 1

def foo():
    Cache.myvar = 2

def main():

    from sys import version
    print(version)

    a = "1"
    print(a.isdigit())

    c = "1"

    print(float(a) + float(c))

    b = "963spam"
    print(b.isdigit())

    d = 1
    print(float(d))

    foo()
    print(Cache.myvar)

    l = [(1,2), (3,4)]
    print(str(l).strip('[]'))

    a = []
    if not a:
        print("List is empty")

    l1 = [1, 2, 3]
    l2 = l1
    del l1[:]
    print(l2)

    a = ['TRC/WS']
    a = ''.join(a)
    if '/' in a:
        a = a.replace('/', '.')
        b = []
        b.append(a)
    print(b)

    response = urllib.request.urlopen("http://financials.morningstar.com/ajax/ReportProcess4CS  V.html?&t=ZBB&region=usa&culture=en-US&cur=USD&reportType=is&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=859833&denominatorView=raw&number=1")
    htmlStatus = response.status
    print(htmlStatus)
    if htmlStatus != 200:
        print(htmlStatus)

    a = 'hello'
    try:
        if 'hello' == a:
            print('yup')
    except:
        print('error')
    else:
        print('in try-else statement')

    a = '{percent:.4%}'.format(percent=float(1) / float(3))
    print(a)

    from datetime import datetime
    a = str(datetime.now())
    print(a)

    from math import sqrt
    a = 5 + sqrt(12)
    print(a)


    return

#main()


print(str(timeit.timeit(stmt='main()', setup='from __main__ import main', number=1)) + ' seconds')


# eval() lets a python program run python code within itself.
# Below is an example of how to use eval()
def test():
    user_func = input("type a function: y = ")
    for x in range(1,10):
        print("x = ", x , ", y = ", eval(user_func))
    return

from math import *
test()