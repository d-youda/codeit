'''캡술화
1. 객체 일부 구현 내용에 대해 외부로부터의 직접적 액세스 차단
-> 클래스 외부에서 내부로 직접적인 접근을 하지 못하게 함
-> 변수 앞에 __(언더바 두개) 붙이면 접근하지 못하게 함
2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것'''
class Citizen:
    '''주민 클래스'''
    drink_age = 19 #음주 가능 나이

    def __init__(self, name, age , resident_id):
        '''이름, 나이 ,주민등록번호'''
        self.name = name
        self.__age = age
        self.__residnet_id = resident_id
    
    def authenticate(self, id_field):
        '''본인이 맞는지 확인하는 메소드'''
        return self.__residnet_id == id_field
    
    def can_drink(self):
        '''음주 가능 나이인지 확인하는 메소드'''
        return self.__age >= Citizen.drink_age
    
    def __str__(self):
        '''주민 정보를 문자열로 반환하는 메소드'''
        return self.name + "씨는 "+str(self.__age)+"살입니다!"

kyusik = Citizen("최규식" , 25 , "12345678")
young = Citizen("Younghoo kang" , 5 , "87654321") #어린이

print(kyusik.residnet_id) #주민등록번호 유출 가능

kyusik.age = -12
print(kyusik)