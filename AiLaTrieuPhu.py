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
    USER_ANSWER = input("Nhập Vào Câu Trả Lời Của Bạn: ")
    
    if USER_ANSWER.lower() == (CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]).lower():
        print("""
    Bạn Đã Trả Lời Đúng
    Bạn Đang Có {} Đồng
                """.format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))

        if SO_THU_TU == 4:
            print("Bạn Đã Hoàn Thành Trò Chơi Và Bạn Sẽ Nhận Được {} Đồng".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))
        else:
            SO_THU_TU += 1
            CHOI_TIEP = input("Bạn Có Muốn Tiếp Tục? (Y/N): ")
            if CHOI_TIEP.lower() == 'y':
                CAU_HOI_DA_RA.append(VI_TRI_CAU_HOI)
                continue
            else:
                print("Bạn Đã Hoàn Thành Trò Chơi Và Bạn Sẽ Nhận Được {} Đồng".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU - 1]))
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
                    """.format(GIAI_THUONG_LIST_ADJUST[0]))
            break

# Quyền trợ giúp
if QUYEN_TRO_GIUP == 1:
    print("Bạn Đã Chọn Quyền Trợ Giúp Số 1")
    DAP_AN_1 = CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]
    DAP_AN_2 = chr(random.randint(65, 68))
    while DAP_AN_2.lower() == DAP_AN_1.lower():
        DAP_AN_2 = chr(random.randint(65, 68))

    DAP_AN_LIST = [DAP_AN_1, DAP_AN_2]
    DAP_AN_1_display = random.randint(0, 1)
    DAP_AN_2_display = 1 - DAP_AN_1_display
    print('{} --- {}'.format(DAP_AN_LIST[DAP_AN_1_display], DAP_AN_LIST[DAP_AN_2_display]))
    QUYEN_TRO_GIUP.remove(1)