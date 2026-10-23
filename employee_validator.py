import tkinter as tk
from tkinter import messagebox

# دالة لمعالجة المدخلات
def check_inputs():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    employee_id = entry_employee_id.get()

    # التحقق من صحة المدخلات باستخدام if-else
    if len(first_name) < 2:
        messagebox.showerror("Error", f"\"{first_name}\" is not a valid first name. It is too short.")
    elif len(last_name) == 0:
        messagebox.showerror("Error", "The last name must be filled in.")
    elif not employee_id.isdigit():
        messagebox.showerror("Error", f"\"{employee_id}\" is not a valid ID.")
    else:
        messagebox.showinfo("Success", "Data is valid!")

# دالة لإضافة مستخدم
def add_user():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    employee_id = entry_employee_id.get()

    if first_name == "" or last_name == "" or employee_id == "":
        messagebox.showerror("Error", "All fields must be filled in.")
    else:
        messagebox.showinfo("User Added", f"User {first_name} {last_name} with ID {employee_id} added successfully!")

# إعداد نافذة Tkinter
root = tk.Tk()
root.title("تحقق من المدخلات")
root.geometry("400x400")
root.config(bg="#2c3e50")  # تغيير خلفية النافذة إلى لون غامق

# إضافة حقل الإدخال للاسم الأول
label_first_name = tk.Label(root, text="الاسم الأول:", fg="white", bg="#2c3e50", font=("Arial", 14))
label_first_name.pack(pady=5)
entry_first_name = tk.Entry(root, width=30, font=('Arial', 14), borderwidth=5, relief="solid", bg="#ecf0f1")
entry_first_name.pack(pady=5)

# إضافة حقل الإدخال للاسم الأخير
label_last_name = tk.Label(root, text="الاسم الأخير:", fg="white", bg="#2c3e50", font=("Arial", 14))
label_last_name.pack(pady=5)
entry_last_name = tk.Entry(root, width=30, font=('Arial', 14), borderwidth=5, relief="solid", bg="#ecf0f1")
entry_last_name.pack(pady=5)

# إضافة حقل الإدخال للرقم الوظيفي
label_employee_id = tk.Label(root, text="رقم الموظف:", fg="white", bg="#2c3e50", font=("Arial", 14))
label_employee_id.pack(pady=5)
entry_employee_id = tk.Entry(root, width=30, font=('Arial', 14), borderwidth=5, relief="solid", bg="#ecf0f1")
entry_employee_id.pack(pady=5)

# إضافة زر للتحقق من المدخلات
submit_button = tk.Button(root, text="تحقق من المدخلات", command=check_inputs, width=20, height=2, font=("Arial", 14), bg="#3498db", fg="white")
submit_button.pack(pady=10)

# إضافة زر لإضافة مستخدم
add_user_button = tk.Button(root, text="إضافة مستخدم", command=add_user, width=20, height=2, font=("Arial", 14), bg="#2ecc71", fg="white")
add_user_button.pack(pady=10)

# تشغيل التطبيق
root.mainloop()
