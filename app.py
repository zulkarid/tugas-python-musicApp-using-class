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
    

class sistem_playlist: 
    def __init__(self):
        self.playlists = {}  #dictionary sebagai wadah playlist
        self.max_playlist = 5
        self.current_playlist = None
        self.current_song_index = None
    
    def buat_playlist(self, nama):
        if len(self.playlists) >= self.max_playlist:
            print(" telah mencapai jumlah maximum 5 playlist, tambah premium kalau ingin tambah")
            return

        if nama in self.playlists:
            print(f"nama playlist dengan nama: '{nama}' sudah terpakai, cari yang lain! ")
            return

        self.playlists[nama] = [] #List lagu, dianalogikan sebagai Singly Linked List
        print(f"Playlist '{nama}' berhasil dibuat, MANTAB!!!")

    def hapus_playlist(self, nama):
        if nama in self.playlists:
            del self.playlists[nama]
            print(f"playlist: '{nama}' berhasil dihapus.")
        else:
            print("yakin itu nama playlistnya?? ga ada bro!")


    def tambah_lagu(self, playlist, judul):
        if playlist in self.playlists:
            self.playlists[playlist].append(judul)
            print(f"lagu judul: {judul}' ditambahkan ke playlist '{playlist}'.")
        else:
            print("yakin itu nama playlistnya?? ga ada bro")

    def hapus_lagu(self, playlist, judul):
        if playlist not in self.playlists:
            print("yakin itu nama playlistnya?? ga ada bro")
            return

        if judul in self.playlists[playlist]:
            self.playlists[playlist].remove(judul)
            print(f"Lagu berjudul: '{judul}' telah dihapus dari playlist: '{playlist}'.")
        else:
            print("yakin itu nama lagunya?? ga ada bro")

    def pilih_playlist(self, nama):
        if nama not in self.playlists:
            print("yakin itu nama playlistnya?? ga ada bro")
            return False

        self.current_playlist = nama
        return True

    def daftar_lagu(self, playlist): #Singly Linked List
        if playlist in self.playlists:
            return self.playlists[playlist]
        return []
    

class ModeMainMusik:
    def __init__(self, playlist_manager):
        self.pm = playlist_manager

    def play(self, index):
        self.pm.current_song_index = index
        playlist = self.pm.current_playlist
        lagu = self.pm.playlists[playlist][index]

        while True:
            print("===MUSIC PLAYER MODE===")
            print(f"Now Playing : {lagu}")
            print("1. Pause")
            print("2. Next")
            print("3. Previous")
            print("0. Stop Player")

            pilih = input("Pilih menu musik: ")

            if pilih == "1":
                print(f"⏸ Lagu '{lagu}' terpaused.")

            elif pilih == "2":  #Queue
                if index + 1 < len(self.pm.playlists[playlist]):
                    index += 1
                    lagu = self.pm.playlists[playlist][index]
                    print(f"⏭️ lanjut -> putar'{lagu}'")
                else:
                    print("❌ Udah ending kaya hubungan mu!")

            elif pilih == "3":  #Stack
                if index - 1 >= 0:
                    index -= 1
                    lagu = self.pm.playlists[playlist][index]
                    print(f"⏮️ sebelumnya -> putar '{lagu}'")
                else:
                    print("❌ lagu sebelumnya kosong, kaya masa lalumu yang kosong dan hampa!")

            elif pilih == "0":
                print("Menu Player ditutup....")
                break

            else:
                print("Pilih yang tersedia aja, jangan yang lain")

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
