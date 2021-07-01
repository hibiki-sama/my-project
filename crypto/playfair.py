letter_list='ABCDEFGHIKLMNOPQRSTUVWXYZ'#字母表
T_letter=['','','','','']#密码表

#根据密钥建立按行密码表
def Create_Matrix(key):
  key=Remove_Duplicates(key)  #移除密钥中的重复字母
  #key=key.replace(' ','') #去除密钥中的空格
  
  for ch in letter_list:  #根据密钥获取新组合的字母表
    if ch not in key:
      key+=ch
  
  j=0
  for i in range(len(key)): #将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
    T_letter[j]+=key[i]     #j用来定位字母表的行
    if 0==(i+1)%5:
      j+=1
  print(T_letter)
def Remove_Duplicates(key):
  key=key.upper() #转成大写字母组成的字符串
  _key=''
  for ch in key:
    if ch=='J':
      ch='I'
    if ch in _key:
      continue
    else:
      _key+=ch
  return _key
def Get_MatrixIndex(ch):#找字符坐标
  for i in range(len(T_letter)):
    for j in range(len(T_letter)):
      if ch==T_letter[i][j]:
        return i,j #i为行，j为列
def de(cipher,T_letter):
	plaintext=''
	for i in range(0,len(cipher),2):
		j=i+1
		a=Get_MatrixIndex(cipher[i].upper())
		b=Get_MatrixIndex(cipher[j].upper())#找坐标
		if(cipher[i].upper()==cipher[j].upper()):#若组内字母相同
			plaintext+=T_letter[(a[0]-1)%5][(a[1]-1)%5]+T_letter[(a[0]-1)%5][(a[1]-1)%5]
			continue;
		if(a[0]==b[0]):#如果在同一行
			plaintext+=T_letter[a[0]][(a[1]-1)%5]+T_letter[b[0]][(b[1]-1)%5]
		elif(a[1]==b[1]):#如果在同一列
			plaintext+=T_letter[(a[0]+1)%5][a[1]]+T_letter[(b[0]+1)%5][b[1]]
		else:#不同行同列
			plaintext+=T_letter[a[0]][b[1]]+T_letter[b[0]][a[1]]
	return plaintext
cipher='QneomKgkiseunhennhugupuudxrfnzHeuzeuniludrizdrznefoixdhnisdxthdXuzcavkefrfmuetlhhedleumkafgpfrmgOnzNefupuudxrmntrnetheeoieppqnluhtgehnUmlnbplnaikaiaheffxnmgentznaqnmtnrTaglbnnamptkufimfdioridekiefkolngEeftxdxnmtosdulsmtosuionhkodlhdmkanpFwfethfalsethpsnrkctaboafgkpsrnsaepkolnfCpahexnhnseeoupuudxqneomeiagnldAmxrmutrmurnzzkiambnetnbtopeakzuyqhAluqneorlnthedpgoheuzzhefxdpnmttkzzetldHcnamtnhdxatssmtnraibplnheuzdukzpnUmmiafnulnhftadpnthealxdxnqftarnnRimmadoptnrhemptabetkufptnrmkdnaiheff'
key='cute'#密钥
Create_Matrix(key)
plaintext=de(cipher,T_letter)
plaintext=plaintext.lower()
print('明文为:\n',plaintext)
