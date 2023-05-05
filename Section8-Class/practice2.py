class Unit:
    def __init__(self, name, hp, damage): # __init__: 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{name} 유닛이 생성되었습니다.')
        print(f'체력 {hp}, 공격력 {damage}')

# 클래스로부터 만들어지는 객체 / Unit클래스의 인스턴스
marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)

# 레이스: 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit('레이스', 80, 5)
print(f'유닛 이름: {wraith1.name}, 공격력: {wraith1.damage}')

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True # 객체의 변수를 외부에서 할당 가능

if wraith2.clocking == True:
    print(f'{wraith2.name} 는 현재 클로킹 상태입니다.')