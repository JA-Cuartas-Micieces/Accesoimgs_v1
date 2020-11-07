@echo
call %userprofile%\Anaconda3\Scripts\activate.bat
%userprofile%\Anaconda3\python.exe Accesoimgs.py
IF %ERRORLEVEL% NEQ 0 (start msg.vbs)
