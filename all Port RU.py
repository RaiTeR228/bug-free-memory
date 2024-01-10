import tkinter as tk
import tkinter.scrolledtext as scrolledtext

def print_numbers():
    start = int(entry_start.get())
    end = int(entry_end.get())
    numbers = list(range(start, end+1))
    if var.get() == 1:  # вывод в столбик
        result_text = "\n".join(str(num) for num in numbers)
    else:  # вывод в строку
        result_text = " ".join(str(num) for num in numbers)
    result_textbox.delete(1.0, tk.END)
    result_textbox.insert(tk.END, result_text)

def copy_to_clipboard():
    result = result_textbox.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(result)

def save_to_file():
    result = result_textbox.get(1.0, tk.END)
    with open("numbers.txt", "w") as file:
        file.write(result)

# Создание графического интерфейса
root = tk.Tk()
root.title("Приложение для печати чисел")

label_start = tk.Label(root, text="Начальное число:")
label_start.grid(row=0, column=0, padx=10, pady=5)

entry_start = tk.Entry(root)
entry_start.grid(row=0, column=1, padx=10, pady=5)

label_end = tk.Label(root, text="Конечное число:")
label_end.grid(row=1, column=0, padx=10, pady=5)

entry_end = tk.Entry(root)
entry_end.grid(row=1, column=1, padx=10, pady=5)

var = tk.IntVar()
var.set(1)  # значение по умолчанию (вывод в столбик)
radio_button1 = tk.Radiobutton(root, text="В столбик", variable=var, value=1)
radio_button1.grid(row=2, column=0, padx=10, pady=5)

radio_button2 = tk.Radiobutton(root, text="В строку", variable=var, value=2)
radio_button2.grid(row=2, column=1, padx=10, pady=5)

print_button = tk.Button(root, text="Печать чисел", command=print_numbers)
print_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

result_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=10)
result_textbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

copy_button = tk.Button(root, text="Копировать", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, padx=10, pady=5)

save_button = tk.Button(root, text="Сохранить в файл", command=save_to_file)
save_button.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
