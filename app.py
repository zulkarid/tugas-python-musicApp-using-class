import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# singly linked list untuk penyimpanan lagu
class NodeLagu:
    def __init__(self, judul):
        self.judul = judul
        self.next = None


class MusicLibrary:
    def __init__(self):
        self.head = None

    def tambah_lagu(self, judul):
        node = NodeLagu(judul)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def cari_lagu(self, judul):
        cur = self.head
        while cur:
            if cur.judul == judul:
                return True
            cur = cur.next
        return False


# quenue urutan lagu
class QueueLagu:
    def __init__(self):
        self.data = []

    def enqueue(self, lagu):
        self.data.append(lagu)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def kosong(self):
        return len(self.data) == 0


# akun type
class premium:
    def __init__(self):
        self.premium_user = None

    def aktifkan(self, username):
        print("Premium diaktifkan untuk:", username)


class akun:
    def __init__(self):
        self.data_admin = {"username": "atika", "password": "8910"}
        self.data_user = {"username": "widya", "password": "1234"}

    def admin(self, username, password):
        return username == self.data_admin["username"] and password == self.data_admin["password"]

    def user(self, username, password):
        return username == self.data_user["username"] and password == self.data_user["password"]


# playlist
class sistem_playlist:
    def __init__(self):
        self.playlists = {}
        self.max_playlist = 5
        self.current_playlist = None
        self.library = MusicLibrary()

    def buat_playlist(self, nama):
        if len(self.playlists) >= self.max_playlist:
            print(" telah mencapai jumlah maximum 5 playlist, tambah premium kalau ingin tambah")
            return

        if nama in self.playlists:
            print(f"nama playlist dengan nama: '{nama}' sudah terpakai, cari yang lain! ")
            return

        self.playlists[nama] = []
        print(f"Playlist '{nama}' berhasil dibuat, MANTAB!!!")

    def hapus_playlist(self, nama):
        if nama in self.playlists:
            del self.playlists[nama]
            print(f"playlist: '{nama}' berhasil dihapus.")
        else:
            print("yakin itu nama playlistnya?? ga ada bro!")

    def tambah_lagu(self, playlist, judul):
        if playlist in self.playlists:
            self.library.tambah_lagu(judul)   # masuk Singly Linked List
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

    def daftar_lagu(self, playlist):
        if playlist in self.playlists:
            return self.playlists[playlist]
        return []


# sistem player
class ModeMainMusik:
    def __init__(self, playlist_manager):
        self.pm = playlist_manager

    def play(self, index):
        if self.pm.current_playlist is None:
            print("yakin itu nama playlistnya?? ga ada bro")
            return

        playlist = self.pm.current_playlist

        if len(self.pm.playlists[playlist]) == 0:
            print("yakin itu nama lagunya?? ga ada bro")
            return

        if index < 0 or index >= len(self.pm.playlists[playlist]):
            print("yakin itu nama lagunya?? ga ada bro")
            return

        queue = QueueLagu()
        for lagu in self.pm.playlists[playlist]:
            queue.enqueue(lagu)

        lagu = queue.dequeue()

        while True:
            clear_screen()
            print("===MUSIC PLAYER MODE===")
            print(f"Now Playing : {lagu}")
            print("1. Pause")
            print("2. Next")
            print("3. Previous")
            print("0. Stop Player")

            pilih = input("Pilih menu musik: ")

            if pilih == "1":
                print(f"⏸ Lagu '{lagu}' terpaused.")

            elif pilih == "2":
                next_lagu = queue.dequeue()
                if next_lagu:
                    lagu = next_lagu
                    print(f"⏭️ lanjut -> play'{lagu}'")
                else:
                    print("❌ Udah ending!")

            elif pilih == "3":
                print("ini baru pertama woy, mau play sebelumnya gimana?")

            elif pilih == "0":
                print("Menu Player ditutup....")
                break

            else:
                print("Pilih yang tersedia aja, jangan yang lain")
# program utama
akun_obj = akun()

while True:
    print("Akun mu apa bos :")
    print("1. Saya Admin")
    print("2. Saya User")
    print("0. Keluar aplikasi")
    pilih = input("hanya boleh pilih satu aja: ")

    if pilih == "0":
        print("Program ditutup, dadah bosku 👋")
        break

    username = input("Username: ")
    password = input("Password: ")

    logged_in = False

    if pilih == "1" and akun_obj.admin(username, password):
        logged_in = True
    elif pilih == "2" and akun_obj.user(username, password):
        logged_in = True
    else:
        print("coba lagi bung")
        continue

    sp = sistem_playlist()
    player = ModeMainMusik(sp)

    while True:
        clear_screen()
        print("\n=== MENU PLAYLIST ===")
        print("1. Buat Playlist")
        print("2. Hapus Playlist")
        print("3. Tambah Lagu")
        print("4. Hapus Lagu")
        print("5. Pilih Playlist")
        print("6. Daftar Lagu Playlist")
        print("7. Play Musik")
        print("8. Aktifkan fitur premium")
        print("9. Logout")
        print("0. Keluar aplikasi")

        pilih_menu = input("Pilih menu: ")

        if pilih_menu == "1":
            sp.buat_playlist(input("Nama playlist baru: "))

        elif pilih_menu == "2":
            sp.hapus_playlist(input("Nama playlist yang ingin dihapus: "))

        elif pilih_menu == "3":
            sp.tambah_lagu(input("Nama playlist: "), input("Judul lagu: "))

        elif pilih_menu == "4":
            sp.hapus_lagu(input("Nama playlist: "), input("Judul lagu: "))

        elif pilih_menu == "5":
            sp.pilih_playlist(input("Nama playlist: "))

        elif pilih_menu == "6":
            print(sp.daftar_lagu(input("Nama playlist: ")))

        elif pilih_menu == "7":
            player.play(int(input("Index lagu (mulai dari 0): ")))

        elif pilih_menu == "8":
            premium().aktifkan(username)

        elif pilih_menu == "9":
            break

        elif pilih_menu == "0":
            exit()

        else:
            print("Pilih yang tersedia aja, jangan yang lain")
