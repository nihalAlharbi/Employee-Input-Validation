<div align="center">

# 👩‍💻 Employee Input Validation

### A small desktop app with a big focus on getting user input right.

**Python · Tkinter · GUI Development · Input Validation**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-8E44AD?style=flat-square)
![Status](https://img.shields.io/badge/Project-Learning%20Project-E91E63?style=flat-square)

A beginner-friendly Python desktop application that collects employee details, checks selected input rules, and communicates results through clear pop-up messages.

</div>

---

## ✨ What does it do?

Instead of accepting every value silently, the application gives users immediate feedback when certain fields need attention.

| Feature | What happens |
| --- | --- |
| 📝 Employee details | Enter a first name, last name, and employee ID |
| 🔎 Check inputs | Validate first-name length, nonempty last name, and numeric employee ID |
| 💬 Feedback | Display an error or success dialog |
| 👤 Add User | Display a confirmation message when all fields are nonempty |

## 📸 A look at the application

<div align="center">

![Actual Employee Input Validation application window](application.png)

*Real screenshot of the Tkinter interface.*

</div>

## 🧰 Built with

- **Python 3** — application logic and conditional validation
- **Tkinter** — desktop interface, form fields, buttons, and message dialogs
- **Standard library only** — no third-party Python packages required

## 🚀 Run it locally

1. Install **Python 3** with Tkinter support.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```bash
python employee_validator.py
```

The desktop window opens with three input fields and two action buttons.

## 🧪 Try these examples

| Input | Expected result when clicking *Check Inputs* |
| --- | --- |
| First name: `A` | Error: first name is too short |
| Empty last name | Error: last name is required (if the first name passes validation) |
| Employee ID: `ABC` | Error: ID must contain digits only (if names pass validation) |
| First name: `Sara`, last name: `Ali`, ID: `123` | Success message |

## 📌 Current scope and limitations

This project demonstrates **GUI design and basic validation**, not a complete employee management system.

- The last-name check currently tests for an empty value, not a minimum length.
- **Add User** checks that fields are nonempty and shows a confirmation; it **does not save employee records**.
- The Add User action does not apply all the same validation rules as the Check Inputs action.

## 💡 Skills practiced

Building forms, handling button events, applying conditional logic, and giving clear user feedback in a Python desktop interface.

---

<div align="center">

**Built as a hands-on Python learning project.**

[Explore more projects](https://github.com/nihalAlharbi?tab=repositories)

</div>
