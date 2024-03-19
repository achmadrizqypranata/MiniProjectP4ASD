# Achmad Rizqy Pranata - 2209116086
# Program CRUD Pembelian Game Digital (Steam) dengan Fitur tambahan yaitu fitur Searching menggunakan Jump Search

class Node:
    def __init__(self, id_game, judul, genre, harga, tipe):
        self.id_game = id_game
        self.judul = judul
        self.genre = genre
        self.harga = harga
        self.tipe = tipe
        self.next = None

class GameSteam:
    def __init__(self):
        self.head = None

    def tambah_game_awal(self, id_game, judul, genre, harga, tipe):
        new_node = Node(id_game, judul, genre, harga, tipe)
        new_node.next = self.head
        self.head = new_node
        print("Game berhasil ditambahkan ke Steam.")

    def merge_sort(self, head, key='id_game', order='ascending'):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head, key, order)
        right = self.merge_sort(next_to_middle, key, order)

        sorted_list = self.merge(left, right, key, order)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right, key, order):
        if left is None:
            return right
        if right is None:
            return left

        comparison_function = self.get_comparison_function(key, order)

        if comparison_function(left, right):
            result = left
            result.next = self.merge(left.next, right, key, order)
        else:
            result = right
            result.next = self.merge(left, right.next, key, order)

        return result

    def get_comparison_function(self, key, order):
        if order == 'ascending':
            return self.less_than if key == 'id_game' else self.compare_strings_asc
        elif order == 'descending':
            return self.greater_than if key == 'id_game' else self.compare_strings_desc

    def less_than(self, node1, node2):
        return node1.id_game < node2.id_game

    def greater_than(self, node1, node2):
        return node1.id_game > node2.id_game

    def compare_strings_asc(self, node1, node2):
        return node1.judul.lower() < node2.judul.lower()

    def compare_strings_desc(self, node1, node2):
        return node1.judul.lower() > node2.judul.lower()

    def tampilkan_game(self, key='id_game', order='ascending'):
        sorted_head = self.merge_sort(self.head, key, order)
        temp = sorted_head
        if temp is None:
            print("Steam belum memiliki game atau DLC.")
        else:
            print("Daftar Game dan DLC di Steam:")
            while temp:
                print(f"ID: {temp.id_game}, Judul: {temp.judul}, Genre: {temp.genre}, Harga: {temp.harga}, Tipe: {temp.tipe}")
                temp = temp.next

    def perbarui_game(self, id_game, judul=None, genre=None, harga=None, tipe=None):
        temp = self.head
        while temp is not None:
            if temp.id_game == id_game:
                if judul:
                    temp.judul = judul
                if genre:
                    temp.genre = genre
                if harga:
                    temp.harga = harga
                if tipe:
                    temp.tipe = tipe
                print("Data game atau DLC berhasil diperbarui.")
                return
            temp = temp.next
        print("ID game tidak ditemukan.")

    def hapus_game(self, id_game):
        if self.head is None:
            print("Steam belum memiliki game atau DLC.")
            return

        temp = self.head

        if temp.id_game == id_game:
            self.head = temp.next
            temp = None
            print("Game atau DLC berhasil dihapus dari Steam.")
            return

        while temp is not None:
            if temp.id_game == id_game:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print("ID game tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None
        print("Game atau DLC berhasil dihapus dari Steam.")
    
    def jump_search_id(self, id_game):
        if self.head is None:
            print("Steam belum memiliki game atau DLC.")
            return None

        jump = 3
        index = -1

        temp = self.head
        while temp:
            index += 1
            if temp.id_game == id_game:
                return temp
            temp = temp.next

        print("ID game tidak ditemukan.")
        return None

    def jump_search_nama(self, nama_game):
        if self.head is None:
            print("Steam belum memiliki game atau DLC.")
            return None

        jump = 3
        index = -1

        temp = self.head
        while temp:
            index += 1
            if temp.judul.lower() == nama_game.lower():
                return temp
            temp = temp.next

        print("Judul game tidak ditemukan.")
        return None



def main():
    game_steam = GameSteam()

    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Game/DLC")
        print("2. Tampilkan Game/DLC")
        print("3. Perbarui Game/DLC")
        print("4. Hapus Game/DLC")
        print("5. Keluar")
        print("6. Cari Game/DLC")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            id_game = input("Masukkan ID game: ")
            judul = input("Masukkan judul game: ")
            genre = input("Masukkan genre game: ")
            harga = float(input("Masukkan harga game: "))
            tipe = input("Masukkan tipe (Games/DLC): ")
            game_steam.tambah_game_awal(id_game, judul, genre, harga, tipe)
        elif pilihan == '2':
            key = input("Pilih kunci sorting (id_game/judul): ")
            order = input("Pilih urutan sorting (ascending/descending): ")
            game_steam.tampilkan_game(key, order)
        elif pilihan == '3':
            id_game = input("Masukkan ID game yang akan diperbarui: ")
            judul = input("Masukkan judul baru (biarkan kosong jika tidak ingin mengubah): ")
            genre = input("Masukkan genre baru (biarkan kosong jika tidak ingin mengubah): ")
            harga = input("Masukkan harga baru (biarkan kosong jika tidak ingin mengubah): ")
            tipe = input("Masukkan tipe baru (biarkan kosong jika tidak ingin mengubah): ")
            if judul or genre or harga or tipe:
                game_steam.perbarui_game(id_game, judul, genre, harga, tipe)
            else:
                print("Tidak ada perubahan yang dilakukan.")
        elif pilihan == '4':
            id_game = input("Masukkan ID game/DLC yang akan dihapus: ")
            game_steam.hapus_game(id_game)
        elif pilihan == '5':
            print("Terima kasih telah memperbaiki data ku (｡˃ ᵕ < ) -Steam ")
            break
        elif pilihan == '6':
            search_by = input("Masukkan kriteria pencarian (id/nama): ")
            if search_by == 'id':
                id_game = input("Masukkan ID game yang ingin dicari: ")
                game = game_steam.jump_search_id(id_game)
                if game:
                    print(f"ID: {game.id_game}, Judul: {game.judul}, Genre: {game.genre}, Harga: {game.harga}, Tipe: {game.tipe}")
                else:
                    print("Game dengan ID tersebut tidak ditemukan.")
            elif search_by == 'nama':
                nama_game = input("Masukkan nama game yang ingin dicari: ")
                game = game_steam.jump_search_nama(nama_game)
                if game:
                    print(f"ID: {game.id_game}, Judul: {game.judul}, Genre: {game.genre}, Harga: {game.harga}, Tipe: {game.tipe}")
                else:
                    print("Game dengan nama tersebut tidak ditemukan.")
            else:
                print("Kriteria pencarian tidak valid.")

        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
