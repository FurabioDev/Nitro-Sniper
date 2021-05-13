import re
import os
import discord
import platform
import datetime
import requests

from colorama import Fore, init

os.system("title Discord Sniper by 410'Sx10 $$")

class Sniper(discord.Client):
    """Our discord.py client"""

    def __init__(self, **options):
        super().__init__(**options)
        self.token = "TOKEN HERE"

    def client_headers(self):
        """Simply the headers needed to perform the requests"""
        return {
            'Authorization': self.token,
            'Content-Type': 'application/json',
        }

    @staticmethod
    def clear_console():
        if platform.system() != 'Linux':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def replace_multiple(text):
        to_be_replaced = ['b', 'd', 'Y', '.', '`', "'", '~', 'V', 'o', 'D', 'P']
        for elem in to_be_replaced:
            if elem in text:
                text = text.replace(elem, f'{Fore.MAGENTA}{elem}{Fore.RESET}')
        return text

    def start_menu(self):
        banner = self.replace_multiple("""                                                                                                                                                            
       444444444    1111111        000000000             SSSSSSSSSSSSSSS                   iiii                                                             
      4::::::::4   1::::::1      00:::::::::00         SS:::::::::::::::S                 i::::i                                                            
     4:::::::::4  1:::::::1    00:::::::::::::00      S:::::SSSSSS::::::S                  iiii                                                             
    4::::44::::4  111:::::1   0:::::::000:::::::0     S:::::S     SSSSSSS                                                                                   
   4::::4 4::::4     1::::1   0::::::0   0::::::0     S:::::S          nnnn  nnnnnnnn    iiiiiiippppp   ppppppppp       eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  4::::4  4::::4     1::::1   0:::::0     0:::::0     S:::::S          n:::nn::::::::nn  i:::::ip::::ppp:::::::::p    ee::::::::::::ee  r::::rrr:::::::::r  
 4::::4   4::::4     1::::1   0:::::0     0:::::0      S::::SSSS       n::::::::::::::nn  i::::ip:::::::::::::::::p  e::::::eeeee:::::eer:::::::::::::::::r 
4::::444444::::444   1::::l   0:::::0 000 0:::::0       SS::::::SSSSS  nn:::::::::::::::n i::::ipp::::::ppppp::::::pe::::::e     e:::::err::::::rrrrr::::::r
4::::::::::::::::4   1::::l   0:::::0 000 0:::::0         SSS::::::::SS  n:::::nnnn:::::n i::::i p:::::p     p:::::pe:::::::eeeee::::::e r:::::r     r:::::r
4444444444:::::444   1::::l   0:::::0     0:::::0            SSSSSS::::S n::::n    n::::n i::::i p:::::p     p:::::pe:::::::::::::::::e  r:::::r     rrrrrrr
          4::::4     1::::l   0:::::0     0:::::0                 S:::::Sn::::n    n::::n i::::i p:::::p     p:::::pe::::::eeeeeeeeeee   r:::::r            
          4::::4     1::::l   0::::::0   0::::::0                 S:::::Sn::::n    n::::n i::::i p:::::p    p::::::pe:::::::e            r:::::r            
          4::::4  111::::::1110:::::::000:::::::0     SSSSSSS     S:::::Sn::::n    n::::ni::::::ip:::::ppppp:::::::pe::::::::e           r:::::r            
        44::::::441::::::::::1 00:::::::::::::00      S::::::SSSSSS:::::Sn::::n    n::::ni::::::ip::::::::::::::::p  e::::::::eeeeeeee   r:::::r            
        4::::::::41::::::::::1   00:::::::::00        S:::::::::::::::SS n::::n    n::::ni::::::ip::::::::::::::pp    ee:::::::::::::e   r:::::r            
        4444444444111111111111     000000000           SSSSSSSSSSSSSSS   nnnnnn    nnnnnniiiiiiiip::::::pppppppp        eeeeeeeeeeeeee   rrrrrrr            
                                                                                                 p:::::p                                                    
                                                                                                 p:::::p                                                    
                                                                                                p:::::::p                                                   
                                                                                                p:::::::p                                                   
                                                                                                p:::::::p                                                   
                                                                                                ppppppppp                                                   
                                                                                                                ( ´-ω･)︻┻┳══━一""")
        print(banner + f"\n\n\t{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S %p')}{Fore.RESET} [1] Start nitro sniper")

        print(f"\n\t{Fore.MAGENTA}Please make your choice{Fore.RESET}", end='')
        try:
            choice = int(input("  :  "))

            if choice == 1:
                self.clear_console()
                self.execute()

            else:
                self.clear_console()
                self.start_menu()

        except ValueError:
            self.clear_console()
            self.start_menu()

    async def on_connect(self):
        print(f"{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S %p')}{Fore.RESET} ({Fore.MAGENTA}CONNECTED{Fore.RESET}) => Logged in as {self.user.name} | {self.user.id}")

    async def claim_code(self, code: str):
        """Basic shortcut function to claim a gift code and return data"""
        r = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                          headers=self.client_headers(),
                          json={'channel_id': None, 'payment_source_id': None})
        if 'subscription_plan' not in r.text:
            try:
                message = r.json()['message']
            except (AttributeError, IndexError, KeyError):
                message = "cloudflare"
            return {'valid': False, 'message': message}
        else:
            return {'valid': True, 'message': r.json()}
              
    async def on_message(self, message):
        try:
            code = re.search(r'(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)',
                             message.content)
            nitro_code = code.group(2)
            if code:
                if len(nitro_code) == 16 or len(nitro_code) == 24:
                    data = await self.claim_code(nitro_code)
                    data_message = data['message']
                    if 'subscription_plan' in data_message:
                        print(f"{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S %p')}{Fore.RESET} ({Fore.GREEN}Nitro Claimed{Fore.RESET}) - ({Fore.CYAN}{message.guild}{Fore.RESET}) - ({Fore.CYAN}{message.author.name}#{message.author.discriminator}{Fore.RESET}) - ({nitro_code})")
                    else:
                        print(f"{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S %p')}{Fore.RESET} ({Fore.RED}Nitro {data_message}{Fore.RESET}) - ({Fore.CYAN}{message.guild}{Fore.RESET}) - ({Fore.CYAN}{message.author.name}#{message.author.discriminator}{Fore.RESET}) - ({nitro_code})")

        except AttributeError:
            pass

    @staticmethod
    def check_if_connection_exists():
        """Checks if a internet connection exists (needed to run discord.py)"""
        try:
            requests.get('https://google.com/')
            return True
        except:
            return False

    def execute(self):
        """Executes the bot"""
        try:
            if self.check_if_connection_exists():
                super().run(self.token, bot=False)
            else:
                print(f"{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S %p')}{Fore.RESET} - (CONNECTION_ERR)")
                input("\n\n\nPress any key to exit...\n")
        except discord.errors.LoginFailure as e:
            print(f"{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S %p')}{Fore.RESET} - ({Fore.RED}{e}{Fore.RESET})")
            input("\n\n\nPress any key to exit...\n")


if __name__ == '__main__':
    if platform.system() != 'Linux':
        init(convert=True)
    client = Sniper()
    client.start_menu()