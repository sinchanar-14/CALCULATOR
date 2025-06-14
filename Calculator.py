import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium Scientific Calculator")
        self.theme = "dark"
        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        self.entry = tk.Entry(self.root, font="Arial 24", borderwidth=0, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=20, sticky="nsew", padx=10, pady=10)

        toggle_btn = tk.Button(self.root, text="🌙", command=self.toggle_theme, font="Arial 12 bold")
        toggle_btn.grid(row=0, column=4, sticky="ne", padx=5, pady=5)

        buttons = [
            ["sin", "cos", "tan", "sqrt", "log"],
            ["7", "8", "9", "/", "exp"],
            ["4", "5", "6", "*", "C"],
            ["1", "2", "3", "-", "⌫"],
            ["0", ".", "+", "=", ""]
        ]

        self.buttons = []
        for i, row in enumerate(buttons):
            button_row = []
            for j, text in enumerate(row):
                if text == "":
                    button_row.append(None)
                    continue

                if text == "=":
                    btn = tk.Button(self.root, text=text, font="Arial 16 bold", relief=tk.FLAT,
                                    bg="#28a745", fg="white", activebackground="#218838",
                                    command=lambda t=text: self.on_click(t))
                    btn.grid(row=i+1, column=j, columnspan=2, sticky="nsew", padx=5, pady=5)
                else:
                    btn = tk.Button(self.root, text=text, font="Arial 16", relief=tk.FLAT,
                                    command=lambda t=text: self.on_click(t))
                    btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

                button_row.append(btn)
            self.buttons.append(button_row)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.root.grid_columnconfigure(j, weight=1)

    def apply_theme(self):
        if self.theme == "dark":
            bg = "#1e1e1e"
            fg = "white"
            btn_bg = "#3c3c3c"
            active_bg = "#007acc"
        else:
            bg = "white"
            fg = "black"
            btn_bg = "#e6e6e6"
            active_bg = "#cccccc"

        self.root.config(bg=bg)
        self.entry.config(bg=btn_bg, fg=fg, insertbackground=fg)

        for row in self.buttons:
            for btn in row:
                if btn and btn.cget("text") != "=":
                    btn.config(bg=btn_bg, fg=fg, activebackground=active_bg)

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.apply_theme()

    def on_click(self, text):
        current = self.entry.get()
        try:
            if text == "=":
                result = eval(current, {"__builtins__": None}, math.__dict__)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            elif text == "C":
                self.entry.delete(0, tk.END)
            elif text == "⌫":
                self.entry.delete(len(current) - 1, tk.END)
            elif text in ["sin", "cos", "tan", "sqrt", "log", "exp"]:
                val = float(current)
                if text in ["log", "sqrt"] and val < 0:
                    raise ValueError("Invalid input")
                result = getattr(math, text)(val)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            else:
                self.entry.insert(tk.END, text)
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Divide by 0")
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x550")
    app = CalculatorApp(root)
    root.mainloop()
