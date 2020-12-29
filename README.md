# ros_greeting_clock
![Alt](https://github.com/kazukiakimoto/ros_greeting_clock/blob/master/image/IMG_6013.JPG)

# 概要
現在時間に合わせて挨拶をしてくれるプログラムです

# 説明
このROSのパッケージはパブリッシャーがdatetimeモジュールから取得した現在時刻のunix時間をパブリッシュし、サブスクライバがその時間に合わせて挨拶をしてくれます。  
 - 5~9時は"おはようございます"
 - 10~18時は"こんにちは"
 - 19~23時は"こんばんは"
 - 0~4時は"こんな時間に何しているんですか？"

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
MIT LICENSE  
https://github.com/kazukiakimoto/ros_greeting_clock/blob/master/LICENSE
