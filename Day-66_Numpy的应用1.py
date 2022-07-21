# -*- coding: utf-8 -*-

"""
@Date : 2022/7/21 21:03

@Author : Administrator

@File : Day-66_Numpy的应用1.py

@Software : PyCharm

@Desc :

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 一维数组
# 方法1 使用array 函数，通过List创建数组对象

array1 = np.array([1,2,3,4,5])
array1

# 方法2：使用arange函数，指定取值范围创建数组对象
array2 = np.arange(0,20,2)

# 方法3：使用linspace函数，用指定范围均匀间隔的数字创建数组对象
array3 = np.linspace(-5,5,101)

# 方法4：使用numpy.random 模块的函数生成随机数创建数组对象产生10个[0,1)范围的随机小数
array4 = np.random.rand(10)

array5 = np.random.randint(1,100,10)

# 产生20个μ=50 ，西格玛=10 的正态分布随机数
array6 = np.random.normal(50, 10, 20)

# 说明：创建一维数组还有很多其他的方式，比如通过读取字符串、读取文件、解析正则表达式等方式，这里我们暂不讨论这些方式，有兴趣的读者可以自行研究。

# 二维数组

# 方法一：使用array函数，通过嵌套的list创建数组对象
array7 = np.array([[1,2,3],[4,5,6]])

# 方法二：使用zeros、ones、full、函数指定数组的形状创建数组对象
# 使用zeros 函数，代码：
array8 = np.zeros((3,4))

# 使用ones函数
array9 = np.ones((3,4))

# 使用full函数, 代码：
array10 = np.full((3,4), 10)

# 方法三：使用eye函数创建单位矩阵
array11 = np.eye(4)

# 方法四：通过reshape将一维数组变成二维数组
array12 = np.array([1,2,3,4,5,6]).reshape(2,3)
# 提示：reshape是ndarray对象的一个方法，使用reshape方法时需要确保调形后的数组元素个数与调形前数组元素个数保持一致，否则将会产生异常

# 方法五：通过numpy.random模块的函数生成随机数创建数组对象产生[0,1)范围的随机小数构成的3行4列的二维数组
array13 = np.random.rand(3,4)
# 产生[1,100)范围的随机整数构成的3行4列的二维数组，代码
array14 = np.random.randint(1, 100, (3, 4))

# 多维数组
# 使用随机的方式创建多维数组
array15 = np.random.randint(1,100,(3,4,5))
array51 = np.random.randint(1,100,(3,4,5,6))

# 将一维二维的数组调形为多维数组
array16 = np.arange(1, 25).reshape((2,3,4))

# 二维数组调形为多维数组
array17 = np.random.randint(1, 100, (4, 6)).reshape((4,3,2))

# 读取图片获得对应的三维数组
array18 = plt.imread("guido.jpg")
# 说明：上面的代码读取了当前路径下名为guido.jpg 的图片文件，计算机系统中的图片通常由若干行若干列的像素点构成，而每个像素点又是由红绿蓝三原色构成的，所以能够用三维数组来表示。读取图片用到了matplotlib库的imread函数。

"""
数组对象的属性
"""

# 1. size 属性：数组元素个数

array19 = np.arange(1, 100, 2)
array20 = np.random.rand(3,4)
# print(array19.size, array20.size)
# 50 12
# 2. shape 属性：数组的形状
# print(array19.shape, array20.shape)
# (50,) (3, 4)

# 3. dtype属性：数组元素的数据类型
print(array19.dtype, array20.dtype)
# int32 float64

# 4. ndim属性：数组的维度
print(array19.ndim, array20.ndim)
# 1 2

# 5. itemsize属性：数组单个元素占用内存空间的字节数
array21 = np.arange(1, 100, 2, dtype=np.int8)
print(array19.itemsize, array20.itemsize, array21.itemsize)
# 4 8 1
# 说明：在使用arange创建数组对象时，通过dtype参数指定元素的数据类型。可以看出，np.int8代表的是8位有符号整数，只占用1个字节的内存空间，取值范围是。

# 6. nbytes 属性：数组所有元素占用内存空间的字节数
print(array19.nbytes, array20.nbytes, array21.nbytes)
# 200 96 50

# 7. flat 属性： 数组（一维化之后）元素的迭代器 ??
from typing import Iterable
print(isinstance(array20.flat, np.ndarray), isinstance(array20.flat, Iterable))

# False True

# 8. base 属性：数组的基对象（如果数组共享了其他数组的内存空间）？？
array22 = array19[:]
print(array22.base is array19, array22.base is array21)
# True False
# 说明：上面的代码用到了数组的切片操作，它类似于 Python 中list类型的切片，但在细节上又不完全相同，下面会专门讲解这个知识点。通过上面的代码可以发现，
# ndarray切片后得到的新的数组对象跟原来的数组对象共享了内存中的数据，因此array22的base属性就是array19对应的数组对象。

"""
数组的索引和切片
"""
