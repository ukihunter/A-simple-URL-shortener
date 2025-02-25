import customtkinter as ctk
import pyshorteners
import pyperclip
import time
import threading
from CTkMessagebox import CTkMessagebox


def shorten_url():
    long_url = url_entry.get()
    if not long_url:
        result_label.configure(text="Please enter a URL", text_color="red")
        return

    result_label.configure(text="Shortening...", text_color="yellow")

    def process():
        time.sleep(1)
        if tiny_var.get():
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
        elif bitly_var.get():
            api_key = "aa26e34e38e089295dba4fc95984989be5acf009"  # Replace with a valid API key
            shortener = pyshorteners.Shortener(api_key=api_key)
            short_url = shortener.bitly.short(long_url)
        else:
            result_label.configure(text="Please select a shortening service", text_color="red")
            return

        result_label.configure(text=short_url, text_color="green")
        copy_button.configure(state=ctk.NORMAL)  

    threading.Thread(target=process).start()

# Function to copy URL to clipboard
def copy_to_clipboard():
    pyperclip.copy(result_label.cget("text"))
    CTkMessagebox(title="Success", message="Shortened URL copied to clipboard!", icon="check")

# GUI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("URL Shortener By UKI")
root.geometry("950x70")
root.resizable(False, False)

# Main Frame
frame = ctk.CTkFrame(root, corner_radius=15)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Widgets in grid layout
url_entry = ctk.CTkEntry(frame, width=200, height=35, font=("Arial", 12),placeholder_text="Enter the URL...")
url_entry.grid(row=2, column=0, padx=5, pady=5)

shorten_button = ctk.CTkButton(frame, text="Shorten", command=shorten_url, fg_color="#3b82f6", hover_color="#2563eb", corner_radius=10, font=("Arial", 14))
shorten_button.grid(row=2, column=1, padx=5, pady=5)

tiny_var = ctk.BooleanVar()
bitly_var = ctk.BooleanVar()

tiny_check = ctk.CTkCheckBox(frame, text="TinyURL", variable=tiny_var, font=("Arial", 12))
tiny_check.grid(row=2, column=2, padx=5, pady=5)

bitly_check = ctk.CTkCheckBox(frame, text="Bitly", variable=bitly_var, font=("Arial", 12))
bitly_check.grid(row=2, column=3, padx=5, pady=5)

result_label = ctk.CTkLabel(frame, text="", font=("Arial", 14), text_color="white")
result_label.grid(row=2, column=4, padx=4, pady=5)

copy_button = ctk.CTkButton(frame, text="Copy", command=copy_to_clipboard, state=ctk.DISABLED, fg_color="#10b981", hover_color="#059669", corner_radius=10, font=("Arial", 12))
copy_button.grid(row=2, column=5, padx=5, pady=5)  

root.mainloop()
