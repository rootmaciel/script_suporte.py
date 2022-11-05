print('''
        [+]---------------------------------------------[+]
        [+]Script de Automatização - Ferramentas Básicas[+]
        [+]---------------------------------------------[+]
        [+]     S.O Ubuntu 18 - GOX Internet Suporte    [+]
        [+]---------------------------------------------[+]''')
import os
print("\nAtualizando Repositório Ubuntu...\n")
os.system("apt -y update")
os.system("apt -y upgrade")
print('''--------------------------------------------------------------------------------------
   [+] Update e Upgrade [OK].\n''')
print("Iniciando o processo de instalação de ferramentas básicas via apt install...")
print('''
	[+]Veja a baixo as ferramentas a serem instaladas[+]

	[+]1-Diodon OBS: P/Configura Win+V do teclado
	[+]2-Firefox v.50 OBS: P/Acesso remoto aos Roteadores
	[+]3-BitDefender
	[+]4-Nmap
	[+]5-figlet''')
import time
time.sleep(5)
print("\nInstalando Diodon, Nmap, Figlet...\n")
time.sleep(3)
os.system("apt install diodon nmap figlet -y")

print("\nInstalando Brave...\n")
time.sleep(3)
os.system("apt install apt-transport-https curl")
os.system("curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main |sudo tee /etc/apt/sources.list.d/brave-browser-release.list" ')
os.system("apt update")
os.system("apt install brave-browser -y")

print("\nFazendo Download do Frefox-50.0...\n")
time.sleep(3)
os.system("wget https://ftp.mozilla.org/pub/firefox/releases/50.0/linux-x86_64/br/firefox-50.0.tar.bz2")
os.system("tar -xvf firefox-50.0.tar.bz2")
os.system("chmod 777 firefox")

print("\n[OK]Instalando BitDefender...\n")
time.sleep(4)
os.system("wget https://cloud.gravityzone.bitdefender.com/Packages/NIX/0/52ALpP/setup_downloader.tar")
os.system("tar -xvf setup_downloader.tar")
os.system("chmod 777 installer")
input("\nAperte Enter para instalar... OBS: Para verificar o monitoramento da instalação abre outro terminal como root/sudo su e digite: tail -f /opt/bitdefender-security-tools/var/log/installer.log\n")
os.system("./installer")
input("\nAperte Enter para continuar...Para verificar se o agente foi instalado, execute em outro terminal: (systemctl status bdsec*)\n")
