# FakeMail 📨

![TextPro me_166c9d2163300e (1)](https://github.com/user-attachments/assets/0bac1622-7077-4f9e-96b6-bd0b58432ee3)

**FakeMail** is a Python program designed to generate random and fake emails using various methods. It offers a simple and intuitive menu for users to create emails from different sources, check email validity, and more.

## 🚀 Features
- **Create Email from Names**: Generate emails using real names.
- **Create Email from Random String**: Generate emails using completely random strings.
- **Create Email from RandomUser**: Create emails based on random user data.
- **Create Email from Mimesis**: Utilize the Mimesis module to create realistic fake emails.
- **Create Email from Faker**: Leverage the Faker module for generating credible emails.
- **Valid Email Checker**: Validate a list of emails to determine which are live and which are dead.

## 📖 How to Use
1. **Clone the Repository:**
    ```
    git clone https://github.com/RozhakXD/FakeMail.git
    cd FakeMail
    ```
2. **Install the Required Modules:**
    ```
    pip install -r requirements.txt
    ```
3. **Run the Program:**
    ```
    python Run.py
    ```

## ⚙️ Requirements
- Python 3.x
- Modules: `mimesis`, `faker`, `rich`, `randomuser`, and others listed in `requirements.txt`

## 📬 Support
If you find this project helpful, consider supporting me through the following platforms:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## 🛠️ Troubleshooting
If you encounter issues while using the FakeMail program, there are a few things you can check. First, make sure the domain you input is in the correct format, such as `@gmail.com`. An incorrect format could cause the program to exit or display an error. If the program exits when entering a small number of emails, ensure you input at least 100 emails for the program to function properly.

When using the email checker, verify that the file name and path are correct and that the file exists in the specified directory. If the file provided for the email checker is empty, use a different file that contains valid email entries. If the email validation process fails or takes too long, check your internet connection and ensure the service is working correctly. You may also try validating with a different email provider if issues persist.

## 📸 Screenshot
![FunPic_20240824](https://github.com/user-attachments/assets/71b493a3-0f36-4122-b96b-3057acc9cd2f)

## 📝 Notes
- **Email Quantity**: It's recommended to generate more than 100 emails for optimal results.
- **Error Handling**: If an error occurs, check the response log for more details.
- **File Validity Check**: Make sure the file provided for the email checker contains a valid email list.
- **Domain Input**: Ensure the domain format is correct (e.g., @gmail.com).

## ⚠️ Warning
Please use this tool responsibly. Generating fake emails for malicious purposes or spamming is not encouraged and may violate terms of service of various platforms. Ensure you have the right to use any domain names and email addresses generated. Misuse of this tool could result in legal consequences.

## 📜 License
This project is licensed under the GNU General Public License. See the [LICENSE](https://github.com/RozhakXD/FakeMail?tab=GPL-3.0-1-ov-file) file for details.
