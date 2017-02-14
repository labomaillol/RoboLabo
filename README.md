# RoboLabo

Repo regroupant tous les scripts du rover FPV créé à partir d'une vieille voiture télécommandée

Lignes de commandes à lancer après l'installation de Raspbian Pixel :

sudo apt-get install subversion libv4l-dev libjpeg8-dev imagemagick gstreamer1.0 guvcview bison libglib2.0-dev flex arduino 
sudo apt-get install gstreamer1.0-packagekit gstreamer1.0-tools gstreamer1.0-omx gstreamer1.0-plugins-ugly gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-bad gstreamer1.0-libav lighttpd php5 php5-cli imagemagick php5-imagick php5-gd xplanet unclutter mingetty xutils-dev libudev-dev libxwiimote-dev libxwiimote2 x11proto-core-dev xorg-server-source

sudo apt-get install pkg-config make xutils-dev libtool xserver-xorg-dev libx11-dev libxi-dev libxrandr-dev libxinerama-dev libudev-dev libncurses5-dev gtk-doc-tools

sudo pip3 evdev
 
cd ~/Downloads/
mkdir gst
cd gst
wget https://gstreamer.freedesktop.org/src/gst-rtsp-server/gst-rtsp-server-1.4.4.tar.xz
tar -xf gst-rtsp-server-1.4.4.tar.xz
cd gst-rtsp-server-1.4.4
sudo ./autogen.sh

