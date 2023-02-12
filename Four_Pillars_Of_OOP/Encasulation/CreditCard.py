class CreditCard:
    '''신용 카드를 나타내는 클래스'''
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        '''사용자 이름, 비밀번호 , 카드 한도 정보'''
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_password(self):
        print("비밀번호는 볼 수 없습니다.")
    
    def set_password(self, password):
        self.__password = password
    
    def get_payment_limit(self):
        return self.__payment_limit
    
    def set_payment_limit(self, payment_limit):
        if payment_limit<0 or payment_limit>self.MAX_PAYMENT_LIMIT:
            print("카드 한도는 0원~3천만원 사이로 설정해 주세요!")
        else :self.__payment_limit = payment_limit


card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())