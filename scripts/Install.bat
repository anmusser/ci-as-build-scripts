@echo off
C:/BrAutomation/PVI/V4.5/PVI/Tools/PVITransfer/PVITransfer.exe -silent C:/BuildEngine/Scripts/OfflineInstall.pil C:/BuildEngine/Scripts/PVILog.txt
echo PVI error number is %errorlevel%
if errorlevel = 28324 goto cant_find_module
if errorlevel = 28321 goto no_file_name_specified
if errorlevel = 28320 goto file_not_found
if errorlevel = 4808 goto connection_failed
if errorlevel = 0 goto success
:file_not_found
echo ERROR: File not found
goto end
:no_file_name_specified
echo ERROR: No file name specified
goto end
:cant_find_module
echo ERROR Module not found
goto end
:connection_failed
echo PVI error: No connection available to the PLC
goto end
:success
echo Program executed successfully
:end