import os

class QuanLy:
# Danh sách
    def __init__(self):
# Danh sách có sản phẩm
        self.sanpham = {
            1: {"Mã sản phẩm": "SP1", "Tên": "Laptop Dell Inspiron 15", "Giá": 15500000, "Số lượng": 20, "Mô tả": "Laptop 15.6 inch, Intel Core i5, RAM 8GB, SSD 256GB, phù hợp cho học tập và làm việc."},
            2: {"Mã sản phẩm": "SP2", "Tên": "Điện thoại Samsung Galaxy S21", "Giá": 18000000, "Số lượng": 15, "Mô tả": "Smartphone 6.2 inch, camera 64MP, pin 4000mAh, thiết kế sang trọng."},
            3: {"Mã sản phẩm": "SP3", "Tên": "Tai nghe Sony WH-1000XM4", "Giá": 7500000, "Số lượng": 30, "Mô tả": "Tai nghe không dây, khử tiếng ồn, âm thanh chất lượng cao, thời gian sử dụng 30 giờ."},
            4: {"Mã sản phẩm": "SP4", "Tên": "Máy ảnh Canon EOS 2000D", "Giá": 10000000, "Số lượng": 10, "Mô tả": "Máy ảnh DSLR cơ bản, phù hợp cho người mới bắt đầu."},
            5: {"Mã sản phẩm": "SP5", "Tên": "Bàn phím cơ Razer BlackWidow V3", "Giá": 2500000, "Số lượng": 25, "Mô tả": "Bàn phím cơ với đèn RGB, switch Razer Green, lý tưởng cho game thủ."}
        }
# Danh sách rỗng
        # self.sanpham = {}
# Hiển thị danh sách
    def hien_thi_danh_sach(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("----- DANH SÁCH SẢN PHẨM -----")
        if self.sanpham == {}:
            print("Danh sách rỗng")
            input("Nhấn Enter để quay lại menu chính...")
        else:
            for sp in sorted(self.sanpham.values(), key=lambda x:x["Mã sản phẩm"]):
                print(f"Mã sản phẩm: {sp["Mã sản phẩm"]}\nTên: {sp["Tên"]}\nGiá: {sp["Giá"]}\nSố lượng: {sp["Số lượng"]}\nMô tả: {sp["Mô tả"]}")
                print("-"*100)
            input("Nhấn Enter để quay lại menu chính...")
# Thêm sản phẩm
    def them_san_pham(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("----- THÊM SẢN PHẨM -----")
        ma_sp = f"SP{len(self.sanpham) + 1}"
        ten = input("Nhập tên: ").strip()
        gia = input("Nhập giá (VND): ").strip()
        so_luong = input("Nhập số lượng: ").strip()
        mo_ta = input("Nhập mô tả: ").strip()
        self.sanpham[len(self.sanpham) + 1] = {"Mã sản phẩm": ma_sp, "Tên": ten, "Giá": gia, "Số lượng": so_luong, "Mô tả": mo_ta}
        input("Nhấn Enter để quay lại menu chính...")
# Cập nhật sản phẩm
    def cap_nhat_san_pham(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("----- CẬP NHẬT SẢN PHẨM -----")
        ma_sp = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        for sp in self.sanpham.values():
            if sp["Mã sản phẩm"] == ma_sp:
                print("Đã tìm thấy sản phẩm. Bỏ trống (Enter) nếu không muốn cập nhật")
                ma = input(f"Mã sản phẩm cũ ({sp["Mã sản phẩm"]}), nhập mã mới: ").strip().upper() or sp["Mã sản phẩm"]
                ten = input(f"Tên cũ ({sp["Tên"]}), nhập tên mới: ").strip() or sp["Tên"]
                gia = input(f"Giá cũ ({sp["Giá"]}), nhập giá mới: ").strip() or sp["Giá"]
                so_luong = input(f"Số lượng cũ ({sp["Số lượng"]}), nhập số lượng mới: ").strip() or sp["Số lượng"]
                mo_ta = input(f"Mô tả cũ ({sp["Mô tả"]}), nhập mô tả mới: ").strip() or sp["Mô tả"]
                sp.update({"Mã sản phẩm": ma, "Tên": ten, "Giá": gia, "Số lượng": so_luong, "Mô tả": mo_ta})
                input("Nhấn Enter để quay lại menu chính...")
                break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Không tìm thấy sản phẩm có mã giống mã đã nhập")
            input("Nhấn Enter để quay lại menu chính...")
# Xóa sản phẩm
    def xoa_san_pham(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("----- XÓA SẢN PHẨM -----")
        xoa = input("Nhập mã sản phẩm bạn muốn xóa: ").strip().upper()
        for key, sp in self.sanpham.items():
            os.system("cls" if os.name == "nt" else "clear")
            print("----- XÓA SẢN PHẨM -----")
            if sp["Mã sản phẩm"] == xoa:
                while True:
                    hoi = input(f"Bạn có chắc chắn muốn xóa sản phẩm {sp['Mã sản phẩm']}? (Y/N): ").strip().upper()
                    if hoi == "Y":
                        del self.sanpham[key]
                        print("Xóa sản phẩm thành công")
                        input("Nhấn Enter để quay lại menu chính...")
                        break
                    elif hoi == "N":
                        print("Hủy xóa sản phẩm")
                        input("Nhấn Enter để quay lại menu chính...")
                        break
                    else: print("Chức năng không hợp lệ, vui lòng chọn lại")
                break
        else:
            print(f"Không tìm thấy sản phẩm có mã giống mã đã nhập ({xoa})")
            input("Nhấn Enter để quay lại menu chính...")
# Sắp xếp
    def sap_xep_san_pham(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("----- SẮP XẾP SẢN PHẨM -----")
            print("""1. Mã tăng dần
2. Mã giảm dần
3. Tên tăng dần
4. Tên giảm dần
5. Giá tăng dần
6. Giá giảm dần""")
            sap_xep = int(input("Chọn chức năng: "))
            if sap_xep in [1,2,3,4,5,6]:
                if sap_xep == 1: danh_sach = sorted(self.sanpham.values(), key=lambda x: x["Mã sản phẩm"])
                elif sap_xep == 2: danh_sach = sorted(self.sanpham.values(), key=lambda x: x["Mã sản phẩm"], reverse=True)
                elif sap_xep == 3: danh_sach = sorted(self.sanpham.values(), key=lambda x: x["Tên"])
                elif sap_xep == 4: danh_sach = sorted(self.sanpham.values(), key=lambda x: x["Tên"], reverse=True)
                elif sap_xep == 5: danh_sach = sorted(self.sanpham.values(), key=lambda x: x["Giá"])
                elif sap_xep == 6: danh_sach = sorted(self.sanpham.values(), key=lambda x: x["Giá"], reverse=True)
                os.system("cls" if os.name == "nt" else "clear")
                print("----- DANH SÁCH SẢN PHẨM -----")
                for sp in danh_sach:
                    print(f"Mã sản phẩm: {sp["Mã sản phẩm"]}\nTên: {sp["Tên"]}\nGiá: {sp["Giá"]}\nSố lượng: {sp["Số lượng"]}\nMô tả: {sp["Mô tả"]}")
                    print("-"*100)
                input("Nhấn Enter để quay lại menu chính...")
                break
            else:
                print("Chức năng không hợp lệ, vui lòng chọn lại")
                input("Nhấn Enter để chọn lại...")
# Tìm sản phẩm đắt nhất
    def tim_san_pham_dat_nhat(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("----- TÌM SẢN PHẨM ĐẮT NHẤT -----")
        dat_nhat = max(self.sanpham.values(), key=lambda x: x["Giá"])
        print(f"""Mã sản phẩm: {dat_nhat["Mã sản phẩm"]}
Tên: {dat_nhat["Tên"]}
Giá: {dat_nhat["Giá"]}
Số lượng: {dat_nhat["Số lượng"]}
Mô tả: {dat_nhat["Mô tả"]}""")
        input("Nhấn Enter để quay lại menu chính...")
# Menu chính
quanly = QuanLy()
while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""----- CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM -----
1. Xem danh sách
2. Thêm mới
3. Cập nhật
4. Xóa
5. Sắp xếp
6. Tìm sản phẩm có giá đắt nhất
7. Thoát""")
        lua_chon = int(input("Chọn chức năng: ").strip())
        if lua_chon == 1: quanly.hien_thi_danh_sach()         
        elif lua_chon == 2: quanly.them_san_pham()
        elif lua_chon == 3: quanly.cap_nhat_san_pham()      
        elif lua_chon == 4: quanly.xoa_san_pham()
        elif lua_chon == 5: quanly.sap_xep_san_pham()
        elif lua_chon == 6: quanly.tim_san_pham_dat_nhat()
        elif lua_chon == 7:
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")
            input("Nhấn Enter để chọn lại...")