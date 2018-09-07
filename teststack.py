import Stack_pfix as st
pfix=st.stack()
exp=list(input('Please Enter a Post Fix Expression \n'))

for i in range(len(exp)-1):
    if (exp[i] == '1') or (exp[i] =='2') or (exp[i] =='3') or (exp[i] =='4') or (exp[i] =='5') or (exp[i] =='6') or (exp[i] =='7') or (exp[i] =='8') or (exp[i] =='9') or (exp[i] =='0'):
          pfix.push(int(exp[i]))
    elif (exp[i]=='+'):
          num1=pfix.pop()
          num2=pfix.pop()
          num3=num1+num2
          pfix.push(num3)
    elif (exp[i]=='-'):
          num1=pfix.pop()
          num2=pfix.pop()
          num3=num2-num1
          pfix.push(num3)
    elif (exp[i]=='*'):
          num1=pfix.pop()
          num2=pfix.pop()
          num3=num1*num2
          pfix.push(num3)
    elif (exp[i]=='/'):
          num1=pfix.pop()
          num2=pfix.pop()
          num3=num2/num1
          pfix.push(num3)

pfix.pop()
print('The Result is ')
pfix.PrintStack()
        


