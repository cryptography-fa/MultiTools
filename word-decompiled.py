# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys
print '\x1b[1;36mSilahkan Masukkan Username & Password Anda :V'
print '\x1b[1;36mGak Punya Username sama password nya? Hubungi Zen via WhatsApp 085325463021 '
username = 'ZenTampan'
password = 'Aditiaganteng'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('username : ')
    if uname == username:
        pwd = raw_input('password : ')
        if pwd == password:
            print '\x1b[1;36mLogin Berhasil Gan....',
            sys.exit()
        else:
            print '\x1b[1;31mMaaf Password Yang Anda masukan Salah gan... [?]\x1b[00m'
            print 'Silahkkan Login kembali gan.!!\n'
            restart()
    else:
        print '\x1b[1;31mMaaf Username Yang Anda masukan salah... [?]\x1b[00m'
        print 'Silahkan Login Kembali gan...!!\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()