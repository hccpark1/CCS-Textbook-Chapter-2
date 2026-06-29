import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.font_manager as fm
import numpy as np 
from scipy.interpolate import interp1d
# import plotly.express as px     # 추세선 그리기

# 한글 깨짐 방지
font_path = 'C:/Windows/Fonts/HANBatang.ttf'                # 나눔글꼴 경로 설정
font_name = fm.FontProperties(fname=font_path).get_name()   # 폰트 이름 가져오기
plt.rc('font', family=font_name)                            # 폰트 설정


# Data 입력
x = np.array([650,700,700,1020])
y = np.array([350,340,390,530])

# 추세선을 위한 계산 - 1차원의 polynomial(다항식)을 계산하기 위한 코드입니다.
z = np.polyfit(x, y, 1) # (X,Y,차원) 정의
p = np.poly1d(z) # 1차원 다항식에 대한 연산을 캡슐화

# 그래프 그리기
plt.figure(figsize=(6, 5))
plt.plot(x,y, "bo", label='수액기 체적(cc)')      #산점도를 뜻할 때 'o'라고 합니다.
plt.plot(x,p(x),"r--", label='y=x')
# pylab.plot(x,y, "o", label='수액기 체적(cc)')      #산점도를 뜻할 때 'o'라고 합니다.
# pylab.plot(x,p(x),"r--", label='y=x')
plt.xlabel('냉매 충진량(g)', fontsize=12)
plt.ylabel('수액기 체적(cc)', fontsize=12)

plt.grid()
plt.xlim(300, 1100)
plt.ylim(100, 600)
plt.yticks(np.arange(200, 600, 100))
plt.text(910, 280, "y=%.6fx+(%.6f)"%(z[0],z[1])) # (4.8, 6)위치에 추세선 식 표현
plt.legend()
plt.savefig('D:/냉매 충진량 vs 수액기 체적 Graph.png')
plt.show()
# 방정식 계산
print( "y=%.6fx+(%.6f)"%(z[0],z[1]))

