'''
추상화 : 내부 내용을 잘 모르고도 잘 사용할 수 있도록 하는 것
'''
#추상화를 잘 하려면 이름을 잘 지어야 함
'''
이름을 잘 짓지 않으면 어디에 쓰는 클래스인지 이해하기가 어렵다
'''
class someClass:
    class_variable = 0.02

    def __init__(self, variable_1 , variable_2):
        self.variable_1 = variable_1
        self.variable_2 = variable_2
    
    def method_1(self,some_value):
        self.variable_2 += some_value
    
    def method_2(self,somevalue):
        if self.variable_2 < somevalue:
            print("Insufficient balance!")
        else: self.variable_2 -= somevalue
    
    def method_2(self):
        self.variable_2 += 1+someClass.class_variable

'''좋은 예시'''
class BankAccount:
    interest = 0.02

    def __init__(self, owner_name , balance):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!")
        else: self.balance -= amount
    
    def add_interest(self):
        self.balance *= 1+BankAccount.interest
'''어디에 쓰는 클래스이고, 어떻게 사용해야 할 지 직관적으로 알 수 있음'''

example_account = BankAccount("Hong Gil dong" , 1000)
example_account.add_interest()
print(example_account.balance)

example_account.deposit(500)
print(example_account.balance)

example_account.withdraw(2000)
print(example_account.balance)

#추상화 잘하는 방법 2: 문서화하기
'''
파이썬 : docString 사용
docstring : 문서화 문자열
클래스나 문자열의 정보 저장 가능
'''
class BankAccount:
    '''은행 계좌 클래스'''
    interest = 0.02

    def __init__(self, owner_name , balance):
        '''인스턴스 변수 : name(문자열) , balance(실수형)'''
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        '''잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드'''
        self.balance += amount
    
    def withdraw(self, amount):
        '''잔액 인스턴스 변수 bakance를 파라미터 amount만큼 줄여주는 메소드'''
        if self.balance < amount:
            print("Insufficient balance!")
        else: self.balance -= amount
    
    def add_interest(self):
        '''잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드'''
        self.balance *= 1+BankAccount.interest

help(BankAccount)
'''docstring만 보여줌'''