from os import WEXITED
import tkinter as tk
import webbrowser
from indeed_data import indeed_fun
from simply_hired_data import sh_fun


def callback(url):
    webbrowser.open_new(url)


def print_jobs(job_name, job_location):

    # INDEED

    # print("\nJobs from Indeed\n")
    indeed_obj = indeed_fun(job_name, job_location)

    for i in range(0, min(5, len(indeed_obj["titles"]))):

        # data

        str = indeed_obj["titles"][i]+"\n"+indeed_obj["ratings"][i] + "\n" + indeed_obj["company"][i] + \
            "\n" + indeed_obj["location"][i]
        url = indeed_obj["links"][i]

        # layout

        frm_indeed.rowconfigure(i, weight=1, minsize=50)

        frm_indeed_cell = tk.Frame(master=frm_indeed)
        frm_indeed_cell.grid(row=i, column=0, padx=5, pady=5)

        greeting_btn = tk.Button(
            master=frm_indeed_cell,
            text=str,
            foreground="purple",
            background="yellow",
            cursor="hand2",
            command=lambda e=url: callback(e),
            width=25,
            height=6
        )
        greeting_btn.pack()

    # SIMPLY HIRED

    # print("Jobs from Simply Hired\n")
    simply_hired_obj = sh_fun(job_name, job_location)

    for i in range(0, min(5, len(simply_hired_obj["titles"]))):

        # data

        str = simply_hired_obj["titles"][i]+"\n" + simply_hired_obj["company"][i] + "\n" + \
            simply_hired_obj["location"][i]
        url = simply_hired_obj["links"][i]

        # layout

        frm_simply_hired.rowconfigure(i, weight=1, minsize=50)

        frm_simply_hired_cell = tk.Frame(master=frm_simply_hired)
        frm_simply_hired_cell.grid(row=i, column=0, padx=5, pady=5)

        greeting_btn = tk.Button(
            master=frm_simply_hired_cell,
            text=str,
            foreground="purple",
            background="yellow",
            cursor="hand2",
            command=lambda e=url: callback(e),
            width=25,
            height=6
        )
        greeting_btn.pack()


def init_print_jobs():
    job_name = job_name_entry.get()
    job_location = job_location_entry.get()
    print_jobs(job_name, job_location)


window = tk.Tk()

#  Frames

# Four frames that add up to our primary vertical grid

for i in range(0, 4):
    window.rowconfigure(i, weight=1, minsize=50)

window.columnconfigure(0, weight=1, minsize=75)

frm_name = tk.Frame(master=window)
frm_name.grid(row=0, column=0, padx=5, pady=5)

frm_location = tk.Frame(master=window)
frm_location.grid(row=1, column=0, padx=5, pady=5)

frm_button = tk.Frame(master=window)
frm_button.grid(row=2, column=0, padx=5, pady=5)

frm_jobs = tk.Frame(master=window)
frm_jobs.grid(row=3, column=0, padx=5, pady=5)

# Two frames that add up to our horizontal job grid

for i in range(0, 2):
    frm_jobs.columnconfigure(i, weight=1, minsize=75)

frm_jobs.rowconfigure(i, weight=1, minsize=50)

frm_indeed = tk.Frame(master=frm_jobs)
frm_indeed.grid(row=0, column=0, padx=5, pady=5)

frm_simply_hired = tk.Frame(master=frm_jobs)
frm_simply_hired.grid(row=0, column=1, padx=5, pady=5)


# Labels and Entries

job_name_label = tk.Label(master=frm_name, text="Job Name")
job_name_entry = tk.Entry(master=frm_name, fg="black", bg="white", width=50)
job_location_label = tk.Label(master=frm_location, text="Job Location")
job_location_entry = tk.Entry(
    master=frm_location, fg="black", bg="white", width=50)

job_name_label.pack(side=tk.LEFT)
job_name_entry.pack(side=tk.LEFT)
job_location_label.pack(side=tk.LEFT)
job_location_entry.pack(side=tk.LEFT)

go_btn = tk.Button(
    master=frm_button,
    text="Go!!",
    foreground="white",
    background="black",
    width="3",
    height="1",
    command=init_print_jobs
)

go_btn.pack()

window.mainloop()
