import os
import setuptools
modulelist = os.listdir("src")
modulelistclean =[]
print(modulelist)
for i in modulelist[:-1]:
    i = i.split(".")[0]
    modulelistclean.append("src/"+i)
    
setuptools.setup(
    name='VSAG', # 包的名字，可随意取
    py_modules=modulelistclean # 对应hello.py，也是安装了包之后实际import的名字
)
