import tkinter as tk
from tkinter import scrolledtext
import requests
import json

window = tk.Tk()
window.title("Example ChatBox By DoseOfWeed")
window.geometry("400x500")

header_label = tk.Label(window, text="🤖if u see this ur %100 gay boiii", font=("Arial", 12))
header_label.pack(pady=10)

chat_area = scrolledtext.ScrolledText(window, width=40, height=20, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10)
chat_area.config(state='disabled')  

input_field = tk.Entry(window, width=30)
input_field.pack(pady=5)

send_button = tk.Button(window, text="Send", command=lambda: doseofweed_send())
send_button.pack(pady=5)

def doseofweed_send():
    user_msg = input_field.get()
    if user_msg.strip() != "":
        doseofweed_update(f"You: {user_msg}\n")
        input_field.delete(0, tk.END)
        
        try:
            response = requests.get(f"https://chatgpt.hosters.club/?chat={user_msg}")
            data = response.json()
            ai_reply = data.get("response", "No response!")
            doseofweed_update(f"AI: {ai_reply}\n")
        except:
            doseofweed_update("AI: Oops api fucked.\n")

def doseofweed_update(message):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, message)
    chat_area.see(tk.END)
    chat_area.config(state='disabled')

def doseofweed_start():
    window.mainloop()

if __name__ == "__main__":
    doseofweed_start()