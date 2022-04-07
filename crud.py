# Nama              : Maya Humaerah
# NIM               : 200511024
# Kelas             : R1 Teknik Informatika (Semester 4)
# Dosen Pengampu    : Freddy Wicaksono, M.Kom
# Tugas 1 PBO2

import psycopg2 as db
import os
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor

    try :
        con = db.connect(
        host = "localhost",
        database = "kampus",
        port = 5432,
        user = "maya",
        password = "12345678"
        )
        cursor = con.cursor()
        connected = True
    except :
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

def Tampil():
    a = connect()
    sql="select * from mahasiswa"
    a.execute(sql)
    results = a.fetchall()

    if a.rowcount < 0:
        print("Tidak ada data mahasiswa.")
    else :
        for data in results:
            print(data)

def Entry():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM: ")
    xnama = input("Masukkan Nama Lengkap: ")
    xidfk = input("Masukkan ID Fakultas (1 .. 5): ")
    xidpr = input("Masukkan ID Prodi (1 .. 10): ")
    a = connect()
    sql = "insert into mahasiswa (nim, nama, idfakultas, idprodi) values ('"+xnim+"','"+xnama+"','"+xidfk+"','"+xidpr+"')"
    a.execute(sql)
    con.commit()
    print("Entry is done.")

def Cari():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim +"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("search is done.")

def Ubah():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini :")
    print(record)
    row = a.rowcount
    if(row==1):
        print("Silahkan untuk mengubah data..")
        xnama = input("Masukkan Nama Lengkap: ")
        xidfk = input("Masukkan ID Fakultas (1 .. 5): ")
        xidpr = input("Masukkan ID Prodi (1 .. 10): ")
        a = connect()
        sql = "update mahasiswa set nama='" + xnama +"', idfakultas='" + xidfk + "', idprodi='" + xidpr + "' where nim='" + xnim + "'"
        a.execute(sql)
        con.commit()
        print("Update is done.")
        sql="select * from mahasiswa where nim='" + xnim + "'"
        a.execute(sql)
        rec = a.fetchall()
        print("Data setelah diubah :")
        print(rec)

    else:
        print("Data tidak ditemukan")

def Hapus():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini :")
    print(record)
    row = a.rowcount
    if(row==1):
        jwb=input("Apakah ingin menghapus data? (y/t)")
        if(jwb.upper()=="Y"):
            a = connect()
            sql = "delete from mahasiswa where nim='" + xnim + "'"
            a.execute(sql)
            con.commit()
            print("Delete is done.")
        else:
            print("Data batal untuk dihapus.")
    else:
        print("Data tidak ditemukan")

def show_menu():
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Tampilkan Data")
    print("2. Insert Data")
    print("3. Cari Data")
    print("4. Update Data")
    print("5. Hapus Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    os.system("cls")

    if menu == "1":
        Tampil()
    elif menu == "2":
        Entry()
    elif menu == "3":
        Cari()
    elif menu == "4":
        Ubah()
    elif menu == "5":
        Hapus()
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")

if __name__ == "__main__":
  while(True):
      show_menu()