@echo off
Title 修改DNS
Color 1

%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit

:step
echo .
echo ++++++++++++++++++++++++++++++++
echo 1.静态地址DNS
echo 2.公司NAS
echo 3.自动获取公司DNS
echo 4.显示ip地址
echo 5.开启WLAN
echo 6.关闭WLAN
echo ++++++++++++++++++++++++++++++++
echo .
set /p n=请选择:
if "%n%"=="" cls&goto :step
if  "%n%"=="1" call :1
if  "%n%"=="2" call :2
if  "%n%"=="3" call :3
if  "%n%"=="4" call :4
if  "%n%"=="5" call :5
if  "%n%"=="6" call :6
if /i "%n%"=="n" exit
pause
goto :eof

:1
echo 静态地址DNS119.29.29.29
netsh interface ip set dns "以太网" static 119.29.29.29
netsh interface ipv4 show config name="以太网"
goto step

:2
echo 公司NAS10.48.6.41
netsh interface ip set dns "以太网" static 10.48.6.41
netsh interface ipv4 show config name="以太网"
goto step

:3
echo 自动获取公司DNS
netsh interface ip set dns "以太网" dhcp
netsh interface ipv4 show config name="以太网"
goto step

:4
echo 显示ip地址
netsh interface ipv4 show config name="以太网"
goto step

:5
echo 开启WLAN
netsh interface set interface "WLAN" enabled
goto step

:6
echo 关闭WLAN
netsh interface set interface "WLAN" disabled
goto step
