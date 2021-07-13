import random
r = random.randint(1, 100)
while True:
	a = input('請輸入您猜的數字：')
	a = int(a)
	if r == a:
		print('恭喜！您猜對了！')
		break
	elif r > a:
		print('猜錯了！您猜的比答案小！')
	elif r < a:
		print('猜錯了！您猜的比答案大！')