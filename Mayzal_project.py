from time import sleep
import os


menu = """
1.locator
2.trap
3.troll

0.EXIT
"""
def main():
   print (menu)
   pilhan = input('masukan pilihan anda : ')
   if pilhan == '1' or pilhan ==  '01':
      print ('all_seeing')
      os.system('git clone https://github.com/thelinuxchoice/locator && cd locator && bash locator. sh')
   elif pilhan == '2' or pilhan == '02':
        print ('installing trap')
        os.system('git clone https://github.com/zlucifer/trap_project && cd trap_project && bash trap.sh')
   elif pilhan == '3' or pilhan == '03':
        print ('installing troll')
        os.system('git clone https://github.com/zlucifer/troll_project && cd troll_project && bash troll.sh')

   else:
      print('ERROR : WRONG INPUT.....!!!!')


main()
