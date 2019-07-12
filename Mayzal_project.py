from time import sleep
import os


menu = """
1.all_seeing
2.trap
3.troll

0.EXIT
"""
def main():
   print (menu)
   pilhan = input('masukan pilihan anda : ')
   if pilhan == '1' or pilihan ==  '01':
      print ('all_seeing')
      os.system('git clone https://github.com/zlucifer/all_seeing && cd all_seeing && bash cctv.sh')
   elif pilhan == '2' or pilihan == '02':
        print ('installing trap')
        os.system('git clone https://github.com/zlucifer/trap_project && cd trap_project && bash trap.sh')
   elif pilhan == '3' or pilihan == '03':
        print ('installing troll')
        os.system('git clone https://github.com/zlucifer/troll_project && cd troll_project && bash troll.sh')

   else:
      print('ERROR : WRONG INPUT.....!!!!')


main()
