# pyinstaller --paths=E:\myCreate\code_scrape\.venv\Lib\site-packages app.py --onefile --hide-console hide-early
import tkinter as tk
from tkinter import ttk

import scrape


class Report(tk.Tk):
    def __init__(self):
        super().__init__()
        style = ttk.Style()
        self.title("Scraper")

        style.configure(
            "Custom.TButton",
            foreground="#15903d",
            background="#15903d",
            font=("Times New Roman", 15),
            relief="raised",
        )
        self.geometry("280x200")
        self.configure(padx=20, pady=20)

        self.rowconfigure(0, pad=30)
        self.rowconfigure(1, pad=20)
        self.columnconfigure(0, pad=20)

        self.title_lbl = ttk.Label(
            self,
            text="Scraper",
            foreground="#15903d",
            font=("Segoe Script", 23, "bold"),
        )
        self.title_lbl.grid(row=0, column=0)

        self.exit_btn = ttk.Button(
            self, text="START", command=self.scraping, style="Custom.TButton"
        )
        self.exit_btn.grid(row=1, column=0)

    def scraping(self):
        scraping = scrape.Scraping()


if __name__ == "__main__":
    report = Report()
    report.mainloop()
