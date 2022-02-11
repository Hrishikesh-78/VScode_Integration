import numpy as np
val=500
def func(x):
    return x**2    

print('Name=',__name__)

if __name__=='__main__':
    print('runs when executed directly')
    ans=func(5)
    print(f"My input=5 and output={ans}")
else:
    print('runs when imported')        