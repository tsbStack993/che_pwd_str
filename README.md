# Password Strength Checker

A simple, modern web application for checking password strength, built with **Flask** and styled using **Tailwind CSS**.  
It evaluates passwords against common security criteria and provides suggestions for improvement.

---

## Features

- **Checks for:**
  - Minimum length (8+ characters)
  - Uppercase and lowercase letters
  - Digits
  - Special characters
  - Not being a common password
- **Real-time feedback** on password strength
- **Suggestions** for making passwords stronger
- **Modern UI** with Tailwind CSS
- **Privacy notice:** Passwords are never stored or logged

---

## Usage

1. **Clone or download** this repository.

2. **Install dependencies:**
   ```
   pip install flask
   ```

3. **Run the app:**
   ```
   python app.py
   ```

4. **Open your browser** and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## File Structure

- `app.py` &mdash; Flask web application and HTML template
- `che_pwd.py` &mdash; Password strength checking logic

---


## License

MIT License

---

## Credits

- [Flask](https://flask.palletsprojects.com/)
