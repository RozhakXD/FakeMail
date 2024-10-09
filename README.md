# FakeMail: A Smart Fake Email Generator Tool 📨

![FakeMail Logo](https://github.com/user-attachments/assets/0bac1622-7077-4f9e-96b6-bd0b58432ee3)

[**FakeMail**](https://github.com/RozhakLabs/FakeMail) is a Python program designed to generate random and fake emails using various methods. It offers a simple and intuitive menu for users to create emails from different sources, check email validity, and more.

## 🚀 Features

FakeMail offers a versatile set of features for creating fake email addresses. You can generate emails from real names, random strings, or utilize popular libraries like `randomuser` and `mimesis`, and `faker` for more realistic data. Furthermore, the program includes a built-in email validator to check a list of emails and determine which ones are still active.

## 📖 How to Use

1. **Clone the Repository:**
   
   ```
   git clone https://github.com/RozhakLabs/FakeMail.git
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

This tool should be used only for ethical and legal purposes. Generating fake emails for spamming, fraudulent activities, or any actions that breach terms of service is not permitted. Make sure you have the necessary permissions to use any domain names or email addresses. Misuse of this tool can result in severe legal consequences and is contrary to responsible use guidelines.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.