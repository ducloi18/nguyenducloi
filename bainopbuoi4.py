# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:33:51 2024

@author: NGUYEN DUC LOI
Bài1:Khoảng cách 
distance = float(input(" Nhập độ dài đoạn đường đến trường (m): "))
if distance > 1200:
    print("Đường đến trường quá xa. Thôi. Đi xe máy đi!")
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi, đi xe đạp!")
else:
    print("Không xác định được xa-gần.")
    
Bài 2: Tính GPA
GPA = float(input(" Nhập điểm trung bình: "))
if GPA < 3.5:
    print(" Học lực Kém.")
elif GPA >= 3.5 and GPA < 5.0:
    print(" Học lực Yếu.")
elif GPA >= 5.0 and GPA < 7.0:
    print(" Học lực Trung Bình.")
elif GPA >= 7.0 and GPA < 8.0:
    print(" Học lực Khá.")
elif GPA >= 8.0 and GPA < 9.0:
    print(" Học lực giỏi.")
else:
    print(" Học lực Xuất sắc.")
    
Bài 3: Chứng minh 3 cạnh tam giác
a = float(input(" a= "))
b = float(input(" b= "))
c = float(input(" c= "))
if a + b > c and a + c > b and b + c > a:
    print(" a,b,c là 3 cạnh của một tam giác")
else:
    print(" a,b,c không là 3 cạnh của một tam giác")
    
Bài 4: Tam giác đặc biệt
a = float(input(" a= "))
b = float(input(" b= "))
c = float(input(" c= "))
if (a + b > c and a + c > b and b + c > a):
    if a == b == c:
        print(" tam giác đều ")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print(" tam giác vuông")
    elif a == b or b == c or a == c:
        print(" tam giác cân")
    else:
        print(" đây là tam giác")
else:
    print(" đây không là tam giác")
    
Bài 5: Phương trình bậc nhất( cách 1)
a = float(input(" nhập số a: "))
b = float(input(" nhập số b: "))
if (a == 0):
    if b == 0:
        print("Pt có vô số nghiệm")
    else:
        print("pt vô nghiệm")
else:
    print("pt có nghiệm duy nhất x = ", -b/a)
    
Phương trình bậc nhất (cách 2)
a = float(input(" nhập số a: "))
b = float(input(" nhập số b: "))
if (a == 0):
    if b == 0:
        print("Pt có vô số nghiệm")
    else:
        print("pt vô nghiệm")
else:
    print("pt có nghiệm duy nhất x = ", -b/a)
    
Bài 6: Phương trình bậc 2
import math
a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
denta = b*b - (4*a*c)
if a == 0:
    print(" pt có 1 nghiệm duy nhất x=", -b/c)
elif a != 0 and denta < 0:
    print(" pt vô nghiệm")
elif a != 0 and denta == 0:
    print("pt có nghiệm kép x1=x2 = ", -b/(2*a))
elif a != 0 and b*b-(4*a*c) > 0:
    print("pt có 2 nghiệm pb x1 = ", (-b + math.sqrt(denta))/(2*a))
    print("pt có 2 nghiệm pb x2 = ", (-b - math.sqrt(denta))/(2*a))

Bài 7: Giá tiền taxi
distance = float(input(" nhập số quãng đường taxi đi (km): "))
money = 3*13000 + 5 * 12000 + (distance - 8)*10000
if distance > 0 and distance <= 1:
    print("số tiền phải trả là 20000")
elif distance > 1 and distance < 4:
    print("số tiền phải trả = ", distance*13000)
elif distance >= 4 and distance <= 8:
    print(" số tiền phải trả = ", 3*13000 + (distance - 3)*12000)
else:
    print(" số tiền phải trả = ", money)
    if money > 100:
        print(" số tiền phải trả sau cùng = ", money - (money*0.08))

Bài 8: Kéo búa bao
import random
choices = ["kéo", "búa", "bao"]
kq_người_chơi = input("Nhập kết quả người chơi: ")
if kq_người_chơi not in ["kéo", "búa", "bao"]:
    print("kết quả không hợp lệ, nhập lại")
kq_may = random.choice(choices)
print(f"kết quả của máy {kq_may}")
if kq_người_chơi == kq_may:
    print("Hòa!")
elif (kq_người_chơi == "búa" and kq_may == "kéo") or \
     (kq_người_chơi == "kéo" and kq_may == "bao") or \
     (kq_người_chơi == "bao" and kq_may == "búa"):
    print(" Bạn thắng")
else:
    print("Bạn thua")
    
"""

