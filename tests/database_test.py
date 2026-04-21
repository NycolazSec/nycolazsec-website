import pymysql
import colorama
import socket


class DatabaseTest:
    def __init__(self, host, user, password, database) -> None:
        self.host = host[0]
        self.user = user[0]
        self.password = password[0]
        self.database = database[0]
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(colorama.Fore.GREEN + "[+] Database Connection Successful")
        except pymysql.Error:
            print(colorama.Fore.RED + "[!] Error connecting to the database" + colorama.Fore.RESET)
    
    def __del__(self):
        if hasattr(self, 'connection'):
            self.connection.close()
            print(colorama.Fore.YELLOW + "[!] Database Connection Closed")