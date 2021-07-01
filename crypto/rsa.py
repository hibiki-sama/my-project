def Square_51(a_51,m_51,n_51):# 平方—乘算法
    # 十进制转二进制
    H = bin(m_51)
    H = H.replace('0b','')  # 去除系统自带的 0b
    H = str(H)  # 转成字符串
    # 初始化
    result =a_51
    print("第 0 步,i= 1 result=",result)
    for index in range(1, len(H)):
        result = result ** 2 % n_51   
        if H[index] == '1':
            result = result * a_51 % n_51
        print("第",index,"步","i=",H[index],"result=",result)
    return result

def Modular_51(a_51,m_51,n_51):#模重复平方算法
	# 十进制转二进制
    H = bin(m_51)
    H = H.replace('0b','')  # 去除系统自带的 0b
    H = str(H)  # 转成字符串
    mm=a_51
    result=1
    for index in range(len(H)-1,-1,-1):   
        if H[index] == '1':
            result = result * mm % n_51
        mm = a_51 ** pow(2,len(H)-index) % n_51
        print("第",len(H)-1-index,"步","i=",H[index],"a=",result,"b=",mm)
    return result

if __name__ == "__main__":
	a,m,n=map(int,input('输入a,b,c:').split())
	print("平方—乘算法结果为",Square_51(a,m,n),"\n")
	print("模重复平方算法结果为",Modular_51(a,m,n))
