class UserMainCode(object):
    def nthPrime(cls,input1):
        c = 0
        num = 2
        result = 0
        while (c != input1):
           count = 0
           for i in range(2,num):
              if (num % i == 0):
                 count+=1
                 break
           if (count == 0):
              c+=1
              result = num
           num = num + 1
        return result
        
# userInput=int(input())
# print(UserMainCode.nthPrime(1,userInput))

