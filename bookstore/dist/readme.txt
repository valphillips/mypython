To create executable:

>pip install pyinstaller
>cd to the directory that has your program files
>pyinstaller --onefile --windowed Bookstore_FrontEnd.py
(This will create the executable file in a directory ./dist)

If you want to provide your user with the database, will need to provide them with the executable file and the database
otherwise they will start with a blank db
