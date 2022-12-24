# whatsapp-bulk-sender-with-attachments

Whatsapp Bulk Messenger automates sending of messages with attachments via Whatsapp Web. The tool can you used to send whatsapp message in bulk. Program uses runs through a list of numbers provided in numbers.txt and then tries to send a prediefined (but templated) message to each number in the list. It can also read other columns from the number csv to populate template specific words and then send out a personalized message to the number


Please reach out to me on [![Linkedin Badge](https://img.shields.io/badge/-MAH-blue?style=flat&logo=Linkedin&logoColor=white)](https://linkedin.com/in/mohammed-althaf-h) for more enquiry.

# Requirements

*  Python >= 3.6
*  Chrome headless is installed by the program automatically

# Setup

1. Install python - >=v3.6
2. Run `pip install -r requirements.txt`

# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Enter the list of numbers line-separated in `numbers.txt` file.
3. Add path of the folder where attachment are stored in line 89 `filen=(f"Give the path name here/{filename}")#path name where file is stored Eg: "C:/Users/Desktop/bot/`
4. Run `python automator.py`.
5. Enter the file name when prompted
6. Once the program starts, you'll see the message in message.txt and count of numbers in the numbers.txt file.
7. After a while, Chrome should pop-up and open web.whatsapp.com.
8. Scan the QR code to login into whatsapp.
10. Sit back and relax!

Source code credits @anirudhbagri.
