import tkinter as tk
import ezgmail

def send_email():
    ezgmail.send(recipient_area.get(), subject_area.get(), email_area.get("1.0", tk.END))

window = tk.Tk()
window.title("Send Emails")

window.columnconfigure([0, 1], minsize=100, weight=1)
window.rowconfigure(0, minsize=50, weight=1)

# buttons, labels and entries on the left hand side
side_pane = tk.Frame(master=window)
side_pane.grid(row=0, column=0, sticky="ns")

recipient_area = tk.Entry(master=side_pane)
recipient_label = tk.Label(master=side_pane, text="To:")
recipient_label.grid(row=1, column=0, sticky="ew")
recipient_area.grid(row=2, column=0, sticky="ew")

subject_area = tk.Entry(master=side_pane)
subject_label = tk.Label(master=side_pane, text="Subject:")
subject_label.grid(row=3, column=0, sticky="ew")
subject_area.grid(row=4, column=0, sticky="ew")

#email body area
email_pane = tk.Frame(master=window)
email_pane.grid(row=0, column=1, sticky="nsew")
email_area = tk.Text(master=email_pane)
email_area.grid(row=0, column=1, padx=5, pady=5)

send_btn = tk.Button(master=side_pane, text="Send", command=send_email)
send_btn.grid(row=0, column=0, padx=5, pady=10)

window.mainloop()
