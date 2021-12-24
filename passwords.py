import random
import string

print('Hello, Welcome to Password generator!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)
password = "".join(temp)

all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,length))

print(password)

#SAMPLE O/P: (length = 16)
#3Atza*qP#h-vJoK+
#7c%A4gOt#M[}qr2
#@JmFf"awbQ1Ts4dx