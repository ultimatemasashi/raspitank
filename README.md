# raspitank
ラズパイをサーボモーターで動かします
USBカメラをRASPITANKに実装。　pygamesで遠隔制御します。
３６０°回転サーボモーターが２台必要となります。

![RASPITANK](https://github.com/ultimatemasashi/raspitank/blob/main/122566478_270925330891548_6412678789847878808_n.jpg)
 サーボモータードライバーPCA9685を使用するため、インストールが必要です。

sudo pip install adafruit-pca9685

インストールできればI2Cの設定をします。

sudo raspi-config　

回路を構成し通信を確認します。

sudo i2cdetect -y 1


カメラ画像はOPENCVを使っています。OPENCVで作成した画像をpygameでの背景にしています。
d.jpgファイルと定義しています。

的のファイルはtarget.jpg 音はbig-explosion1.wavを使用しています。
pythonファイルと同じディレクトリに配置してください。


キーボードの↑で前進、↓で後退
←→でそれぞれ旋回します。

クリックすると爆発音がなります。
