echo "set default language"
echo "[1] - en"
echo "[2] - pt-br"

sudo cp ../nam /usr/local/bin/ &
sudo rm -rf /usr/local/bin/nam/README.md &
sudo rm -rf /usr/local/bin/nam/install.sh &

echo "the program was installed: /usr/local/bin/"