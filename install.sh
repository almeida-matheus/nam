#!/usr/bin/env bash

[ ! -x "$(which python)" ] && {
    echo "python is not installed, please install it."
    exit 1
}

echo "*********************"
echo "     install nam     "
echo "*********************"
echo "set default language"
echo "[1] - pt-br"
echo "[2] - en"
echo -n "selected option: "
read option;
echo -e "\n"

sudo cp ../nam /usr/local/bin/ &
sudo rm -rf /usr/local/bin/nam/.git &
sudo rm -rf /usr/local/bin/nam/assets &
sudo rm -rf /usr/local/bin/nam/install.sh &
sudo rm -rf /usr/local/bin/nam/README.md &

case $option in
  "1")
  sudo cp /usr/local/bin/nam/settings/language-br/commands/* /usr/local/bin/nam/commands &
  ;;
  "2")
  sudo cp /usr/local/bin/nam/settings/language-br/commands/* /usr/local/bin/nam/commands &
  echo "sorry the english version wasn't released yet"
  echo "brazilian portuguese version installed"
  ;;
  "*")
  exit 1
esac

echo "the program was installed in: /usr/local/bin/"