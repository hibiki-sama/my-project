import random
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
		first=pow(a,t,num)
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

if __name__=='__main__':
	if (millerRabin(2071)):
		print('yepe')
	else:
		print('nope')
