import random

_PATH = 'D:/GiangKhaiVinh/LapTrinhPython-Teky/AiLaTrieuPhu'

BO_CAU_HOI_FILE_NAME = 'BoCauHoi.txt'
CAU_TRA_LOI_FILE_NAME = 'CauTraLoi.txt'
GIAI_THUONG_FILE_NAME = 'GiaiThuong.txt'

BO_CAU_HOI = _PATH + '/' + BO_CAU_HOI_FILE_NAME
CAU_TRA_LOI = _PATH + '/' + CAU_TRA_LOI_FILE_NAME
GIAI_THUONG = _PATH + '/' + GIAI_THUONG_FILE_NAME

with open(BO_CAU_HOI, 'r', encoding='utf-8') as f:
    BO_CAU_HOI_LIST = f.readlines()

with open(CAU_TRA_LOI, 'r', encoding='utf-8') as f:
    CAU_TRA_LOI_LIST = f.readlines()

with open(GIAI_THUONG, 'r', encoding='utf-8') as f:
    GIAI_THUONG_LIST = f.readlines()

CAU_TRA_LOI_LIST_ADJUST = []
for i in CAU_TRA_LOI_LIST:
    CAU_TRA_LOI_LIST_ADJUST.append(i.strip())

GIAI_THUONG_LIST_ADJUST = []
for j in GIAI_THUONG_LIST:
    GIAI_THUONG_LIST_ADJUST.append(j.strip())

CAU_HOI_DA_RA = []
SO_THU_TU = 0
QUYEN_TRO_GIUP = [1, 2]

for i in range(5):
    print("Câu Hỏi Thứ {}".format(SO_THU_TU + 1))
    VI_TRI_CAU_HOI = random.randint(1, 18)

    while VI_TRI_CAU_HOI in CAU_HOI_DA_RA:
        VI_TRI_CAU_HOI = random.randint(1, 18)

    print(BO_CAU_HOI_LIST[VI_TRI_CAU_HOI])
    
    # Hỏi người chơi có muốn dùng quyền trợ giúp không
    if QUYEN_TRO_GIUP:
        CHON_TRO_GIUP = input("Bạn Có Muốn Chọn Quyền Trợ Giúp Không? (Y/N): ")
        if CHON_TRO_GIUP.lower() == 'y':
            print("Các Quyền Trợ Giúp Có Sẵn: ")
            if 1 in QUYEN_TRO_GIUP:
                print("1. 50:50")
            if 2 in QUYEN_TRO_GIUP:
                print("2. Gọi Người Thân")
            
            TRO_GIUP = int(input("Chọn Quyền Trợ Giúp (1 hoặc 2): "))
            
            if TRO_GIUP == 1 and 1 in QUYEN_TRO_GIUP:
                # Quyền trợ giúp số 1: 50:50
                print("Bạn Đã Chọn Quyền Trợ Giúp Số 1")
                DAP_AN_1 = CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]  # Đáp án đúng
                DAP_AN_2 = chr(random.randint(65, 68))  # Đáp án ngẫu nhiên

                while DAP_AN_2.lower() == DAP_AN_1.lower():
                    DAP_AN_2 = chr(random.randint(65, 68))

                DAP_AN_LIST = [DAP_AN_1, DAP_AN_2]
                random.shuffle(DAP_AN_LIST)  # Trộn thứ tự 2 đáp án

                print('{} _____ {}'.format(DAP_AN_LIST[0], DAP_AN_LIST[1]))
                QUYEN_TRO_GIUP.remove(1)
            
            elif TRO_GIUP == 2 and 2 in QUYEN_TRO_GIUP:
                # Quyền trợ giúp số 2: Gọi người thân
                print("Bạn Đã Chọn Quyền Trợ Giúp Số 2: Gọi Người Thân")
                
                # Xác suất người đúng là 80%
                XAC_SUAT_DUNG = 0.8
                GOI_Y_DUNG = random.random() < XAC_SUAT_DUNG

                if GOI_Y_DUNG:
                    GOI_Y = CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]  # Gợi ý đúng
                else:
                    GOI_Y = chr(random.randint(65, 68))  # Gợi ý sai
                    while GOI_Y.lower() == CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI].lower():
                        GOI_Y = chr(random.randint(65, 68))

                print("Người Thân Của Bạn Nói: Tôi Nghĩ Đáp Án Đúng Là '{}'".format(GOI_Y))
                QUYEN_TRO_GIUP.remove(2)
    
    # Người chơi trả lời câu hỏi
    USER_ANSWER = input("Nhập Vào Câu Trả Lời Của Bạn: ")
    
    if USER_ANSWER.lower() == (CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]).lower():
        print("""
    Bạn Đã Trả Lời Đúng
    Bạn Đang Có {} Đồng
                """.format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))

        if SO_THU_TU == 4:
            print("Bạn Đã Hoàn Thành Trò Chơi Và Bạn Nhận Được {} Đồng".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))
        else:
            SO_THU_TU += 1
            CHOI_TIEP = input("Bạn Có Muốn Tiếp Tục? (Y/N): ")
            if CHOI_TIEP.lower() == 'y':
                CAU_HOI_DA_RA.append(VI_TRI_CAU_HOI)
                continue
            else:
                print("Bạn Đã Hoàn Thành Trò Chơi Và Bạn Nhận Được {} Đồng".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU - 1]))
                break
    else:
        if SO_THU_TU == 0:
            print("""
        Bạn Đã Trả Lời Sai
        Vì Sai Câu Hỏi Đầu Tiên, Bạn Không Nhận Được Gì Cả
                  """)
            break
        else:
            print("""
        Bạn Đã Trả Lời Sai
        Xin Chúc Mừng Bạn Đã Trắng Tay
                    """)
            break