import os
import time
import subprocess

def painel():
    while True:
        os.system("cls")
        art()
        print("[1] Instalar scoop.sh e apps")
        print("[2] Apps de arranque")
        print("[3] Pontos de restauro")
        print("[0] Sair")
        print("[99] Creditos")
        x = input("Escolhe uma opção: ")

        if x == "1":
            instalar_scoop()
        elif x == "2":
            desativar_arranque()
        elif x == "3":
            ponto()
        elif x == "0":
            print("Saindo...")
            break
        elif x == "99":
            creditos()
        else:
            print("Opção inválida.")
            input("Pressiona Enter para tentar novamente...")

def art():
    os.system('cls')
    art = r'''
              (
               )
              (
        /\  .-"""-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"""-;///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/
    '''
    print(art)

def run_powershell_command(cmd):
    completed = subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True
    )
    if completed.returncode != 0:
        print("Erro:", completed.stderr)
    else:
        print(completed.stdout)

def instalar_scoop():
    os.system('cls')
    os.system('powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"')
    os.system('powershell -Command "iwr -useb get.scoop.sh | iex"')
    time.sleep(2)
    os.system('cls')
    print("Desejas instalar mais partições a partir do scoop? (Y/N)")
    opcao1 = input()
    os.system('cls')
    if opcao1.lower() == "y":
        print("==================== scoop.sh ====================")
        print("[1] git - controlo de versoes")
        print("[2] python - linguagem de programacao")
        print("[3] 7zip - open source compactador")
        print("[4] vscode - editor de codigo")
        print("[5] curl - transferencias de dados")
        print("[6] winfetch - informacoes de sistema")
        print("[7] nmap - estudo de ips e redes")
        print("==================================================")
        opcao2 = input("Quero instalar (separa por espaços): ")

        lista_opcoes = [opcao.strip() for opcao in opcao2.split(" ") if opcao.strip() != ""]

        for op in lista_opcoes:
            if op == "1":
                os.system("scoop install git")
            elif op == "2":
                os.system("scoop install python")
            elif op == "3":
                os.system("scoop install 7zip")
            elif op == "4":
                os.system("scoop install vscode")
            elif op == "5":
                os.system("scoop install curl")
            elif op == "6":
                os.system("scoop install winfetch")
            elif op == "7":
                os.system("scoop install nmap")
            else:
                print(f"Opção inválida: {op}")
        
        time.sleep(3)
        os.system('cls')
        print("Consegues aceder às instalações em \"C:\\Users\\utilizador\\scoop\\apps\"")
        input("Pressiona Enter para voltar ao menu...")
        os.system('cls')

def desativar_arranque():
    while True:
        os.system('cls')
        print("[1] Listar apps no arranque")
        print("[2] Remover tudo do arranque")
        print("[0] Voltar ao menu principal")
        y = input("Opcao: ")
        os.system('cls')
        if y == "1":
            os.system(
                'powershell -Command "Get-CimInstance -ClassName Win32_StartupCommand | '
                'Select-Object Name,Command,Location | Format-Table -AutoSize"'
            )
            input("Pressiona Enter para voltar ao menu de arranque...")
        elif y == "2":
            comando = (
                'powershell -Command "Get-CimInstance -ClassName Win32_StartupCommand | '
                'ForEach-Object { '
                'if ($_.Location -like \'HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run*\') { '
                'Remove-ItemProperty -Path $_.Location -Name $_.Name -ErrorAction SilentlyContinue } '
                '}"'
            )
            os.system(comando)
            print("Todas as apps de arranque do utilizador foram removidas.")
            input("Pressiona Enter para voltar ao menu de arranque...")
        elif y == "0":
            break
        else:
            print("Opção inválida.")
            time.sleep(2)

def run_powershell_command_as_admin(cmd):
    full_cmd = f"{cmd}; Pause"
    subprocess.run([
        "powershell",
        "-Command",
        f"Start-Process powershell -ArgumentList '-NoProfile -Command \"{full_cmd}\"' -Verb RunAs"
    ])

def criar_ponto_restauro_admin():
    cmd = 'Checkpoint-Computer -Description \\"Ponto de Restauro Manual\\" -RestorePointType \\"MODIFY_SETTINGS\\"; Read-Host \\"Pressiona Enter para fechar\\"'
    powershell_cmd = f'Start-Process powershell -ArgumentList \'-NoExit -Command "{cmd}"\' -Verb RunAs'
    subprocess.run(["powershell", "-Command", powershell_cmd])

def ponto():
    while True:
        os.system('cls')
        print("Pontos de restauro sao essenciais caso fizeres merda no teu pc...")
        print("[1] Criar ponto de restauro")
        print("[2] Listar pontos de restauro")
        print("[0] Voltar ao menu principal")
        opc = input("Opção: ")

        if opc == "1":
            criar_ponto_restauro_admin()
            print("Ponto de restauro criado!")
            input("Pressiona Enter para continuar...")
        elif opc == "2":
            run_powershell_command_as_admin("Get-ComputerRestorePoint | Format-Table -AutoSize")
            input("Pressiona Enter para continuar...")
        elif opc == "0":
            break
        else:
            print("Opção inválida.")
            time.sleep(2)

def creditos():
    os.system('cls')
    cred_art()
    time.sleep(7)

def cred_art():
    art = r'''
 / \-----------------, 
 \_,|                | 
    |    secondzxs   | 
    |  ,---------------
    \_/______________/  
'''
    print(art)
    print("mail: wonttrackme@proton.me")
    print("discord: secondzxs")
    print("")
    print("Obrigado por usares, a sair dentro de 10 segundos...")
    time.sleep(10)
    
painel()
