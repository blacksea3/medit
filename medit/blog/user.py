from blog.models import *

## 验证用户
## 输入用户名、密码
## 输出类型+代号 F错误 T成功  F0账号不存在 F1账号密码不对应
def login_verify(username,password):
	user = User.objects.filter(username = username)
	if not user:
		return 'F0'
	else:
		if password != user[0].password:
			return 'F1'
		else:
			return 'T'

## 自动检查用户
## 输入session
## 输出 True 已登陆 False 未登录			
def login_auto_check(session):
	if 'username' in session:
		if 'password' in session:
			user = User.objects.filter(username = session['username'])
			if not user:
				return False
			else:
				if session['password'] != user[0].password:
					return False
				else:
					return True
		else:
			return False
	else:
		return False
