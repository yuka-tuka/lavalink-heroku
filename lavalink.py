
from os import system, environ


class lavalinkserver:

    def __init__(self):
        self.download_command = "curl -s https://api.github.com/repos/Frederikam/Lavalink/releases/18978720 | grep browser_download_url | cut -d '\"' -f 4 | wget -qi -"
        self.change_port = 'sed -i "s|DYNAMICPORT|$PORT|" application.yml'
        self.change_password = 'sed -i "s|DYNAMICPASSWORD|$PASSWORD|" application.yml'
        self.no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
        self.additional = environ.get("ADDITIONAL_JAVA_OPTIONS")
        self.run_command = f"java -jar Lavalink.jar {self.additional}"

    def password_and_port(self):
        print("[INFO] Trocando a porta E Senha...")
        try:
            system(self.change_port)
            if not environ.get("PASSWORD"):
               print("[INFO] Senha padrao foi definida...")
               return system(self.no_password)
            system(self.change_password)
        except BaseException as exc:
            print(f"[ERROR] Erro ao trocar porta E senha... Info: {exc}")
        else:
            print("[INFO] Sucesso ao trocar a porta e a senha...")

    def download(self):
        print("[INFO] Baixando o lavalink...")
        try:
            system(self.download_command)
        except BaseException as exc:
            print(f"[ERROR] Erro ao baixar o lavalink... Info: {exc}")

        else:
            print("[INFO] Sucesso ao baixar o lavalink...")
    
    def run(self):
        self.download()
        self.password_and_port()
        print("[INFO] Iniciando o lavalink.")
        try:
            system(self.run_command)
        except BaseException as exc:
            print(f"[ERROR] Falha ao iniciar o lavalink... Info: {exc}")

if __name__ == "__main__":
   lavalinkserver().run()

