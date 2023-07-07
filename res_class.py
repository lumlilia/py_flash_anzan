import os
import math
import const
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
    os.system(const.CLEAR_CMD)

    print(
      'フラッシュ暗算\n'
      + '桁数: ' + str(self.setting.data['digit']) + ' / '
      + '回数: ' + str(self.setting.data['count']) + ' / '
      + '速度: ' + str(self.setting.data['speed'])
      + (' / S乱' if self.setting.data['s-random'] else '')
      + '\n\n'
      + '準備はいいか？野郎ども\n\n'
    )

    return self.InputCheck(
      input(
        'y: やってやろうじゃねぇか！\n'
        's: 設定\n'
        + 'q: やっぱ帰る\n'
      ), 0
    )


  def InputCheck(self, instr, mode):
    if instr not in self.char_arr:
      if mode == 0:
        return self.Title()

      elif mode == 1:
        os.system(const.CLEAR_CMD)
        return self.Continue()

      else:
        return print('Error!!\n\nmodeの値が不正です' )

    char_i = math.floor(self.char_arr.index(instr) / 2)

    if char_i == 0:
      return self.Start(True if mode == 0 else False)

    elif char_i == 1:
      self.setting.SettingTop()

      return self.Title()

    else:
      exit()


  def Start(self, flag):
    if flag:
      self.nums.Set(self.setting.data)

    self.nums.Create()
    self.nums.View()

    return self.Question()


  def Question(self):
    anser = input('合計は？\n')

    try:
      int(anser)

    except ValueError:
      os.system(const.CLEAR_CMD)
      print('数字を入力してください')

      return self.Question()

    os.system(const.CLEAR_CMD)
    sum_num = sum(self.nums.nums)

    if int(anser) == sum_num:
      print('正解！\n')

    else:
      print('ハズレ…\n')

    print(
      str(sum_num) + ' ' + str(self.nums.nums).replace(',', ' +') + '\n\n'
      + 'あなたの答え: ' + anser + '\n\n'
    )

    return self.Continue()


  def Continue(self):
    print('続ける？\n')

    return self.InputCheck(
      input(
        'y: このまま続ける\n'
        + 's: 設定を変える\n'
        + 'q: さようなら\n'
      ), 1
    )
