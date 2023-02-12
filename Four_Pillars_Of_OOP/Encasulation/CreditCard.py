class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        '''이름, 비밀번호 , 카드 한도'''
        self.name = name
        self.password = password
        self.payment_limit = payment_limit
    
    @property
    def password(self):
        '''password getter method'''
        return "비밀 번호는 볼 수 없습니다"
    
    @password.setter
    def password(self, passwd):
        '''password setter method'''
        self._password = passwd
    
    @property
    def payment_limit(self):
        '''payment_limit getter method'''
        return self._payment_limit
    
    @payment_limit.setter
    def payment_limit(self, limit):
        '''payment_limit setter method'''
        if limit<0 or limit>self.MAX_PAYMENT_LIMIT:
             print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
        else: 
            self._payment_limit = limit

card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)