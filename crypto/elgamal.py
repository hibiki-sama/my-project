import random

def powmod(a,b,c):#快速幂取余
	ans = 1
	a = a % c
	while(b>0):
		if(b % 2 == 1):
			ans = (ans * a) % c;
		b = b//2
		a = (a * a) % c
	return ans
def Protogen(p):#寻找本原根
	a=[];
	for i in range(1,p):#//获取p-1的所有因子
		if((p-1)%i==0):
			a.append(i)
	n=0
	while(True):
		n=n+1
		x=-1
		for j in range(len(a)):#求阶,如果阶==p-1，那就是原根
			if(powmod(n,a[j],p)==1):
				x=a[j]
				break
		if(x==p-1):
			break
	print('the Protogen is',n)
	return n
def Inverse(y1,key,p):#求逆元
	x=powmod(y1,key,p)
	i=0
	while(True):
		i=i+1
		if((i*x)%p==1):
			return i
def en(msg,p,y,g):
	k=random.randint(2,p-2)
	y1=powmod(g,k,p)
	y2=powmod(y,k,p)
	y2=(y2*msg)%p
	print('The two encrypted numbers are',y1,"and",y2)
	return y1,y2
def de(y1,y2,key,p):
	h=Inverse(y1,key,p)
	msg=(y2*h)%p
	print('the message is',msg)
def Largeprime(ksize=20):#生成一个素数，ksize用来调整位数
	while True:
		num = random.randrange(2**(ksize - 1),2**(ksize))
		if (isPrime(num)):
			return num
def isPrime(num):#简单素性检测
	if (num<2):
		return False
		
	lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
                 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
                 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
                 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
                 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
                 983, 991, 997]

	if num in lowPrimes:
		return True

	for prime in lowPrimes:
		if num % prime == 0:
			return False

	return millerRabin(num)
def millerRabin(num):#Miller-Rabin 素性检测算法
	safetime=10#素性检测次数
	temp=num-1
	s=0
	t=0
	while(temp%2==0):#计算n-1=2^s*t中的S
		s=s+1
		temp=temp//2
	t=temp#得到t
	for i in range(safetime):
		a=random.randrange(2,num-1)
		first=powmod(a,t,num)
		if(first==1 or first==num-1):
			continue
		else:
			so=first
			for j in range(1,s+1):
				so=(so**2)%num
				if(so==num-1):
					break
			if(j==s):
				return False
	return True

p=Largeprime()
print("Random prime number is",p)
print("please input your key in the range 2 ~",p-2)
key=int(input())
print("please input your message")#msg应为整数
msg=int(input())

g=Protogen(p)
y=powmod(g,key,p)
print("The public key is",y)
y1,y2=en(msg,p,y,g)
de(y1,y2,key,p)
