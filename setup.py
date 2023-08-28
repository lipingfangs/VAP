import os
import setuptools
modulelist = os.listdir("src")
modulelistclean =[]
print(modulelist)
for i in modulelist[:-1]:
    i = i.split(".")[0]
    modulelistclean.append("src/"+i)
    
setuptools.setup(
    name='VAP',
    py_modules=modulelistclean 
)
