# バーンズリーのシダをmatplotlibで描画する
# 描画の様子アニメーションで確認することができる

# 9/13 一旦、画像モードで描画を成功させる

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

x_max=5
x_min=-5
y_max=10
y_min=0
pixel=1000 #画素数


# 描画用データ
data=np.zeros((pixel,pixel))


# 画像モード or アニメーションモードを選択ss
mode=input('mode: 0(image) 1(animation)')

fig,ax=plt.subplots()
ax.set_xlim(x_min,x_max)
ax.set_ylim(y_min,y_max)
custom_cmap=ListedColormap(['white','green'])
if mode=='0':
    # 画像モード
    # fig,ax=plt.subplots()
    # ax.set_xlim(x_min,x_max)
    # ax.set_ylim(y_min,y_max)
    print('image mode')
    pass
elif mode=='1':
    fig,ax=plt.subplots()
    ax.set_xlim(x_min,x_max)
    ax.set_ylim(y_min,y_max)
    # アニメーションモード
    print('animation mode')
    ims=[]



[x,y]=[0.0,0.0]
for i in range(10000):
    rand=np.random.rand()
    if rand<0.01:
        [[a,b],[c,d]]=[[0.,0.],[0.,0.16]]
        [e,f]=[0.,0.]
    elif rand<0.86:
        [[a,b],[c,d]]=[[0.85,0.04],[-0.04,0.85]]
        [e,f]=[0.,1.6]
    elif rand<0.93:
        [[a,b],[c,d]]=[[0.2,-0.26],[0.23,0.22]]
        [e,f]=[0.,1.6]
    else:
        [[a,b],[c,d]]=[[-0.15,0.28],[0.26,0.24]]
        [e,f]=[0.,0.44]
    
    [x,y]=[a*x+b*y+e,c*x+d*y+f]
    
    X=min(pixel-1,int(((x-x_min)/(x_max-x_min))*pixel))
    Y=-min(pixel-1,int(((y-y_min)/(y_max-y_min))*pixel))
    data[Y][X]=1

    if mode=='0':
        # print("画像モード")
        pass
    elif mode=='1':
        print(f"frame{i+1} is OK")
        im=ax.imshow(data,animated=True,cmap='Greens')
        ims.append([im])

# ax.set_xlim=(x_min,x_max)
# ax.set_ylim=(y_min,y_max)
# ani=animation.ArtistAnimation(fig,ims,interval=100)
# plt.show()
if mode=='0':
    print("画像モードの最終")
    ax.imshow(data, cmap=custom_cmap, extent=(x_min,x_max,y_min,y_max))
    ax.grid(False)  # グリッド線を非表示
    plt.show()
elif mode=='1':
    print("アニメーションモードの処理を記述")
    # ani=animation.ArtistAnimation(fig,ims,interval=100)
    # plt.show()
