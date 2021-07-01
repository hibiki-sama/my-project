
import vigenerecipher
 
 
#使用拟重合指数法确定秘钥长度：拟重合指数大于0.6为标志
def length(Ciphertext):
    ListCiphertext=list(Ciphertext)
    Keylength=1
 
    while True:
        #指数初始化为０
        CoincidenceIndex = 0
 
        #使用切片分组
        for i in range(Keylength):
            Numerator = 0
            PresentCipherList = ListCiphertext[i::Keylength]
 
            #使用集合去重，计算每一子密文组的拟重合指数
            for Letter in set(PresentCipherList):
                Numerator += PresentCipherList.count(Letter) * (PresentCipherList.count(Letter)-1)
            CoincidenceIndex += Numerator/(len(PresentCipherList) * (len(PresentCipherList)-1))
 
        #求各子密文组的拟重合指数的平均值
        Average=CoincidenceIndex / Keylength
        Keylength += 1
 
        #均值＞0.6即可退出循环
        if Average > 0.06:
            break
 
    Keylength -= 1
    return Keylength
 
 
#使用重合指数法确定秘钥内容：遍历重合指数的最大值为标志
def keyword(Ciphertext,keylength):
    ListCiphertext = list(Ciphertext)
    Standard = {'A':0.08167,'B':0.01492,'C':0.02782,'D':0.04253,'E':0.12702,'F':0.02228,'G':0.02015,'H':0.06094,'I':0.06966,'J':0.00153,'K':0.00772,'L':0.04025,'M':0.02406,'N':0.06749,'O':0.07507,'P':0.01929,'Q':0.00095,'R':0.05987,'S':0.06327,'T':0.09056,'U':0.02758,'V':0.00978,'W':0.02360,'X':0.00150,'Y':0.01974,'Z':0.00074}
 
    while True:
        KeyResult = []
 
        for i in range(keylength):
            # 使用切片分组
            PresentCipherList = ListCiphertext[i::keylength]
 
            #初始化重合指数最大值为０，检验移动位数对应字符以＊代替
            QuCoincidenceMax = 0
            KeyLetter = "*"
 
            #遍历移动的位数
            for m in range(26):
                #初始化当前移动位数的重合指数为０
                QuCoincidencePresent = 0
 
                #遍历计算重合指数：各个字符的频率＊对应英文字符出现的标准频率－－－的和
                for Letter in set(PresentCipherList):
                    LetterFrequency = PresentCipherList.count(Letter) / len(PresentCipherList)
 
                    # 标准频率
                    k = chr( ( ord(Letter) - 65 - m ) % 26 + 65 )
                    StandardFrequency = Standard[k]
 
                    #计算重合指数
                    QuCoincidencePresent = QuCoincidencePresent + LetterFrequency * StandardFrequency
 
                #保存遍历过程中重合指数的最大值，同时保存对应应对的位数，即对应key的字符
                if QuCoincidencePresent > QuCoincidenceMax:
                    QuCoincidenceMax = QuCoincidencePresent
                    KeyLetter = chr( m + 65 )
 
            #保存当前位置key的值，退出循环，进行下一组子密文移动位数的尝试
            KeyResult.append( KeyLetter )
        #列表转为字符串
        Key = "".join(KeyResult)
        break
    return Key
 
 
if __name__ == '__main__':
 
    Ciphertext = input("输入密文：").upper()
 
    Keylength = length(Ciphertext)
 
    print("keylength最可能为：",Keylength)
 
    KeyResult = keyword(Ciphertext,Keylength)
 
    print("秘钥最可能为：" , KeyResult)
 
    #已知秘钥可用python自带维吉尼亚解密
    ClearText = vigenerecipher.decode( Ciphertext,KeyResult )
    print("解密结果为：" , ClearText)
 
 
 
 
 
 
