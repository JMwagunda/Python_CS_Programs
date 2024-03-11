from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Create global variable for right_frame
right_frame = None

class PatientQueue:
    def __init__(self):
        self.storage = []

    def add_patient(self, item):
        self.storage.append(item)
        self.sort_list()

    def sort_list(self):
        self.storage.sort(key=lambda x: x[1], reverse=True)  # Sort by age

    def remove_patient(self, item):
        if item in self.storage:
            self.storage.remove(item)

    def replace_age(self, item, new_age):
        for patient in self.storage:
            if patient == item:
                patient[1] = new_age
        self.sort_list()

    def queue_size(self):
        return len(self.storage)

    def remove_first(self):
        if self.storage:
            removed_patient = self.storage.pop(0)
            messagebox.showinfo("Remove First", f"Removed Patient: {removed_patient[0]} (Age: {removed_patient[1]}, Priority: {removed_patient[2]})")
            return removed_patient
        else:
            messagebox.showerror("Error", "Queue is empty")
            return None
    def remove_last(self):
            if self.storage:
                removed_patient = self.storage.pop()
                messagebox.showinfo("Remove Last", f"Removed Patient: {removed_patient[0]} (Age: {removed_patient[1]}, Priority: {removed_patient[2]})")
                return removed_patient
            else:
                messagebox.showerror("Error", "Queue is empty")
                return None

    def get_last(self):
        if self.storage:
            last_patient = self.storage[-1]
            messagebox.showinfo("Get Last", f"Last Patient: {last_patient[0]} (Age: {last_patient[1]}, Priority: {last_patient[2]})")
        else:
            messagebox.showerror("Error", "Queue is empty")
    def get_first(self):
        if self.storage:
            patient = self.storage[0]
            messagebox.showinfo("Get First", f"First Patient: {patient[0]} (Age: {patient[1]}, Priority: {patient[2]})")
        else:
            messagebox.showerror("Error", "Queue is empty")

    def is_empty(self):
        return len(self.storage) == 0

    def poll_queue(self):
        if self.storage:
            return self.storage.pop(0)
        return None
    def get_highest_priority(self):
        if self.storage:
            return max(patient[2] for patient in self.storage)
        else:
            return 0

    def is_priority_assigned(self, priority):
        return any(patient[2] == priority for patient in self.storage)
    
# Function to draw patient icons
def draw_patients():
    for widget in right_frame.winfo_children():
        widget.destroy()

    patient_icons = []
    info_label = Label(right_frame, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"))
    info_label.pack(side=TOP)
    position_of_patient = 0

    for age, name, _ in queue.storage:
        img = Image.open('stickman.png')
        img = img.resize((40, 40))
        img = ImageTk.PhotoImage(img)

        position_of_patient += 1

        icon_label = Label(right_frame, bg='white', text=f'{position_of_patient}:{age},{name}yrs', image=img, compound="bottom")
        icon_label.image = img
        icon_label.pack(side=LEFT, padx=5)
        patient_icons.append(icon_label)

# Function to update the queue display
def update_queue_display():
    queue_listbox.delete(0, END)  # Clear the listbox
    for patient in queue.storage:
        queue_listbox.insert(END, f"{patient[0]} (Age: {patient[1]}, Priority: {patient[2]})")
        
def update_display():
    update_queue_display()
    draw_patients()

# Function to handle admitting a patient
def admit_patient():
    name = name_entry.get()
    age = age_entry.get()

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be an integer")
        return

    # Always assign consecutive priorities
    priority = queue.get_highest_priority() + 1

    if priority_entry.get() != '' and int(priority_entry.get()) != priority:
        messagebox.showerror("Error", "Assigned priority does not match the expected priority")
        return

    # Check if the priority is already assigned
    while queue.is_priority_assigned(priority):
        priority += 1

    patient = [name, age, priority]

    if queue.queue_size() == 10:
        messagebox.showerror("Error", "Queue is already full")
    else:
        queue.add_patient(patient)
        update_display()
        clear_input_fields()

# Function to handle deleting a patient
def delete_patient():
    name = name_entry.get()
    age = age_entry.get()
    priority = priority_entry.get()

    if not name or not age or not priority:
        messagebox.showerror("Error", "Please enter patient details for deletion")
        return

    try:
        age = int(age)
        priority = int(priority)
    except ValueError:
        messagebox.showerror("Error", "Age and priority must be integers")
        return

    patient = [name, age, priority]
    if patient not in queue.storage:
        messagebox.showerror("Error", "Patient not found in the queue")
        return

    queue.remove_patient(patient)
    messagebox.showinfo("Remove Patient", f"Removed Patient: {patient[0]} (Age: {patient[1]}, Priority: {patient[2]})")
    
    update_queue_display()
    draw_patients()
    clear_input_fields()

# Function to replace age
def replace_age():
    name = update_name_entry.get()
    new_age = update_age_entry.get()

    if not name or not new_age:
        messagebox.showerror("Error", "Please enter patient details for updating")
        return

    try:
        new_age = int(new_age)
    except ValueError:
        messagebox.showerror("Error", "New age must be an integer")
        return

    # Find the patient in the queue
    patient_found = False
    for index, patient in enumerate(queue.storage):
        if patient[0] == name:
            patient_found = True
            # Update the patient's age
            patient[1] = new_age
            messagebox.showinfo("Update", f"Patient {name}, Age: {new_age}, Priority: {patient[2]} has been moved to the front of the queue.")

            break

    if not patient_found:
        messagebox.showerror("Error", "Patient not found in the queue")

    queue.sort_list()  # Re-sort the queue based on the updated ages

    update_queue_display()
    update_display()
    clear_input_fields()

# Function to handle checking the queue size
def check_queue_size():
    size = queue.queue_size()
    messagebox.showinfo("Queue Size", f"The current size of the queue is {size}")

# Function to handle removing the first patient from the queue
def remove_first_patient():
    removed_patient = queue.remove_first()
    if removed_patient:
        update_display()

# Function to handle getting information about the first patient without removing them
def get_first_patient():
    queue.get_first()
    update_display()
    
# Function to handle removing the last patient from the queue
def remove_last_patient():
    removed_patient = queue.remove_last()
    if removed_patient:
        update_display()

# Function to handle getting information about the last patient without removing them
def get_last_patient():
    queue.get_last()
    update_display()

# Function to handle checking if the queue is empty
def check_if_empty():
    if queue.is_empty():
        messagebox.showinfo("Is Empty", "The queue is empty")
    else:
        messagebox.showinfo("Is Empty", "The queue is not empty")


# Function to clear input fields
def clear_input_fields():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    priority_entry.delete(0, END)
    update_name_entry.delete(0, END)
    update_age_entry.delete(0, END)

# Function to update the queue display
def update_queue_display():
    queue_listbox.delete(0, END)  # Clear the listbox
    for patient in queue.storage:
        queue_listbox.insert(END, f"{patient[0]} (Age: {patient[1]}, Priority: {patient[2]})")

# Create main window
window = Tk()
window.title("Patient Queue System")

# Create frames
input_frame = Frame(window)
input_frame.pack(side=LEFT, padx=10)

queue_display_frame = Frame(window)
queue_display_frame.pack(side=RIGHT, padx=10)

# Create input widgets
Label(input_frame, text="Name:").grid(row=0, column=0)
name_entry = Entry(input_frame, width=30, borderwidth=2)
name_entry.grid(row=0, column=1)

Label(input_frame, text="Age:").grid(row=1, column=0)
age_entry = Entry(input_frame, width=30, borderwidth=2)
age_entry.grid(row=1, column=1)

Label(input_frame, text="Priority:").grid(row=2, column=0)
priority_entry = Entry(input_frame, width=30, borderwidth=2)
priority_entry.grid(row=2, column=1)

admit_button = Button(input_frame, text="Admit", command=admit_patient)
admit_button.grid(row=3, column=0, pady=5)

delete_button = Button(input_frame, text="Delete", command=delete_patient)
delete_button.grid(row=3, column=1, pady=5)

Label(input_frame, text="Name:").grid(row=4, column=0)
update_name_entry = Entry(input_frame, width=30, borderwidth=2)
update_name_entry.grid(row=4, column=1)

Label(input_frame, text="Age:").grid(row=5, column=0)
update_age_entry = Entry(input_frame, width=30, borderwidth=2)
update_age_entry.grid(row=5, column=1)

update_button = Button(input_frame, text="Update", command=replace_age)
update_button.grid(row=6, column=1, pady=5)

remove_first_button = Button(input_frame, text="Remove First", command=remove_first_patient)
remove_first_button.grid(row=7, column=1, pady=5)

get_first_button = Button(input_frame, text="Get First", command=get_first_patient)
get_first_button.grid(row=7, column=0, pady=5)

is_empty_button = Button(input_frame, text="Is Empty", command=check_if_empty)
is_empty_button.grid(row=8, column=1, pady=5)

remove_last_button = Button(input_frame, text="Remove Last", command=remove_last_patient)
remove_last_button.grid(row=9, column=0, pady=5)

get_last_button = Button(input_frame, text="Get Last", command=get_last_patient)
get_last_button.grid(row=9, column=1, pady=5)

queue_size_button = Button(input_frame, text="Length", command=check_queue_size)
queue_size_button.grid(row=8, column=0, pady=5)

# Create a listbox for displaying the queue
queue_listbox = Listbox(queue_display_frame, width=40, height=10)
queue_listbox.grid(row=0, column=0, padx=5, pady=10)

# Initialize the patient queue
queue = PatientQueue()

# Create the right frame
right_frame = Frame(window)
right_frame.pack(side=RIGHT, padx=10)

# Start the GUI main loop
window.mainloop()
