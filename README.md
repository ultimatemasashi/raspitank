# raspitank
ラズパイをサーボモーターで動かします
カメラをRASPITANKに実装。　pygamesで遠隔制御します。

PCA9685 16チャンネル 12-ビット PWM Servo モーター ドライバーを使用するため、インストールが必要です。

sudo pip install adafruit-pca9685

インストールできればI2Cの設定をします。

sudo raspi-config　

回路を構成し通信を確認します。

sudo i2cdetect -y 1


カメラ画像はOPENCVを使っています。OPENCVで作成した画像をpygameでの背景にしています。

