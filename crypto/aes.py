def Sbox_51(fir_num_51, last_num_51):
	#S盒替换
	sbox=[[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76], 
	[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
	[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
	[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
	[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
	[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
	[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
	[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
	[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
	[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
	[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
	[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
	[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
	[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
	[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
	[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
	return (sbox[fir_num_51][last_num_51])

def line_shift_51(dir_clear_number):
	#进行行移位操作
	for i in range(4):
		my_list = []
		list = dir_clear_number[i]
		for j in range(4):
			my_list.append(list[(j + i) % 4])
		dir_clear_number[i] = my_list
	return dir_clear_number

def get_matrix_of_clear_number(clear_number):
	#得到输入数据对应的矩阵
	dir = {0:[], 1:[], 2:[], 3:[]}
	length = len(clear_number)
	for i in range(length):
		dir[i % 4].append(clear_number[i])
	return dir

def print_(dir_num):
	#测试输出字典
	for key, num in dir_num.items():
		print(num)
		
def dex_to_int(string):
	#得到数据二进制到十进制的转换
	my_result = 0
	for k in range(8):		
		if string[k] == '1':
			my_result += 2 ** (7 - k)
	return my_result

def get_2(last_num):
	#得到列混合中乘以2的结果	
	last_num_copy = last_num
	last_num_copy = bin(last_num_copy)[2:].rjust(8, '0')
	judge_num = bin(last_num)[2:]	
	judge_num = last_num_copy[0]
	last_num_copy = last_num_copy[1:]
	last_num_copy += '0'
	
	if judge_num == '1':
		string_judge = '00011011'	
		last_num_copy = bin(XOR(string_judge, last_num_copy))[2:].rjust(8, '0')	
	return last_num_copy

def define_column_rotation(dir_clear_number_copy):
	#在列混合中先将列进行旋转
	dir_clear_number = {0:[], 1:[], 2:[], 3:[]}
	for key, num in dir_clear_number_copy.items():
		list = num	
		for i  in range(4):
			dir_clear_number[i].append(int(list[i],16))
	return dir_clear_number

def define_column_hybrid(dir_clear_number_copy):
	#进行列混合操作，得到对应的十六进制的矩阵		
	dir_matrix = {
		0:[2, 3, 1, 1],
		1:[1, 2, 3, 1],
		2:[1, 1, 2, 3],
		3:[3, 1, 1, 2]
	}
	dir_clear_number = define_column_rotation(dir_clear_number_copy)	
	dir_new_clear_number = {0:[], 1:[], 2:[], 3:[]}
	
	for i in range(4):	
		list_matrix = dir_matrix[i]
		list = []
		for j in range(4):		
			list_num = dir_clear_number[j]
			string = ''		
			my_string  = '00000000'
 
			for k in range(4):
				if list_matrix[k] == 2:
					string = get_2(list_num[k])
				if list_matrix[k] == 3:
					string = get_2(list_num[k])
					list_num_copy = bin(list_num[k])[2:].rjust(8, '0')
					string = bin(XOR(string, list_num_copy))[2:].rjust(8, '0')
				if list_matrix[k] == 1:
					string = bin(list_num[k])[2:].rjust(8, '0')	
				my_string = bin(XOR(my_string, string))[2:].rjust(8, '0')
			my_result = dex_to_int(my_string)
			list.append(hex(my_result)[2:])
			dir_new_clear_number[i] = list
	return dir_new_clear_number

def hex_to_int_number(hex_num, flag):
	#十六进制矩阵转换为十进制矩阵
	number = int(hex_num, 16)
	int_num = number // 16
	int_re = number % 16
	if flag == 1:
		my_number = Sbox_51(int_num, int_re)
	else:
		my_number = define_inverse_S_box(int_num, int_re)
	return my_number

def define_byte_subdtitution(dir_new_number, flag):
	#定义字节代换
	dir_1 = {0:[], 1:[], 2:[], 3:[]}
	for j in range(4):
		list_new = []
		list = dir_new_number[j]
		for k in range(4):		
			new_num = hex_to_int_number(list[k], flag)
			list_new.append(hex(new_num)[2:])
		dir_1[j] = list_new
	return dir_1

def XOR(string_1, string_2):
	#得到异或后的十进制结果	
	decimal_result = 0
	for i in range(8):
		if string_1[i] != string_2[i]:
			decimal_result += 2 ** (7 - i)
	
	return decimal_result

def get_round_key_plus(clear_number, dir_key_extend):
	#进行轮密钥加的操作
	dir_new_number = {0:[], 1:[], 2:[], 3:[]}
	for i in range(4):
		list_number = clear_number[i]
		list_key = dir_key_extend[i]
		list = []
		for j in range(4):
			number = int(list_number[j], 16)
			key = int(list_key[j], 16)
			string_num = bin(number)[2:].rjust(8, '0')
			string_key = bin(key)[2:].rjust(8, '0')
			result_int = XOR(string_num, string_key)
			list.append(hex(result_int)[2:])
		dir_new_number[i] = list
	return dir_new_number

if __name__ == "__main__":
	print("明文: ")
	clear_number = input()
	clear_number=clear_number.split( )
	dir_clear_number = get_matrix_of_clear_number(clear_number)
	print("输入明文状态矩阵: ")
	print_(dir_clear_number)
	
	print("密钥: ")
	secret_key = input()
	secret_key=secret_key.split( )
	dir_secret_key = get_matrix_of_clear_number(secret_key)
	print("输入密钥状态矩阵: ")
	print_(dir_secret_key)
	
	#对明文进行轮密钥加
	dir_new_number = get_round_key_plus(dir_clear_number, dir_secret_key)
	print('轮密钥加:')
	print_(dir_new_number)
	
	dir_1 = define_byte_subdtitution(dir_new_number, 1)#字节代换
	print('字节代换:')
	print_(dir_1)
	
	dir_1 = line_shift_51(dir_1)#行移位
	print('行移位:')
	print_(dir_1)
	
	
	dir_1 = define_column_hybrid(dir_1)#列混合
	print('列混合:')
	print_(dir_1)
 
