import pandas as pd

mydataset = {
    'car':["Bmw","Volvo","Ford"],
    'passing':[3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print(pd.__version__)

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)