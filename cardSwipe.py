import os,sys,time
f = open('numb/number_of_entries{}'.format(time.strftime('%d%m%y')),'w')
input_ = ''
f.write('{}\n'.format(time.strftime("%d/%m/%y")))

while(not input_ == 'Stop Demon'):
    try:
        os.system('clear')
        os.system('figlet Swipe your UD ID or Type your ID Number!')
        input_ = str(raw_input())
        if(len(input_) < 19):
            f.write('{} {}\n'.format(str(input_),time.strftime("%H:%M:%S")))
            os.system('clear')
            os.system('figlet Thank You!')
            time.sleep(2)
        else:
            f.write('{} {}\n'.format(str(input_)[10:19],time.strftime("%H:%M:%S")))
            os.system('clear')
            os.system('figlet Thank you')
            time.sleep(2)
    except:
        print 'Please try again!'
os.system('./commandForEmail "numb/number_of_entries{}"'.format(time.strftime("%d%m%y")))
