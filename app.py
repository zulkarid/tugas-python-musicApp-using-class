class data: 
    def dataku (self, baru):
        self.baru = baru
        print(self.baru)


class akun:
    def __init__(self):

        self.data_admin = {"username":"atika", "password": "8910"}
        self.data_user = {"username":"widya", "password":"1234"}


    def admin(self, username, password):
        if username == self.data_admin["username"] and password == self.data_admin["password"]:
            return True
        return False


    def user(self, username, password):
        if username == self.data_user["username"] and password == self.data_user["password"]:
            return True
        return False
    

class fitur:
    def newsong(self, playlist):
        self.playlist = playlist

    def tambah_lagu(self, lagu):
        self.lagu = lagu

    def ganti_lagu_playlist(self, list):
        self.list = list

    def delete(self,delete):
        self.delete = delete

#------------------------------------------------------------------ batas fitur

    def cari_lagu(self,cari):
        self.cari = cari

    def play_song(self,play):
        self.play = play

    def pause_song(self,pause):
        self.pause = pause

    def auto_next(self,next,previous):
        self.next = next
        self.previous = previous

    def addToPlaylist(self, Addplaylist):
        self.Addplaylist = Addplaylist


akun = akun()   

print("Akun mu apa bos :")
print("1. Saya Admin")
print("2. Saya User")
pilih = input("hanya boleh pilih satu aja: ")

username = input("Username: ")
password = input("Password: ")

if pilih == "1":
    if akun.admin(username, password):
        print("Awas, ADMIN telah datang!")
    else:
        print("coba lagi bung")

elif pilih == "2":
    if akun.user(username, password):   
        print("Selamat datang wahai USER!")
    else:
        print("coba lagi bung")

else:
    print("Lo milih apa wok!")
