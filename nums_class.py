import time
import random
import os
from setting_class import Setting


class Nums(Setting):
  def __init__(self):
    self.nums = []
    self.u_bar = ''


  def Set(self, digit, count, speed):
    self.digit = digit
    self.count = count
    self.speed = (10 - speed) / 10


  def Create(self):
    self.nums = []

    for i in range(self.count):
      dig_base = 10 ** self.digit
      self.nums.append(random.randint(dig_base / 10, dig_base - 1))

    self.u_bar = ''

    for i in range(self.digit):
      self.u_bar += '_'


  def View(self):
    for i in range(6):
      os.system('clear')

      if i % 2 == 0:
        print(self.u_bar)

      time.sleep(0.5)

    for n in self.nums:
      os.system('clear')
      print(n)
      time.sleep(self.speed)
      os.system('clear')
      time.sleep(self.speed / 2)

    os.system('clear')
