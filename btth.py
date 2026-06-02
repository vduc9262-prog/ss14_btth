
grade_book = [
    {'stt': 1,"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {'stt': 2,"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book):
    print('--- BẢNG ĐIỂM HỌC SINH ---')
    print('Mã SV | Tên Học Sinh        | Điểm Toán | Điểm Anh | ĐTB')
    print('-' * 70)
    for p in (book):
            tb = (p['info'][0] + p['info'][1]) / 2
            print(f'{p['id']:<5} | {p['name']:<18}  | {p['info'][0]:<9} | {p["info"][1]:<8} | {tb} '  )
            print('-' * 70)

def add_student(book):

    while True:
        input_id = input("Nhập mã sinh viên:")

        check = False

        for student in book:
            if input_id == student['id']:
                check = True
                print('Mã sinh viên đã tồn tại')
                break

        if not check:
            break
    
    input_name = input('Nhập tên sinh viên: ')
    input_math = int(input('Nhập điểm toán: '))
    input_eng = int(input('Nhập điểm anh: '))

    book.append({
        "stt": book[len(book) - 1]['stt'] + 1,
        "id": input_id,
        "name": input_name,
        "info": (input_math, input_eng)
    })
    print('theem thanh cong !')

def update_student(book):
    student_id = input('nhập mã sinh viên cần cập nhật: ').upper()

   
    for po in book:

        if student_id == po["id"]:
            print(f'cập nhật mã {po["id"]} ')

            math_new = int(input('nhập điểm toán cần cập nhật: '))
            english_new = int(input('nhập điểm anh cần cập nhật: '))
            po["info"] = (math_new,english_new)

            print(f'cập nhật thành công sinh viên mã {po["id"]} ')
            break

    else:   
        print("ko tìm thấy mã sinh viên !")


def delete_student(book):
    delete_id = input("nhập mã sinh viên cần xóa: ").upper()

    for de in book:
        if delete_id == de["id"]:
            book.remove(de)
            print(f'đã xóa mã sinh viên {de["id"]}')
            break


    else:
        print('ko tìm thấy mã sinh viên cần xóa !')

while True:
    choice = int(input('''=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình

==============================
Chọn chức năng (1-5): '''))

    match choice:
        case 1: 
            display_grades(grade_book)
        case 2:
            add_student(grade_book)
        case 3:
            update_student(grade_book)
        case 4:
            delete_student(grade_book)
        case 5:
            print('Thoát chương trình')
            break

        case _:
            print('Lựa chọn không hợp lệ')