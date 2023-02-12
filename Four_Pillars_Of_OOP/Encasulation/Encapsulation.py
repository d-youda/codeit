class Citizen:
    '''주민 클래스'''
    drink_age = 19 #음주 가능 나이

    def __init__(self, name, age , resident_id):
        '''이름, 나이 ,주민등록번호'''
        self.name = name
        self.age = age
        self.residnet_id = resident_id
    
    def authenticate(self, id_field):
        '''본인이 맞는지 확인하는 메소드'''
        return self.residnet_id == id_field
    
    def can_drink(self):
        '''음주 가능 나이인지 확인하는 메소드'''
        return self.age >= Citizen.drink_age
    
    def __str__(self):
        '''주민 정보를 문자열로 반환하는 메소드'''
        return self.name + "씨는 "+str(self.age)+"살입니다!"

    @property
    def age(self):
        print("나이를 반환합니다.")
        return self._age

    @age.setter
    def age(self,value):
        print("나이를 설정합니다")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else: self._age = value

young = Citizen("Younghoo kang" , -18 , "12345678")

print(young.get_age())

young.set_age(25)
print(young.get_age())