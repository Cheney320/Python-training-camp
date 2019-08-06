"""
编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
    要求：
        登录成功一次，后续的函数都无需再输入用户名和密码
    注意：
        从文件中读出字符串形式的字典，可以用
        eval('{"name":"albert","password":"123"}')转成字典格式

"""

db = 'db.txt'
login_status = {'user':None,'status':False}
def auth(auth_type='file'):
    def auth2(func):
        def wrapper(*args, **kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args, **kwargs)
            if auth_type == 'file':
                with open(db, encoding='utf-8') as f:
                    dic = eval(f.read())
                name = input('username: ').strip()
                password = input('password: ').strip()
                if name in dic['name'] and password == dic['password']:
                    login_status['user'] = name
                    login_status['status'] = True
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('username or password error')
            elif auth_type == 'sql':
                pass
            else:
                pass
        return wrapper
    return auth2

@auth()
def index():
    print('index')

@auth(auth_type='file')
def home(name):
    print('welcome %s to home' %name)

# index()
home("albert")