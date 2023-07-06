import os
import math
import re


class Setting():
  def __init__(self):
    self.digit = 1
    self.count = 5
    self.speed = 4

    self.char_arr = ([
      'd', 'D',  # Digit
      'c', 'C',  # Count
      's', 'S',  # Speed
      'q', 'Q'   # quit
    ])

    self.set_texts = ([
      '桁数を設定してね ', '[1-5]',
      '回数を設定してね ', '[2-9]',
      '速度を設定してね ', '[1-9]',
    ])


  def SettingTop(self):
    os.system('clear')

    print('設定めにゅ〜\n')
    
    instr = input(
      'd: 桁数\n'
      + 'c: 回数\n'
      + 's: 速度\n'
      + 'q: 設定完了\n'
    )

    if instr not in self.char_arr:
      return self.SettingTop()

    else:
      char_i = math.floor(self.char_arr.index(instr) / 2)

      if char_i < 3:
        return self.Set(char_i)


  def Set(self, mode):
    os.system('clear')
    mode_i = mode * 2
    num_range = self.set_texts[mode_i + 1]

    instr = input(
      self.set_texts[mode_i]
      + num_range + '\n'
    )

    if re.fullmatch(num_range, instr) == None:
      input(
        '\nError!!\n'
        + num_range[1:2] + '〜' + num_range[3:4]
        + 'の範囲で入力してください (press keys)'
      )

      return self.Set(mode)

    else:
      n = int(instr)

      if mode == 0:
        self.digit = n

      elif mode == 1:
        self.count = n

      elif mode == 2:
        self.speed = n
      
      input(
        self.set_texts[mode_i][0:2] + ' を '
        + instr + ' に設定しました (press keys)'
      )

    return self.SettingTop()
