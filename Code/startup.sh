DAEMONPATH = "/home/pi/RASPY-PRO/ExecDaemon.py"

echo "starting legopi"
echo "---------------"
echo "loading spi drivers"
/sbin/modprobe spi-bcm2708
echo "---------------"
echo "starting execdaemon"
/usr/bin/python $DAEMONPATH &
echo "---------------"
echo "finished startup script"

