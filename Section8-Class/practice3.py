# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # __init__: 생성자
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print(f'{self.name}: {location} 방향으로 이동합니다. [속도 {self.speed}]')

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # __init__: 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name}: {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]')

    def damaged(self, damage):
        print(f'{self.name}: {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name}: 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f'{self.name}: 파괴되었습니다.')
            
# # 파이어뱃: 공격 유닛, 화염방사기.
# firebat1 = AttackUnit('파이어뱃', 50, 16)
# firebat1.attack('5시')

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽: 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f'{name}: {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]')

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super는 self없이 사용
        self.location = location
    
# 서플라이 디폿: 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
# valkyrie.fly(valkyrie.name, '3시')

# 벌쳐: 지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌쳐', 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
# battlecruiser.fly(battlecruiser.name, '9시')
battlecruiser.move('9시')
valkyrie.move('9시')