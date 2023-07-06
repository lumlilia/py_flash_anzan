import os
import math
from nums_class import Nums
from setting_class import Setting


class Res():
  def __init__(self):
    self.setting = Setting()
    self.nums = Nums()
    self.char_arr = ([
      'y', 'Y', # Yes
      's', 'S', # Setting
      'q', 'Q'  # Quit
    ])


  def Title(self):
    os.system('clear')

    print(
      'フラッシュ暗算\n'
      + '桁数: ' + str(self.setting.digit) + ' / '
      + '回数: ' + str(self.setting.count) + ' / '
      + '速度: ' + str(self.setting.speed) + '\n\n'
      + '準備はいいか？野郎ども\n\n'
    )

    instr = input(
      'y: やってやろうじゃねぇか！\n'
      's: 設定\n'
      + 'q: やっぱ帰る\n'
    )

    if instr not in self.char_arr:
      return self.Title()

    char_i = math.floor(self.char_arr.index(instr) / 2)

    if char_i == 0:
      self.nums.Create(self.setting.digit, self.setting.count, self.setting.speed)
      self.nums.View()

      return self.Question()

    elif char_i == 1:
      self.setting.SettingTop()

      return self.Title()

    else:
      exit()


  def Question(self):
    anser = input('合計は？')

    try:
      int(anser)

    except ValueError:
      os.system('clear')
      print('数字を入力してください')

      return self.Question()

    os.system('clear')
    sum_num = sum(self.nums.nums)

    if int(anser) == sum_num:
      print('正解！\n')

    else:
      print('ハズレ…\n')

    print(
      str(sum_num) + ' ' + str(self.nums.nums).replace(',', ' +') + '\n\n'
      + 'あなたの答え: ' + anser + '\n'
    )
