import sqlite3

'''Ket noi database'''
conn=sqlite3.connect('/info.db')

'''Tao cursor'''
c=conn.cursor()

'''Them phan tu'''
# thanhpho=[
#     ('18CDT1SP1','Da Nang'),
#     ('18CDT1SP2','Ha Noi'),
#     ('18CDT1SP3','Ho Chi Minh')
# ]

# c.executemany("INSERT INTO thongtin VALUES (?,?)",thanhpho)

'''Tao table'''
# c.execute("""CREATE TABLE thongtin(
#     ma_barcode text,
#     tinh_thanhpho text
# )
#         """)

'''Xóa table'''
# c.execute("DROP TABLE thongtin")
'''Xóa record'''
#c.execute("DELETE from thongtin WHERE rowid = 3")

c.execute("SELECT rowid,* FROM thongtin")

items=c.fetchall()
print (items)
for item in items:
    print(item)
conn.commit()
conn.close()