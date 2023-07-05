import time
import random
import os


class Nums:
  def __init__(self):
    self.nums = []


  def Create(self):
    self.nums = []

    for i in range(5):
      self.nums.append(random.randint(1, 9))


  def View(self):
    for n in self.nums:
      os.system('clear')
      print(n)
      time.sleep(0.5)
      os.system('clear')
      time.sleep(0.1)

    os.system('clear')


  def Question(self):
    self.anser = input('合計は？')

    try:
      int(self.anser)
    except ValueError:
      os.system('clear')
      print('数字を入力してください')

      return self.Question()

    return self.anser
