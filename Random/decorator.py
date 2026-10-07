# experimenting on decorator -> wrapper

def adddition_modification(func):
    def addition_mod(a,b):
        res=a+b+1
        original_Result=func(a,b)
        print("original_result",original_Result,sep=':')
        print("result inside addition_mod",res,sep=':')
    return addition_mod   
   
@adddition_modification
def addition(a,b):
    res=a+b
    return res
addition(2,4)




    
        
        