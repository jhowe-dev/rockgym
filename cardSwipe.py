import os,sys,time
f = open('number_of_entries{}'.format(time.strftime('%d%m%y')),'w')
input_ = ''
f.write('{}\n'.format(time.strftime("%d/%m/%y")))

while(not input_ == 'Stop Demon'):
    try:
        os.system('figlet Swipe your UD ID or Type your ID Number!')
        input_ = str(raw_input())
        f.write('{} {}\n'.format(str(input_)[10:19],time.strftime("%H:%M:%S")))
        print 'Thank You!'
    except:
        print 'Please try again!'
