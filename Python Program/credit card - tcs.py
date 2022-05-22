# # class credit:
# #     def __inti__(self,cardNumber,cardHolder,nameOfBank,dOfExpiry,creditLimit):
# #         self.cardNumber = cardNumber
# #         self.cardHolder = cardHolder
# #         self.nameOfBank = nameOfBank
# #         self.dOfExpiry = dOfExpiry
# #         self.creditLimit = creditLimit
        
# #     def check(self):
        
from datetime import datetime
# userNumber = int(input())
# lists = []
# for i in range(0,userNumber):
#     tempList = []
#     cardNumber = input()
#     tempList.append(cardNumber)
#     cardHolder = input()
#     tempList.append(cardHolder)
#     nameOfBank = input()
#     tempList.append(nameOfBank)
#     dOfExpiry = str(input())
#     dOfExpiry = datetime.strptime(dOfExpiry,"%d-%m-%Y")
#     tempList.append(dOfExpiry)
#     cardBalance = int(input())
#     tempList.append(cardBalance)
#     creditlimit = int(input())
#     tempList.append(creditlimit)
#     lists.append(tempList)
# amountToBePaid = int(input("Enter the amount: "))
# dateOfPay = datetime.strptime(str(input()),"%d-%m-%Y")
# for i in lists:
#     for j in i:
#         if(amountToBePaid<=i[4] and dateOfPay<=i[3]):
#             res = i[4]+amountToBePaid
#             print(i[0],end=",")
#             print(i[5]-res,end=",")
#             print(res)
#             break
#         else:
#             print("Payment Not Completed")

    
class cc:
     def __inti__(self,cn,noch,nob,doe,cb,cl):
         self.cn = cn
         self.noch = noch
         self.nob = nob
         self.doe = doe
         self.cb = cb
         self.cl = cl
def fun1(locc, amount,dop):
    locc.sort(key=lambda x:x.cl-x.cb,reverse = True)
    for i in locc:
        if(i.cl-i.cb>=amount):
            if(doe>dop):
                continue
            else:
                return i
    return None
n = int(input())
locc = []
for l in range(n):
    cn = input()
    noch = input()
    nob= input()
    doe = input()
    doe = datetime.strptime(doe,"%d-%m-%Y")
    cb = int(input())
    cl = int(input())
    locc.append(cc.__inti__(cn,noch,nob,doe,cb,cl))
    
amount = int(input())
dop = input()
dop= datetime.strptime(dop,"%d-%m-%Y")
t = fun1(locc,amount,dop)
if t==None:
    print("Payment not Completed")
else:
    print('Card Details after Payment')
    print('{0},{1},{2}'.format(t.cn,t.cl,t.cb-amount,t.cb+amount))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    