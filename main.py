import os
import time
import random
import nums_class as Nums


def main():
  os.system('clear')
  nums = Nums.Nums()

  print('フラッシュ暗算\n準備はいいか？野郎ども\n')
  instr = input('やってやろうじゃねぇか！(y):')

  if instr == 'y' or instr == 'Y':
    nums.Create()
    nums.View()
    anser = nums.Question()

    if int(anser) == sum(nums.nums):
      print('正解！')

    else:
      print('ハズレ…\n\n正解は'\
      + str(sum(nums.nums))\
      )

main()
