#!/usr/bin/env bash

[ ! -x "$(which python)" ] && {
    echo "python is not installed, please install it."
    exit 1
}

if [ $(id -u) != 0 ]; then
    echo "permission denied, try again using sudo"
    exit 1
fi

pathscript="/opt/scripts" 
pathlink="/usr/local/bin"

echo "========================================"
echo "               install nam              "
echo "========================================"
echo "set default language"
echo "[1] - pt-br"
echo "[2] - en"
echo -n "selected option: "
read option;
echo -e ""

sudo cp -r ../nam $pathscript/ &
rm -rf $pathscript/nam/assets &
rm -rf $pathscript/nam/install.sh &
rm -rf $pathscript/nam/README.md &

if [ ! -e $pathscript ]; then # if directory dont exist
	sudo mkdir $pathscript # create directory
fi
sudo ln -sf $pathscript/nam/nam.py $pathlink/nam & # create link
sudo chmod +x $pathscript/nam/nam.py &
sudo chmod +x $pathlink/nam &

case $option in
    "1")
    echo "brazilian portuguese version installed"
    ;;
    "2")
    cp -r $pathscript/nam/settings/language-br/commands/* $pathscript/nam/commands &
    echo "sorry, english version wasn't released yet"
    echo "brazilian portuguese version installed"
    ;;
    *)
    echo "error: type only 1 or 2"
    exit 1
esac

echo "the program was installed in: $pathscript"