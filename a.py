def run(num):

   if num<10:
       num+=11
       print("more 10")
   if num>10:
       open(num)
       print("less 10")

def open(num):
    if num>10:
        num-=11
        print("open more 10")
    if num<10:
        run(num)
        print("open less 10")

run(0)