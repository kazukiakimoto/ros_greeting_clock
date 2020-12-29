# ros_greeting_clock

# 概要
時間に合わせて挨拶をしてくれるプログラムです

# 説明
このROSのパッケージはパブリッシャーが時間をカウントし、サブスクライバがその時間に合わせて挨拶をしてくれます。

# デモ
URL:

# スペック
- PC:Raspberry Pi 3 Model B  
- OS:Ubuntu 20.04.1 LTS

# インストール
~~~　　
$ cd ~/catkin_ws/src
$ git clone https://github.com/kazukiakimoto/ros_greeting_clock/blob/master/README.md　
$ cd ../ && catkin_make
~~~

# 使い方
~~~  
一つ目の端末で
$ roscore
二つ目の端末で
$ rosrun ros_greeting_clock count.py
三つ目の端末で
$ rosrun ros_greeting_clock aisatu.py
~~~

# ライセンス
