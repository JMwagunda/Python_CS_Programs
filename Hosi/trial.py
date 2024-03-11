from tkinter import *
from tkinter import messagebox

class PatientQueue:
    def __init__(self):
        self.storage = []
        self.size = 0

    def add_patient(self, item):
        self.storage.append(item)
        self.sort_list()

    def sort_list(self):
        self.storage.sort(key=lambda x: x[2])  # Sort by priority

    def remove_patient(self, item):
        if item in self.storage:
            self.storage.remove(item)

    def replace_priority(self, item, new_priority):
        for patient in self.storage:
            if patient == item:
                patient[2] = new_priority
        self.sort_list()

    def queue_size(self):
        return len(self.storage)

    def peek_queue(self):
        return self.storage[0] if self.storage else None
    
    def remove_first(self):
        if self.storage:
            self.storage.pop(0)
            messagebox.showinfo("Remove First", "Removed the first patient from the queue")
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

# Function to handle admitting a patient
def admit_patient():
    name = name_entry.get()
    age = age_entry.get()

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be an integer")
        return

    # Always assign priority 1 for the first patient, and consecutive priorities for the rest
    priority = 1 if queue.queue_size() == 0 else queue.queue_size() + 1

    if priority_entry.get() != '' and int(priority_entry.get()) != priority:
        messagebox.showerror("Error", "Assign priority 1 for the first patient, and consecutive priorities for the rest")
        return

    # Check if the priority is already assigned
    for patient in queue.storage:
        if patient[2] == priority:
            messagebox.showerror("Error", f"Priority {priority} is already assigned to another patient")
            return

    patient = [name, age, priority]
    
    if queue.queue_size() == 7:
        messagebox.showerror("Error", "Queue is already full")
    else:
        queue.add_patient(patient)
        update_queue_display()
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
    update_queue_display()
    clear_input_fields()
    
def replace_priority():
    name = update_name_entry.get()
    new_priority = update_priority_entry.get()

    if not name or not new_priority:
        messagebox.showerror("Error", "Please enter patient details for updating")
        return

    try:
        new_priority = int(new_priority)
    except ValueError:
        messagebox.showerror("Error", "New priority must be an integer")
        return

    # Find the patient in the queue
    patient_found = False
    for index, patient in enumerate(queue.storage):
        if patient[0] == name:
            patient_found = True
            # Update the patient's priority
            patient[2] = new_priority
            break

    if not patient_found:
        messagebox.showerror("Error", "Patient not found in the queue")

    queue.sort_list()  # Re-sort the queue based on the updated priorities

    update_queue_display()
    clear_input_fields()
    
# Function to handle checking the queue size
def check_queue_size():
    size = queue.queue_size()
    messagebox.showinfo("Queue Size", f"The current size of the queue is {size}")

# Function to handle peeking at the front of the queue
def peek_at_queue():
    patient = queue.peek_queue()
    if patient:
        messagebox.showinfo("Peek", f"Next Patient: {patient[0]} (Age: {patient[1]}, Priority: {patient[2]})")
    else:
        messagebox.showerror("Error", "Queue is empty")

# Function to handle removing the first patient from the queue
def remove_first_patient():
    queue.remove_first()
    update_queue_display()

# Function to handle getting information about the first patient without removing them
def get_first_patient():
    queue.get_first()

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
    update_priority_entry.delete(0, END)

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

Label(input_frame, text="Priority:").grid(row=5, column=0)
update_priority_entry = Entry(input_frame, width=30, borderwidth=2)
update_priority_entry.grid(row=5, column=1)

update_button = Button(input_frame, text="Update", command=replace_priority)
update_button.grid(row=6, column=1, pady=5)

remove_first_button = Button(input_frame, text="Remove First", command=remove_first_patient)
remove_first_button.grid(row=8, column=0, pady=5)

get_first_button = Button(input_frame, text="Get First", command=get_first_patient)
get_first_button.grid(row=8, column=1, pady=5)

is_empty_button = Button(input_frame, text="Is Empty", command=check_if_empty)
is_empty_button.grid(row=9, column=0, pady=5)
queue_size_button = Button(input_frame, text="Length", command=check_queue_size)
queue_size_button.grid(row=7, column=0, pady=5)

peek_button = Button(input_frame, text="Peek", command=peek_at_queue)
peek_button.grid(row=7, column=1, pady=5)

# Create a listbox for displaying the queue
queue_listbox = Listbox(queue_display_frame, width=40, height=10)
queue_listbox.grid(row=0, column=0, padx=5, pady=10)

# Initialize the patient queue
queue = PatientQueue()

# Start the GUI main loop
window.mainloop()
