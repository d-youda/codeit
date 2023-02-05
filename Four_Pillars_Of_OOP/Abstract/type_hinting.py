#파이썬 : 동적 타입 언어이기 때문에, 변수 앞에 타입 알려주지 않음
'''사용자가 변수 타입을 헷갈리지 않게 하기 위해 타입을 알려주는 것 : type hinting'''
class BankAccount:
    '''은행 계좌 클래스'''
    interest:float = 0.02

    def __init__(self, owner_name:str , balance:float)->None:
        '''인스턴스 변수 : name(문자열) , balance(실수형)'''
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount:float)->None:
        '''잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드'''
        self.balance += amount
    
    def withdraw(self, amount:float)->None:
        '''잔액 인스턴스 변수 bakance를 파라미터 amount만큼 줄여주는 메소드'''
        if self.balance < amount:
            print("Insufficient balance!")
        else: self.balance -= amount
    
    def add_interest(self)->None:
        '''잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드'''
        self.balance *= 1+BankAccount.interest

'''type hinting한대로 값을 넣지 않아도 실행은 가능함
    대신, 팝업 경고메세지는 출력해줄 수 있음
    실행에 직접 영향을 주진 않지만, 다른 개발자들이 어느 타입을 써야 하는지 빠르게 알 수 있도록 한다는 장점이 있음
    
    그러나, 3.0이하 버전에는 type-casting이 실행되지 않음'''
