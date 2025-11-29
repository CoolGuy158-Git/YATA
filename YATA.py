#########################################
# YATA- Yet Another Terminal Application#
#---------------------------------------#
# Under MIT license                     #
# Copyright 2025 CoolGuy158-Git         #
#########################################
import customtkinter as ctk
import subprocess as sp
import re
# The thing that runs the commands
def run_commands(cmd):
    try:
        result = sp.run(cmd, capture_output=True, text=True, shell=True,
                        encoding="utf-8", errors="replace")
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        return stdout + stderr
    except Exception as e:
        return str(e)
def remove_ansi(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)
def on_enter(event=None):
    cmd = command_input.get()
    if cmd.strip() == "":
        return
    output_text.configure(state="normal")
    output_text.insert("end", f"> {cmd}\n")
    result = run_commands(cmd)
    clean_result = remove_ansi(result)
    output_text.insert("end", clean_result + "\n")
    output_text.see("end")
    output_text.configure(state="disabled")
    command_input.delete(0, "end")
    if 'instruction' in globals():
        instruction.destroy()

# GUI
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.geometry("900x600")
root.title("YATA")
root.attributes("-alpha", 0.85)
output_text = ctk.CTkTextbox(root)
output_text.pack(fill="both", expand=True)
instruction = ctk.CTkLabel(root, text="Type a command and press Enter")
instruction.pack(fill="x")
command_input = ctk.CTkEntry(root)
command_input.pack(fill="x")
command_input.bind("<Return>", on_enter)
root.mainloop()
