import tensorflow as tf
from my_setup import func,val
def check_gpu():
    a=tf.test.is_gpu_available( cuda_only=False, min_cuda_compute_capability=None)
    b=tf.test.is_built_with_cuda()
    print('gpu=',a)  
    print('gpu2=',b)  
    return a,b 

if __name__=="__main__":
    #Flag1,Flag2=check_gpu()
    Flag1,Flag2=1,1
    if Flag1==True:
        print('Function imported')
        ans=func(69)
        print(f"input=69 and output={ans}")    
    print('imported val=',val)  #imported variable=val from my_setup script