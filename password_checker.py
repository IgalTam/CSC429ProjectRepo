import tkinter as tk

# TODO: instantiate LSTM
# TODO: instantiate GAN
def gan_score(s):
    return 1 - (0.8 ** len(s))

def lstm_score(s):
    return min(0.05 * len(s), 1)

def update_labels():
    s = entry.get()
    g_s = gan_score(s)
    l_s = lstm_score(s)
    if g_s < 0.6:
        label_gan.config(text = "PassGAN Grade", foreground = "red")
        label_gan_val.config(text = str(round(g_s * 100, 2)) + "%", foreground = "red")
    elif g_s < 0.8:
        label_gan.config(text = "PassGAN Grade", foreground = "orange")
        label_gan_val.config(text = str(round(g_s * 100, 2)) + "%", foreground = "orange")
    else:
        label_gan.config(text = "PassGAN Grade", foreground = "green")
        label_gan_val.config(text = str(round(g_s * 100, 2)) + "%", foreground = "green")
    if l_s < 0.6:
        label_lstm.config(text = "LSTM Grade", foreground = "red")
        label_lstm_val.config(text = str(round(l_s * 100, 2)) + "%", foreground = "red")
    elif l_s < 0.8:
        label_lstm.config(text = "LSTM Grade", foreground = "orange")
        label_lstm_val.config(text = str(round(l_s * 100, 2)) + "%", foreground = "orange")
    else:
        label_lstm.config(text = "LSTM Grade", foreground = "green")
        label_lstm_val.config(text = str(round(l_s * 100, 2)) + "%", foreground = "green")
    return

window = tk.Tk()
label = tk.Label(text="AMIANNPC Password Checker")
label_gan = tk.Label(text="PassGAN Grade", foreground="black", )
label_gan_val = tk.Label(text="--.--%", foreground="black")
label_lstm = tk.Label(text="LSTM Grade", foreground="black")
label_lstm_val = tk.Label(text="--.--%", foreground="black")
entry = tk.Entry()
label.pack()
entry.pack()
label_gan.pack()
label_gan_val.pack()
label_lstm.pack()
label_lstm_val.pack()

while True:
    update_labels()
    window.update_idletasks()
    window.update()