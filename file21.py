import mymodule

s = mymodule.sum( 10 , 20 )
print(s)

print(mymodule.my_var)

mymodule.show()

from mymodule import show,my_var,sum
show()
print(my_var)
s = sum( 1000 , 2000 )
print(s)
import mymodule
import importlib
importlib.reload(mymodule)
import numpy

arr = numpy.array([10,20,30,40,50])

print(arr.sum())
import hbagecalculator
import datetime
Year = int(input("ENTER THE YEAR YOU WERE BORN : "))
age= datetime.datetime.now().year-Year
print("YOUR ARE ", age, "YEARS OLD")

from audioplayer import AudioPlayer

AudioPlayer("censor-beep-1sec-8112.mp3").play(block=True)
