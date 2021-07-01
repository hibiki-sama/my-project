def SHA_1_068():
	sput=input("请输入消息:")
	lenth = strlen(sput)
	bit = lenth * 8
	sput,box1=PutBox(sput, box1)
	box1[bit] = 1#原始消息后添加一个"1"比特位
	if (bit < 448):
		box1=Addlast(box1, bit)
		box1=divide(box1, w)
		w=extend(w)
		w=putdata(w)
	
	else:
		Addlast(box2, bit)
		divide(box1, w)
		divide(box2, w_)
		extend(w)
		extend(w_)
		putdata(w)
		putdata(w_)
	
def PutBox(s,box):
	int i=0
	int temp#暂时保存二进制的数
	while (s[i] != '\0'):
		for ( i < lenth i++):
			int count = 0
			while (s[i] != 0):
				temp = s[i] % 2
				s[i] = s[i] / 2
				box[(i + 1) * 7 +i- count] = temp
				count++
	return s,box

def Addlast(box, bit):
	int temp
	int count = 0
	while (bit != 0):
		temp = bit % 2
		bit = bit / 2
		box[511- count] = temp
		count++
	return box
	

def divide(box, w[][8]):
	int i=0, j=0,count=0
	int sum = 0,flag=0
	while (count < 513):
		if (j == 8):
			i++
			j = 0
		     
		if (flag== 4):
			w[i][j] = sum
			flag= 0
			sum = 0
			j++
		
		if (count % 4 == 0):
			sum+=box[count] * 8
			flag++
		
		else if (count % 4 == 1):
			sum += box[count] * 4
			flag++
		
		else if (count % 4 == 2):
			sum += box[count] * 2
			flag++
		
		else if (count % 4 == 3):
			sum += box[count] * 1
			flag++
		
		count++
	return box
	

def extend(w[][8]):
	int i = 0
	long long int i_
	int t = 16
	while (t < 80):
		for (i=0 i < 8 i++):
			a |= ((unsigned int)w[t - 3][7 - i] & 0xFu) << (i * 4)
		
		for (i=0 i < 8 i++):
			b |= ((unsigned int)w[t - 8][7 - i] & 0xFu) << (i * 4)
		
		for (i=0 i < 8 i++):
			c |= ((unsigned int)w[t - 14][7 - i] & 0xFu) << (i * 4)
		
		for (i=0 i < 8 i++):
			d |= ((unsigned int)w[t - 16][7 - i] & 0xFu) << (i * 4)
		
		x = a^b^c^d
		i_ = leftbit(1, x)
		bin(w, i_, t)
		a = b = c = d = 0
		t++
	

def bin(w[][8],p,t):
	int temp
	int i = 0
	while (p != 0):
		temp = p % 16
		p = p / 16
		w[t][7 - i] = temp
		i++
	

def putdata(w[][8]):
	int i, j
	printf("w[0]:")
		for (j = 0 j < 8 j++):
			printf("%x",w[0][j])
		
		printf("\n")
		printf("w[1]:")
		for (j = 0 j < 8 j++):
			printf("%x", w[1][j])
		
		printf("\n")
		printf("w[2]:")
		for (j = 0 j < 8 j++):
			printf("%x", w[2][j])
		
		printf("\n")
		printf("w[15]:")
		for (j = 0 j < 8 j++):
			printf("%x", w[15][j])
			
		printf("\n")
		printf("w[79]:")
	for (i = 0 i < 8 i++):
		printf("%x", w[79][i])
	
	printf("\n")

if __name__=='__main__':
	SHA_1_068()
	printf("\n")




