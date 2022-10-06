password = 'a123456' 
i = 3 #剩下機會
while i > 0: 
	i = i - 1
	pwd = input ('請輸入密碼: ')
	if pwd == password:
		print('登入成功!!')
		break #跳出迴圈
	else: 
		print('登入錯誤')
		if i > 0:
			print('登入錯誤,還有', i,'次機會')
		else: 
			print('鎖帳號')