import os, requests, ctypes, json
from colorama import Fore, Style, init
init(convert=True)

info = '[UZI]-Whois by https://github.com/zvodka-git'
ctypes.windll.kernel32.SetConsoleTitleW(info)

xmenu = f'''{Style.BRIGHT}

 ███╗██╗   ██╗███████╗██╗███╗
 ██╔╝██║   ██║╚══███╔╝██║╚██║
 ██║ ██║   ██║  ███╔╝ ██║ ██║{Fore.YELLOW}┌┬┐┌─┐┌─┐┬  
 ██║ ██║   ██║ ███╔╝  ██║ ██║{Fore.YELLOW} │ │ ││ ││  
 ███╗╚██████╔╝███████╗██║███║{Fore.YELLOW} ┴ └─┘└─┘┴─┘{Fore.BLACK}
 ╚══╝ ╚═════╝ ╚══════╝╚═╝╚══╝

 {Fore.MAGENTA}[1]- {Fore.WHITE}conseguir informacion de una ip

'''.replace("█", f"{Fore.WHITE}█{Fore.BLACK}")

print(xmenu)
while True:
    print(f" {Fore.WHITE}Elige una opcion :{Fore.MAGENTA}", end='')
    uzi = input()
    if uzi == '1':
        print(f" {Fore.WHITE}Ingresa la direccion ip :{Fore.MAGENTA}", end='')
        ip = input()
        try:
            ip_api = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,country,region,regionName,city,district,zip,lat,lon,currency,isp,org,mobile,proxy,hosting,query')
            ip_api = ip_api.text
            ip_api = json.loads(ip_api)

            status = ip_api.get('status')
            if status == 'fail':
                print(f' {Fore.RED}LA IP NO ES VALIDA {ip}!!', end='')
                os.system('pause>nul & cls')
                print(xmenu)
            else:
                os.system('cls')
                país = ip_api.get('country')
                region = ip_api.get('region')
                region_ = ip_api.get('regionName')
                ciudad = ip_api.get('city')
                distrito = ip_api.get('district')
                codigo_zip = ip_api.get('zip')
                latitud = ip_api.get('lat')
                longitud = ip_api.get('lon')
                moneda = ip_api.get('currency')
                isp = ip_api.get('isp')
                org = ip_api.get('org')
                celular = ip_api.get('mobile')
                proxy = ip_api.get('proxy')
                ip_menu = f'''

 ███╗██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗███╗
 ██╔╝██║    ██║██║  ██║██╔═══██╗██║██╔════╝╚██║
 ██║ ██║ █╗ ██║███████║██║   ██║██║███████╗ ██║ {Fore.YELLOW}╦╔═╗
 ██║ ██║███╗██║██╔══██║██║   ██║██║╚════██║ ██║ {Fore.YELLOW}║╠═╝
 ███╗╚███╔███╔╝██║  ██║╚██████╔╝██║███████║███║ {Fore.YELLOW}╩╩ {Fore.BLACK}
 ╚══╝ ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚══╝
 
 {Fore.RED}>>[ip]- {Fore.WHITE}{ip}
 {Fore.YELLOW}>>[país]- {Fore.WHITE}{país}
 {Fore.MAGENTA}>>[region]- {Fore.WHITE}{region}
 {Fore.MAGENTA}>>[regionName]- {Fore.WHITE}{region_}
 {Fore.YELLOW}>>[ciudad]- {Fore.WHITE}{ciudad}
 {Fore.YELLOW}>>[distrito]- {Fore.WHITE}{distrito}
 {Fore.RED}>>[codigoZIP]- {Fore.WHITE}{codigo_zip}
 {Fore.MAGENTA}>>[latitud]- {Fore.WHITE}{latitud}
 {Fore.MAGENTA}>>[longitud]- {Fore.WHITE}{longitud}
 {Fore.YELLOW}>>[moneda]- {Fore.WHITE}{moneda}
 {Fore.RED}>>[isp]- {Fore.WHITE}{isp}
 {Fore.RED}>>[org]- {Fore.WHITE}{org}
 {Fore.YELLOW}>>[DatosMoviles]- {Fore.WHITE}{celular}
 {Fore.YELLOW}>>[Proxy]- {Fore.WHITE}{proxy}
'''.replace("█", f"{Fore.WHITE}█{Fore.BLACK}")
                print(ip_menu, end='')
                os.system('pause>nul')
        except:
            os.system('cls')
            print(xmenu)
            
    os.system('cls')
    print(xmenu)

        
        
