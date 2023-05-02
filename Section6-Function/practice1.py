# 함수 정의
# 호출하기 전까지는 기능하지 않음
def open_account():
    print('새로운 계좌가 생성되었습니다.')

def deposit(balance, money): # 입금
    print(f'입금이 완료되었습니다. 잔액은 {balance + money} 원입니다.')
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print(f'출금이 완료되었습니다. 잔액은 {balance - money} 원입니다')
        return balance - money 
    else:
        print(f'출금이 완료되지 않았습니다. 잔액은 {balance} 원입니다.')
        return balance
    
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commisiion, balance = withdraw_night(balance, 500)
print(f'수수료 {commisiion} 원이며, 잔액은 {balance} 원입니다.')