import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def add(self, k, v):
        item = [k, v]
        self.pq.append(item)
        self.pq.sort(reverse=True, key=lambda x: x[0])
        return self.pq

    def first_item(self):
        return self.pq[0]

    def remove_first(self):
        return self.pq.pop(0)

    def remove_at_position(self, pos):
        pos -= 1
        return self.pq.pop(pos)

    def update_element(self, old_pos, new_pos):
        key, value = self.pq.pop(old_pos - 1)
        the_item = [str(key), value]
        self.pq.insert(new_pos - 1, the_item)

    def is_empty(self):
        return len(self.pq) == 0

    def get_length(self):
        return len(self.pq)

    def get_pq(self):
        return self.pq


class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Priority Queue")
        self.patient_pq = PriorityQueue()
        self.max_size = 9

        self.create_frames()
        self.create_labels_and_entries()
        self.create_buttons()
        self.pack_widgets()

    def create_frames(self):
        self.right_frame = tk.Frame(self.root, bg='white', bd=2, relief="solid", width=600, height=200)
        self.right_frame.pack(side=tk.RIGHT, padx=5, ipadx=20, ipady=10)
        self.right_frame.pack_propagate(0)

        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, padx=5, pady=5)

    def create_labels_and_entries(self):
        self.patient_name = tk.StringVar()
        self.patient_age = tk.StringVar()
        self.remove_at_var = tk.StringVar()
        self.old_pos_var = tk.StringVar()
        self.new_pos_var = tk.StringVar()

        self.age_label = tk.Label(self.left_frame, text="Enter Age", padx=5, pady=10, fg="black")
        self.name_label = tk.Label(self.left_frame, text="Enter Name", padx=5, pady=10, fg="black")
        self.enter_age = tk.Entry(self.left_frame, textvariable=self.patient_age, font=14, justify="center",
                                  bg="white", fg="black", width=20)
        self.enter_name = tk.Entry(self.left_frame, textvariable=self.patient_name, font=14, justify="center",
                                   bg="white", fg="black", width=20)

        self.remove_at_label = tk.Label(self.left_frame, text="Enter Position to remove", padx=5, pady=10, fg="black")
        self.remove_at_entry = tk.Entry(self.left_frame, textvariable=self.remove_at_var, font=12, justify="center",
                                        bg="white", fg="black", width=20)

        self.update_old_label = tk.Label(self.left_frame, text="Enter old then new Position", padx=5, pady=10, fg="black")
        self.update_new_label = tk.Label(self.left_frame, text="Enter New Position", padx=5, pady=10, fg="black")
        self.update_old_entry = tk.Entry(self.left_frame, textvariable=self.old_pos_var, font=12, justify="center",
                                         bg="white", fg="black", width=20)
        self.update_new_entry = tk.Entry(self.left_frame, textvariable=self.new_pos_var, font=12, justify="center",
                                         bg="white", fg="black", width=20)

    def create_buttons(self):
        self.add_button = tk.Button(self.left_frame, text="Add", command=self.add_patient)
        self.get_first_button = tk.Button(self.left_frame, text="Get First", command=self.get_first_patient)
        self.remove_first_button = tk.Button(self.left_frame, text="Remove First", command=self.remove_first_patient)
        self.is_empty_button = tk.Button(self.left_frame, text="Is Empty", command=self.update_is_empty_label)
        self.length_button = tk.Button(self.left_frame, text="Length", command=self.update_length_label)
        self.remove_at_button = tk.Button(self.left_frame, text="Remove At", command=self.remove_at)
        self.update_button = tk.Button(self.left_frame, text="Update Position", command=self.update_patient)


    def pack_widgets(self):
        self.name_label.pack(side=tk.TOP)
        self.enter_name.pack(side=tk.TOP)
        self.age_label.pack(side=tk.TOP)
        self.enter_age.pack(side=tk.TOP)
        self.add_button.pack(side=tk.TOP, padx=5, pady=5)
        self.remove_at_label.pack(side=tk.TOP)
        self.remove_at_entry.pack(side=tk.TOP, padx=5, pady=5)
        self.remove_at_button.pack(side=tk.TOP, padx=5, pady=5)
        self.update_old_label.pack(side=tk.TOP, padx=5, pady=5)
        self.update_old_entry.pack(side=tk.TOP, padx=5, pady=5)
        self.update_new_entry.pack(side=tk.TOP, padx=5, pady=5)
        self.update_button.pack(side=tk.TOP, padx=5, pady=5)
        self.get_first_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.remove_first_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.is_empty_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.length_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.remove_at_button.pack(side=tk.TOP, padx=5, pady=5)
        self.update_button.pack(side=tk.TOP, padx=5, pady=5)

    def draw_patients(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        patient_icons = []
        self.info_label = tk.Label(self.right_frame, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"), bg="white")
        self.info_label.pack(side=tk.TOP)
        position_of_patient = 0

        for age, name in self.patient_pq.get_pq():
            img = Image.open('stickman.png')
            img = img.resize((40, 40))
            img = ImageTk.PhotoImage(img)

            position_of_patient += 1

            icon_label = tk.Label(self.right_frame, bg='white', text=f'{position_of_patient}:{name},{age}yrs', image=img, compound="bottom")
            icon_label.image = img
            icon_label.pack(side=tk.LEFT, padx=5)
            patient_icons.append(icon_label)

    def update_length_label(self):
        length = self.patient_pq.get_length()
        self.info_label.config(text=f"{length} Patients")

    def update_is_empty_label(self):
        is_empty = self.patient_pq.is_empty()
        self.info_label.config(text=f"Empty: {str(is_empty)}")

    def add_patient(self):
        try:
            if self.patient_pq.get_length() < self.max_size:
                age = int(self.patient_age.get())
                name = str(self.patient_name.get())
                self.patient_pq.add(age, name)

                self.draw_patients()

                self.patient_age.set("")
                self.patient_name.set("")
            else:
                self.info_label.config(text=f"Priority Queue is Full")
        except ValueError:
            self.info_label.config(text=f"Invalid Age")

    def get_first_patient(self):
        if not self.patient_pq.is_empty():
            first_age, first_name = self.patient_pq.first_item()
            self.info_label.config(text=f"First is: {first_name}, {first_age} years old")
        else:
            self.info_label.config(text=f"Priority Queue is empty")

    def remove_first_patient(self):
        if not self.patient_pq.is_empty():
            first_age, first_name = self.patient_pq.remove_first()
            self.draw_patients()
            self.info_label.config(text=f"{first_name} {first_age} years is Removed")
        else:
            self.draw_patients()
            self.info_label.config(text=f"Priority Queue is empty")

    def remove_at(self):
        try:
            the_pos = int(self.remove_at_var.get())
            if 0 < the_pos < self.patient_pq.get_length():
                age, name = self.patient_pq.remove_at_position(the_pos)
                self.draw_patients()
                self.info_label.config(text=f"{name} {age} years is Removed")
                self.remove_at_var.set("")
            else:
                self.info_label.config(text=f"Patient's position doesn't exist in the queue")
        except ValueError:
            self.info_label.config(text=f"Invalid Position")

    def update_patient(self):
        try:
            old_pos_patient = int(self.old_pos_var.get())
            new_pos_patient = int(self.new_pos_var.get())

            if 0 < old_pos_patient < self.patient_pq.get_length():
                self.patient_pq.update_element(old_pos_patient, new_pos_patient)
                self.draw_patients()
                self.old_pos_var.set("")
                self.new_pos_var.set("")
            else:
                self.info_label.config(text=f"Patient's position doesn't exist in the queue")
        except ValueError:
            self.info_label.config(text=f"Invalid Position")


# Run the App
root = tk.Tk()
app = CandyDispenserApp(root)
root.mainloop()
