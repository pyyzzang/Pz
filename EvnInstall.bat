set Python_Exe="C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Python.exe"
set PIP_Exe="C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pip.exe"

%Python_Exe% -m pip install --upgrade pip

%PIP_Exe% install -e django

%PIP_Exe% install --upgrade django

%PIP_Exe% install pywin32

%PIP_Exe% install pyautogui