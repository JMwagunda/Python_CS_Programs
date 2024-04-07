import math 
import random  

class SingleServer(): 
    def __init__(self):  # Constructor method to initialize the simulation parameters
        # Constants for server status
        self.Q_LIMIT = 100  
        self.BUSY = 1  
        self.IDLE = 0  
        # Simulation variables
        self.next_event_type = 0 
        self.num_custs_delayed = 0  
        self.num_delays_required = 0  
        self.num_events = 0  
        self.num_in_q = 0  
        self.server_status = self.IDLE  

        # Statistical counters
        self.area_num_in_q = 0.0  
        self.area_server_status = 0.0  
        self.mean_interarrival = 0.0  
        self.mean_service = 0.0  
        self.sim_time = 0.0 
        self.time_arrival = [0.0] * (self.Q_LIMIT + 1)  
        self.time_last_event = 0.0  
        self.total_of_delays = 0.0 
        self.time_next_event = [0.0, 0.0, 1.0e+30]  
        
    def expon(self, mean):  # Exponential distribution function
        return -mean * math.log(random.random())  # Generate random numbers from exponential distribution

    def initialize(self):  # Initialize simulation
        self.sim_time = 0.0  
        self.server_status = self.IDLE  
        self.num_in_q = 0  
        self.time_last_event = 0.0 
        self.num_custs_delayed = 0  
        self.total_of_delays = 0.0  

        # Set initial event times 
        self.time_arrival = [0.0] * (self.Q_LIMIT + 1)
        self.time_next_event = [0.0, 0.0, 1.0e+30]
        self.time_next_event[1] = self.sim_time + self.expon(self.mean_interarrival)

    def timing(self):  # Determine the next event
        min_time_next_event = 1.0e+29
        self.next_event_type = 0

        # Find the type of the next event
        for i in range(0, self.num_events):
            if self.time_next_event[i] < min_time_next_event:
                min_time_next_event = self.time_next_event[i]
                self.next_event_type = i + 1

        # Check if the event list is empty
        if self.next_event_type == 0:
            # Stop simulation if event list is empty
            with open("output.txt", 'w') as outfile:
                outfile.write(f"Event list empty at time {self.sim_time}")
        # Update simulation time
        self.sim_time = min_time_next_event

    def arrive(self):  # Arrival event
        self.time_next_event[0] = self.sim_time + self.expon(self.mean_interarrival)

        if self.server_status == self.BUSY:  # If server is busy
            self.num_in_q += 1  # Increment number of customers in queue

            if self.num_in_q > self.Q_LIMIT:  # Check for queue overflow
                with open("output.txt", 'w') as outfile:
                    outfile.write(f"Overflow of the array time_arrival at {self.sim_time} and number = {self.num_in_q}")

            # Update arrival time for the new customer
            self.time_arrival[self.num_in_q] = self.sim_time
        else:  # If server is idle
            delay = 0.0
            self.total_of_delays += delay  
            self.num_custs_delayed += 1  
            self.server_status = self.BUSY  
            self.time_next_event[1] = self.sim_time + self.expon(self.mean_service) 

    def depart(self):  # Departure event
        if self.num_in_q == 0:  
            self.server_status = self.IDLE  
            self.time_next_event[1] = 1.0e+30  
        else:  # If customers in queue
            self.num_in_q -= 1  # Decrement number of customers in queue
            delay = self.sim_time - self.time_arrival[1]  
            self.total_of_delays += delay  
            self.num_custs_delayed += 1  
            self.time_next_event[1] = self.sim_time + self.expon(self.mean_service)  

            # Update arrival times for remaining customers in queue
            for i in range(self.num_in_q):
                self.time_arrival[i] = self.time_arrival[i + 1]

    def update_time_avg_stats(self):  # Update time-average statistical accumulators
        time_since_last_event = self.sim_time - self.time_last_event

        # Update area under number in queue and server status
        self.area_num_in_q += (self.num_in_q * time_since_last_event)
        self.area_server_status += (self.server_status * time_since_last_event)
        self.time_last_event = self.sim_time 

    def report(self):  # Generate simulation report
        with open("output.txt", 'w') as outfile:
            outfile.write(
                f"Single Server Queuing System\n\nMean inter-arrival time: {self.mean_interarrival}\nMean Service time: {self.mean_service}"
                f"\nNumber of Customers: {self.num_delays_required} ")
            outfile.write("\n\nAverage Delay in queue: {:.3f} minutes\n".format(self.total_of_delays / self.num_custs_delayed))
            outfile.write("Average number in queue: {:.3f}\n".format(self.area_num_in_q / self.sim_time))
            outfile.write("Server Utilization: {:.3f}\n ".format(self.area_server_status / self.sim_time))
            outfile.write("Time Simulation Ended: {:.3f} minutes\n".format(self.sim_time))

    def main(self):  # Main simulation function
        self.num_events = 2 
        # Read input parameters from file
        with open("input.txt", 'r') as infile:
            line = infile.read()

        # Parse input parameters
        listOfInputs = line.split()
        self.mean_interarrival = float(listOfInputs[0])
        self.mean_service = float(listOfInputs[1])
        self.num_delays_required = int(listOfInputs[2])

        # Write initial simulation details to output file
        with open("output.txt", 'w') as outfile:
            outfile.write(
                "Single server queueing system"
                f"Mean interarrival time {self.mean_interarrival} minutes\n\n"
                f"Mean service time {self.mean_service} minutes"
                f"Number of customers {self.num_delays_required}"
            )

        # Initialize the simulation
        self.initialize()
        
        # Run the simulation until the desired number of delays is reached
        while self.num_custs_delayed < self.num_delays_required:
            self.timing()
            self.update_time_avg_stats()
            if self.next_event_type == 1:
                self.arrive()  
            elif self.next_event_type == 2:
                self.depart()  

        # Generate simulation report
        self.report()

# Start of the program
print("Executing main function")
obj = SingleServer()  
obj.main()  
print("Finished testing main")  
