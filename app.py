import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# singly linked list for penyimpanan lagu
class NodeLagu:
    def __init__(self, id_lagu, judul, artist, genre, duration=None):
        self.id_lagu = id_lagu
        self.judul = judul
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.next = None


class MusicLibrary:
    def __init__(self):
        self.head = None

    def tambah_lagu(self, id_lagu, judul, artist, genre, duration=None):
        node = NodeLagu(id_lagu, judul, artist, genre, duration)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def hapus_lagu(self, id_lagu):
        cur = self.head
        prev = None
        while cur:
            if cur.id_lagu == id_lagu:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def tampilkan_lagu(self):
        cur = self.head
        if not cur:
            print("Music Library kosong.")
            return
        print("ID | Judul")
        while cur:
            print(f"{cur.id_lagu} | {cur.judul}")
            cur = cur.next

    def cari_lagu(self, id_lagu, judul):
        cur = self.head
        while cur:
            if cur.id_lagu == id_lagu and cur.judul == judul:
                return True
            cur = cur.next
        return False


# quenue lagu
class QueueLagu:
    def __init__(self):
        self.data = []

    def enqueue(self, lagu):
        self.data.append(lagu)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None


# informasi akun
class akun:
    def __init__(self):
        self.admin_data = {"username": "atika", "password": "8910"}
        self.user_data = {"username": "widya", "password": "1234"}

    def admin(self, u, p):
        return u == self.admin_data["username"] and p == self.admin_data["password"]

    def user(self, u, p):
        return u == self.user_data["username"] and p == self.user_data["password"]


# sistem playlist
class SistemPlaylist:
    def __init__(self):
        self.playlists = {}
        self.library = MusicLibrary()
        self.current_playlist = None

    def buat_playlist(self, nama):
        if nama in self.playlists:
            print("Playlist sudah ada!")
            return
        self.playlists[nama] = []
        print(f"Playlist '{nama}' dibuat.")

    def lihat_playlist(self):
        if not self.playlists:
            print("Belum ada playlist.")
            return
        print("Daftar Playlist:")
        for p in self.playlists:
            print("-", p)

    def tambah_lagu_playlist(self, playlist, id_lagu, judul):
        if playlist not in self.playlists:
            print("Playlist tidak ditemukan.")
            return

        if not self.library.cari_lagu(id_lagu, judul):
            print("Lagu tidak ada di Music Library.")
            return

        self.playlists[playlist].append((id_lagu, judul))
        print("Lagu ditambahkan ke playlist.")

    def hapus_lagu_semua_playlist(self, id_lagu):
        for p in self.playlists:
            self.playlists[p] = [l for l in self.playlists[p] if l[0] != id_lagu]


# Menu player
class ModeMainMusik:
    def __init__(self, sp):
        self.sp = sp

    def play(self, playlist):
        if playlist not in self.sp.playlists:
            print("Playlist tidak ada.")
            return

        queue = QueueLagu()
        for lagu in self.sp.playlists[playlist]:
            queue.enqueue(lagu[1])

        lagu = queue.dequeue()
        if not lagu:
            print("Playlist kosong.")
            return

        while True:
            clear_screen()
            print("=== MUSIC PLAYER ===")
            print("Now Playing:", lagu)
            print("1. Pause")
            print("2. Next")
            print("0. Stop")

            pilih = input("Pilih: ")
            if pilih == "1":
                print("⏸ Pause")
            elif pilih == "2":
                next_lagu = queue.dequeue()
                if next_lagu:
                    lagu = next_lagu
                else:
                    print("Playlist selesai.")
                    break
            elif pilih == "0":
                break
            else:
                print("Menu tidak valid.")


# Menu Utama
akun_obj = akun()
sp = SistemPlaylist()
player = ModeMainMusik(sp)

# data dummy lagu
sp.library.tambah_lagu("1", "Senja di Kota", "Arsy Widianto", "Pop", "4:12")
sp.library.tambah_lagu("2", "Hujan Tengah Malam", "Payung Teduh", "Indie", "3:58")
sp.library.tambah_lagu("3", "Melukis Senja", "Budi Doremi", "Pop", "4:20")
sp.library.tambah_lagu("4", "Rumah Kita", "God Bless", "Rock", "5:01")
sp.library.tambah_lagu("5", "Sampai Jadi Debu", "Banda Neira", "Folk", "4:35")
sp.library.tambah_lagu("6", "Secukupnya", "Hindia", "Indie", "4:40")
sp.library.tambah_lagu("7", "Akad", "Payung Teduh", "Indie", "4:18")
sp.library.tambah_lagu("8", "Laskar Pelangi", "Nidji", "Pop", "4:45")

# data dummy playlist + lagu
sp.playlists["buat santai sore"] = [
    ("1", "Senja di Kota"),
    ("3", "Melukis Senja"),
    ("5", "Sampai Jadi Debu")
]

sp.playlists["lagu vibes"] = [
    ("2", "Hujan Tengah Malam"),
    ("6", "Secukupnya"),
    ("7", "Akad")
]

sp.playlists["Pop & rock"] = [
    ("4", "Rumah Kita"),
    ("8", "Laskar Pelangi")
]

while True:
    clear_screen()
    print("1. Admin")
    print("2. User")
    print("0. Exit")
    pilih = input("Pilih: ")

    if pilih == "0":
        print("Keluar aplikasi.")
        break

    username = input("Username: ")
    password = input("Password: ")

    # menu ADMIN
    if pilih == "1" and akun_obj.admin(username, password):
        logged_in = True

        while logged_in:
            clear_screen()
            print("=== ADMIN MENU ===")
            print("1. Tambah Lagu")
            print("2. Hapus Lagu")
            print("3. Lihat Library")
            print("0. Logout")

            m = input("Pilih: ")

            if m == "1":
                sp.library.tambah_lagu(
                    input("ID Lagu: "),
                    input("Judul: "),
                    input("Artist: "),
                    input("Genre: "),
                    input("Duration (opsional): ")
                )

            elif m == "2":
                id_lagu = input("ID lagu: ")
                if sp.library.hapus_lagu(id_lagu):
                    sp.hapus_lagu_semua_playlist(id_lagu)
                    print("Lagu dihapus dari library & semua playlist.")
                else:
                    print("Lagu tidak ditemukan.")

            elif m == "3":
                sp.library.tampilkan_lagu()
                input("\nEnter untuk lanjut...")

            elif m == "0":
                print("Logout admin...")
                logged_in = False

            else:
                print("Menu tidak valid.")
                input("Enter untuk lanjut...")

    # menu USER
    elif pilih == "2" and akun_obj.user(username, password):
        logged_in = True

        while logged_in:
            clear_screen()
            print("=== USER MENU ===")
            print("1. Buat Playlist")
            print("2. Lihat Playlist")
            print("3. Tambah Lagu ke Playlist")
            print("4. Play Playlist")
            print("0. Logout")

            m = input("Pilih: ")

            if m == "1":
                sp.buat_playlist(input("Nama playlist: "))

            elif m == "2":
                sp.lihat_playlist()
                input("\nEnter untuk lanjut...")

            elif m == "3":
                sp.library.tampilkan_lagu()
                playlist = input("Nama playlist: ")
                id_lagu = input("ID lagu: ")
                judul = input("Judul lagu: ")
                sp.tambah_lagu_playlist(playlist, id_lagu, judul)
                input("\nEnter untuk lanjut...")

            elif m == "4":
                player.play(input("Nama playlist: "))
                input("\nEnter untuk lanjut...")

            elif m == "0":
                print("Logout user...")
                logged_in = False

            else:
                print("Menu tidak valid.")
                input("Enter untuk lanjut...")

    else:
        print("Login gagal.")
        input("tekan enter buat lanjut")
