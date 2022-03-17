# WhatsApp-Eid-Greeting-Bot

Python script for sending personalized Eid greetings (and other messages) through Whatsapp via a bot.


## Gather Contacts

1) Open [Google Contacts](https://contacts.google.com "G contacts") webpage and export your contacts.
2) Ensure to keep this csv as "google.csv" and keep it in the same folder as the `send_greetings.py` file.
3) Caveat: Unlike the previous version, *filter_contacts.py* now passes all contacts as arguments **en masse**. Therefore any name you want to change or any contact you don't want to send the message to: amend the `google.csv` file beforehand (change in Given name field, delete any contacts you don't want to message etc). This has been done so that the user doesn't have to provide confirmation at each contact name because this could be tedious for 150+ contacts. 

## Install libraries

1) Selenium : `pip install selenium `
2) Pandas : `pip install pandas`

## Firefox Driver

1) Install the latest version of Firefox Driver (geckodriver): https://github.com/mozilla/geckodriver/releases
2) Create a directory named `C:\webdrivers` on Windows or `./webdrivers` on Linux

3)
    ### On Windows

    - right click on the Windows Start menu button --> go to `System` --> `Advanced System Settings` --> `Environment Variables` --> Click on `Path` in `System Variables` --> then click `Edit` button. Click `New` and paste `C:\Webdrivers`.

    - Here is a video explanation of the same process: https://www.youtube.com/watch?v=dz59GsdvUF8

4)
    ### On Linux

    - set up the PATH using:

        > $ export PATH=$PATH:"$HOME/webdrivers"

        > $ source ~/.bashrc

## Running the code

`python send_greetings.py`
