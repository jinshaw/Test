class Count:
     def __init__(self,a,b):
         self.a= int(a)
         self.b= int(b)

     def add(self):
        return self.a+self.b

     def sub(self):
         return self.a-self.b

class Prime:
    def __init__(self,n):
        self.n= int(n)

    def is_prime(self):
        p=self.n
        if p <=1:
            return  False
        for i in range(2,p):
            if p % i == 0:
                return  False
        return True
