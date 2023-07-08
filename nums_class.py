import time
import random
import os
import const


class Nums():
  def __init__(self):
    self.nums = []
    self.u_bar = ''


  def Set(self, data_arr):
    self.digit = data_arr['digit']
    self.count = data_arr['count']
    self.speed = (10 - data_arr['speed']) / 10
    self.sr = data_arr['s-random']


  def Create(self):
    self.nums = []

    for i in range(self.count):
      if self.sr:
        dig_base = 10 ** random.randint(1, self.digit)

      else:
        dig_base = 10 ** self.digit

      rand_min = dig_base / 10
      self.nums.append(random.randint(rand_min, dig_base - 1))

    self.u_bar = ''

    for i in range(self.digit):
      self.u_bar += '_'


  def View(self):
    for i in range(6):
      os.system(const.CLEAR_CMD)

      if i % 2 == 0:
        print(self.u_bar)

      time.sleep(0.5)

    for n in self.nums:
      os.system(const.CLEAR_CMD)
      print(str(n).rjust(self.digit))
      time.sleep(self.speed)
      os.system(const.CLEAR_CMD)
      time.sleep(self.speed / 2)

    os.system(const.CLEAR_CMD)
