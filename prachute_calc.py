#made by MineKura(Kaepi2022 : https://www.github.com/kaepi2022)
import math

#重力加速度
Gravity_E = 9.80665             #重力加速度(地球)
Gravity_M = 9.80665 / 6.0       #重力加速度(月の場合)

#Cの参考値（半球型ビニール）
#参考リンク :  https://www.notion.so/23be4605288c80c2aa4ecf05497d69dd

Cd_MAX = (1.5 + 1.75)   / 2   #完全開放時の平均を取得
Cd_REAL = (1.3+1.5)     / 2   #多少のシワありの現実的な数値
Cd_FAILD = (1.0 + 1.2)  / 2   #展開不良ややや多いシワの場合

#▼定数系
C = (Cd_MAX + Cd_REAL + Cd_FAILD) / 2      #抗力係数（無次元）
R = 287.0                                  #空気の気体定数J(kg*k)
K = 273.15                                 #絶対温度K
P = 101325                                 #1気圧Pa

#絶対温度Kに変換する関数
def get_kelvin(T_C):
    return T_C + K

#空気密度を計算する関数
def air_density(Kelvin):       
    return P / (R * Kelvin)

print("はじめに、空気密度（kg/m³）を求めていきます。\n")
tempera = float(input("実行場所の温度 °C >> "))
Ro      = air_density(get_kelvin(tempera))      #空気密度ρ


print("求めたいものをモード(番号)から選択してください。\n ")
print("1.空気抵抗(抗力) N \n")
print("2.パラシュートの面積 m²/cm²/mm² \n")
mode_num = int(input("番号 (1か2) >> "))

if(mode_num == 1):

    print("空気抵抗(抗力,N)の計算を行います。\n")
    velocity = float(input("物体の落下速度 v >>"))     
    para_A   = float(input("パラシュートの面積 m² >>"))
    ans = (1/2) * Ro * C * para_A * math.pow(velocity,2)
    print(f"-^-^-計算結果-^-^-\n 空気密度ρ ={Ro:.5}kg/m³ \n 空気抵抗Fd = {ans:.5}N")


elif(mode_num == 2):

    print("パラシュートの面積の計算を行います。\n")
    air_res = int(input("空気抵抗(抗力) N >> "))
    velocity = float(input("物体の落下速度 v >>"))
    ans = (2.0 * air_res) / (Ro * C * math.pow(velocity,2))
    print(f"-^-^-計算結果-^-^-\n 空気密度ρ ={Ro:.5}kg/m³ \n パラシュートの面積\n{ans:.5}m²\n{ans*math.pow(10,-2):.5}cm²\n{ans*math.pow(10,-3):.5}mm²\n")

else:
    print("指定された番号は無効です。")
