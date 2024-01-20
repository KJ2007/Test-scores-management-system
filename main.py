from libs.xu_ly_diem import *

lstDiemThi = []

print("CHUONG TRINH QUAN LY DIEM THI THEO MON")
while True:
    print("1: Đọc file điểm thi\n2: Thêm điểm thi\n3: Danh sách điểm thi\n4: Tra cứu điểm thi\n5: Xóa điểm thi\n6: Thống kê\n7: Lưu danh sách điểm thi ra file")
    lua_chon = int(input("Chọn chức năng cần làm việc: "))
    if lua_chon == 1:
        kq = doc_file_csv(lstDiemThi)
        if kq == 1:
            print("Đã đọc file thành công")
    elif lua_chon == 2:
        them_diem_thi(lstDiemThi)
    elif lua_chon == 3:
        in_ds_diem_thi(lstDiemThi)
    elif lua_chon == 4:
        ma_hs = input("Nhập Mã học sinh: ")
        tra_cuu_diem_thi(lstDiemThi, ma_hs)
    elif lua_chon == 5:
        ma_hs = input("Nhập Mã học sinh: ")
        xoa_diem_thi(lstDiemThi, ma_hs)
    elif lua_chon == 6:
        thong_kê(lstDiemThi)
    else:
        kq = luu_file_csv(lstDiemThi)
        if kq == 1:
            print("Đã lưu file thành công")
    tiep_tuc = int(input("Ban co muon tiep tuc (1:TT): "))
    if tiep_tuc != 1:
        break