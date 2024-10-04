from queue_dsa import Queue

class PrinterQueue:
    """
    Task: Implement a Queue to Simulate a Printer's Job Queue
    Objective: Simulate how jobs are handled in a printer queue. 
    The queue should process jobs in the order they are added.
    """
    def __init__(self):
        self.queue = Queue()

    def add_job(self, job_name):
        self.queue.enqueue(job_name)

    def process_job(self):
        if self.queue.is_empty():
            print('No jobs in the queue')
        else:
            print(f'Processing {self.queue.peek()}')
            return self.queue.dequeue()
    

if __name__ == '__main__':
    queue = PrinterQueue()
    queue.add_job("Job1")
    queue.add_job("Job2")
    queue.process_job()  # Output: Processing Job1
    queue.process_job()  # Output: Processing Job2
    queue.process_job()  # Output: No jobs in the queue

