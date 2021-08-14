#!/usr/bin/env bash

pathscript="/opt/scripts" 
pathlink="/usr/local/bin"

check() {
[ ! -x "$(which python3)" ] && {
    echo "python is not installed, please install it."
    exit 1
}

if [ $(id -u) != 0 ]; then
    echo "permission denied, try again using sudo"
    exit 1
fi
}

ask() {
echo ""
echo "========================================="
echo "               install nam               "
echo "========================================="
echo "set commands default language"
echo "[1] - br"
echo "[2] - en"
echo -n "selected option: "
read option;
echo -e ""
return "$option"
}

banner() {
echo "         _  _   _   __  __   "
echo "        | \| | /_\ |  \/  |  "
echo "        |    |/ _ \| |\/| |  "
echo "        |_|\_/_/ \_\_|  |_|  "
echo ""
}

prepare() {
if [ ! -e $pathscript ]; then sudo mkdir $pathscript; fi
if [ ! -e $pathscript/nam ]; then return; fi
sudo rm -rf $pathscript/nam/commands/*
}

install(){
sudo cp -r ../nam $pathscript/
}

link(){
sudo ln -sf $pathscript/nam/nam.py $pathlink/nam 
sudo chmod +x $pathscript/nam/nam.py 
sudo chmod +x $pathlink/nam
}

language(){
case $1 in
    "1")
    echo -e "commands: brazilian portuguese\n"
    ;;
    "2")
    sudo cp -r $pathscript/nam/en/commands/* $pathscript/nam/commands 
    echo -e "commands: english\n"
    ;;
    *)
    echo -e "commands: brazilian portuguese\n"
esac
}

main(){
check
ask
option=$?
banner
echo -ne '>>>>>>>>>                          [20%]\r'
sleep 0.5
echo -ne '>>>>>>>>>>>>>>>>                   [40%]\r'
prepare
sleep 0.5
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>            [60%]\r'
install
sleep 0.5
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      [80%]\r'
link
sleep 0.5
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[100%]\r'
echo -ne '\n'
echo -e "\nnam was installed in: $pathscript"
language $option
}

main