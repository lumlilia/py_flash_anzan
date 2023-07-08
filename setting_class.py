import os
import math
import re
import json
import const


class Setting():
  def __init__(self):
    self.char_arr = ([
      'd', 'D',  # Digit
      'c', 'C',  # Count
      's', 'S',  # Speed
      'r', 'R',  # super Random mode
      'q', 'Q'   # Quit
    ])

    self.set_texts = ([
      '桁数を設定してね ', '[1-9]',
      '回数を設定してね ', '[2-9]',
      '速度を設定してね ', '[1-9]',
    ])

    if os.path.isfile(const.CONFIG_FILE):
      with open(const.CONFIG_FILE, encoding='utf-8') as f:
        try:
          self.data = json.loads(f.read())

        except:
          self.DataInit(True)

        else:
          d_name = ['digit', 'count', 'speed', 's-random']

          if d_name == list(self.data.keys()):
            for i in range(3):
              if not re.fullmatch(self.set_texts[i * 2 + 1], str(self.data[d_name[i]])):
                self.DataInit(True)
                break
          else:
            self.DataInit(True)

    else:
      self.DataInit(False)


  def SettingTop(self):
    os.system(const.CLEAR_CMD)

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

      elif char_i == 3:
        self.data['s-random'] = not self.data['s-random']

        os.system(const.CLEAR_CMD)
        input(
          'SuperRandomMode: '
          + ('ON' if self.data['s-random'] else 'OFF')
          + '\n(press keys)\n'
        )

        return self.SettingTop()

      else:
        with open(const.CONFIG_FILE, mode='w', encoding='utf-8') as f:
          f.write(json.dumps(self.data, indent=2))


  def Set(self, mode):
    os.system(const.CLEAR_CMD)
    mode_i = mode * 2
    num_range = self.set_texts[mode_i + 1]

    instr = input(
      self.set_texts[mode_i]
      + num_range + '\n'
    )

    if not re.fullmatch(num_range, instr):
      input(
        '\nError!!\n'
        + num_range[1:2] + '〜' + num_range[3:4]
        + 'の範囲で入力してください (press keys)'
      )

      return self.Set(mode)

    else:
      n = int(instr)

      if mode == 0:
        self.data['digit'] = n

      elif mode == 1:
        self.data['count'] = n

      elif mode == 2:
        self.data['speed'] = n
      
      input(
        self.set_texts[mode_i][0:2] + ' を '
        + instr + ' に設定しました (press keys)'
      )

    return self.SettingTop()


  def DataInit(self, flag):
    self.data = ({
      'digit': 1,
      'count': 5,
      'speed': 4,
      's-random': False
    })

    with open(const.CONFIG_FILE, mode='w', encoding='utf-8') as f:
      f.write(json.dumps(self.data, indent=2))

    if flag:
      input('Error!!\n\nconfig.jsonが不正です。\n設定を初期化しました。\n')
