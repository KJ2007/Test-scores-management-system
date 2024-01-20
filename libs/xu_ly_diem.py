import csv

def them_diem_thi(lstDiemThi):
    while True:
        while True:
            ma_hs = input("Nhap Ma hoc sinh: ")
            bi_trung = False
            for i in range(0,len(lstDiemThi)):
                if ma_hs == lstDiemThi[i][0]:
                    bi_trung = True
                    print(f"{ma_hs} bi trung")
                    break
            if bi_trung == False:
                break
        ho_thi_hs = input("Ho ten hoc sinh: ")
        ngay_thi = input("Ngay thi")
        mon_thi = input("Mon thi: ")
        diem_thi = float(input("Diem thi: "))
        while diem_thi < 0 or diem_thi > 10:
            print("Điểm thi không hợp lệ")
            diem_thi = float(input("Diem thi: "))
        ket_qua = "Rớt"
        if diem_thi >= 5:
            ket_qua = "Đậu"
        new_lst = [ma_hs, ho_thi_hs, ngay_thi, mon_thi, diem_thi, ket_qua]
        lstDiemThi.append(new_lst)
        tiep_tuc = int(input("Ban co muon tiep tuc (1:TT): "))
        if tiep_tuc != 1:
            break
    

def in_ds_diem_thi(lstDiemThi):
    print("| Mã HS    | Họ tên            | Ngày thi  | Môn thi | Điểm thi | Kết quả ")
    for i in range(len(0, lstDiemThi)):
        print("| {:8} | {:<18} | {:10} | {:<7} | {:<9} | {:<9}".format(lstDiemThi[i][0], lstDiemThi[i][1], lstDiemThi[i][2], lstDiemThi[i][3], lstDiemThi[i][4], lstDiemThi[i][5]))

def tra_cuu_diem_thi(lstDiemThi, ma_hs):
    for i in range(0,len(lstDiemThi)):
        if lstDiemThi[i][0] == ma_hs:
            print(lstDiemThi[i])
            break

def xoa_diem_thi(lstDiemThi, ma_hs):
    for i in range(0,len(lstDiemThi)):
        if lstDiemThi[i][0] == ma_hs:
            diem_bi_xoa = lstDiemThi[i]
            lstDiemThi.remove(lstDiemThi[i])
            break
    if diem_bi_xoa not in lstDiemThi:
        print("Đã xóa")
    else:
        print("Xóa không thành công")

def thong_kê(lstDiemThi):
    tong_hs_thi = len(lstDiemThi)
    thi_dau = 0
    thi_rot = 0
    for i in range(0,len(lstDiemThi)):
        if lstDiemThi[i][5] == "Đậu":
            thi_dau += 1
        else:
            thi_rot += 1
    ty_le = round((thi_dau/tong_hs_thi),1) + " %"
    print("Tổng số học sinh thi:", tong_hs_thi)
    print("Số học sinh thi đậu: ", thi_dau)
    print("Số học sinh rớt: ", thi_rot)
    print("Tỷ lệ: ", ty_le)

def luu_file_csv(lstDiemThi):
    lstLuu = []
    lstLuu.append(["Mã HS", "Họ tên", "Ngày thi", "Môn thi", "Điểm thi", "Kết quả"])
    with open("files/dsdiemthi.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in lstDiemThi:
            writer.writerow(row)
    return 1

def doc_file_csv(lstDiemThi):
    with open("files/dsdiemthi.csv", mode="r", encoding="utf-8") as f:
        for i in csv.reader(f):
            if i[0] == "Mã HS":
                continue
            diem = [i[0], i[1], i[2], i[3], i[4], i[5]]
            lstDiemThi.append(diem)
    return 1
