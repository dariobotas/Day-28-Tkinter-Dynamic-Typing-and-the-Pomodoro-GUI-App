from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1#25
SHORT_BREAK_MIN = 0.1#5
LONG_BREAK_MIN = 0.1#20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  title_label.config(text="Pomodoro")
  check_mark.config(text="")
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  #if it's the time 1st/3rd/5th/7th rep:
  #if it's the 8th rep:
  if reps % 8 == 0:
    title_label.config(text="Break", fg=RED)
    count_down(int(long_break_sec))
  #if are the other cases - 2nd/4th/6th
  elif reps % 2 == 0:
    title_label.config(text="Break", fg=PINK)
    count_down(int(short_break_sec))
  else:
    title_label.config(text="Work", fg=GREEN)
    count_down(int(work_sec))
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
 
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += "✓"
    check_mark.config(text=marks)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


title_label = Label(text="Pomodoro",font=(FONT_NAME, 25), bg=YELLOW, highlightthickness=0, fg=GREEN)
title_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="part2/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2, command=reset_time)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(row=3, column=1)

window.mainloop()