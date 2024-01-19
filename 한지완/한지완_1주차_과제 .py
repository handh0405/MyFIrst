import random

class Dicegame:
    def __init__(self):
        self.N = int(input())

        while (self.N <= 10 or self.N >= 50):
            print("조건에 맞지 않습니다. 다시 입력하세요.")
            self.N = int(input())
        
        self.dice_num = [0, 0, 0, 0, 0, 0]



    # random 라이브러리를 활용해서 주사위를 N번 굴려 결과값(각각의 수가 몇번 나왔는지)을 저장하는 함수
    def roll_dice(self):
        for i in range(self.N):
            self.dice_num[random.randrange(0,6)] +=1


    # 1. 저장된 결과값들 2. 두번째로 많이 나온 주사위 수 를 print하는 함수
    def print_result(self):
        for i in range(6):
            print("Dice number", i+1, ":", self.dice_num[i])   
        findnum = self.dice_num.copy()    
        for i in range(6):
            if max(self.dice_num) == max(findnum):
                findnum.remove(max(self.dice_num))
            else:
                break
        ans = []
        for i in range(6):
            if max(findnum) == self.dice_num[i]:
                ans.append(i+1)
        for i in range(len(ans)):
            print("Second Largest Number :", ans[i])



if __name__ == "__main__":
    dice_game = Dicegame()
    dice_game.roll_dice()
    dice_game.print_result()
