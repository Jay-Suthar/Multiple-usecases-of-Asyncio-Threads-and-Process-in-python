'''use cases'''

'''1) Parallel Processing: Processes can be used to execute tasks concurrently, 
leveraging the available CPU cores for parallel execution. This is particularly 
useful for CPU-bound tasks such as mathematical computations, data processing, 
and simulations.'''
import concurrent.futures
import requests
import multiprocessing
#
#
#
# def downloadFile(url, name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")
#
# def square(x):
#     return x * x

#
# def main1():
#     url = "https://picsum.photos/2000/3000"
#     pros = []
#     for i in range(10):
#         p = multiprocessing.Process(target=downloadFile, args=[url, i])
#         p.start()
#         pros.append(p)
#
#     for p in pros:
#         p.join()
#
# def main2():
#     pros = []
#     numbers = [1, 2, 3, 4, 5]
#     for i in numbers:
#         p = multiprocessing.Process(target=square, args=[i])
#         p.start()
#         pros.append(p)
#
#     for p in pros:
#         p.join()
#
# if __name__ == "__main__":
#     main2()

'''using .pool is used for creating and managing a pool 
of worker processes that can execute tasks in parallel. 
This class simplifies the process of parallelizing tasks 
and distributing them among multiple processes.'''

# if __name__=='__main__':
#
#   with multiprocessing.Pool(processes=4) as pool:
#     results = pool.map(square, [2,5,3,2,1,7,8,5,6,2,2,3])
#
#     print(results)

'''using .Queue which is used to facilitate communication and data 
exchange among different processes in a multiprocessing program.'''
# import multiprocessing
# import time
#
# #defining our function we want to apply multiprocessing on
# #01 the producer function to add elements in the queue
# def producer(q):
#   for item in range(5):
#     q.put(item)
#     print(f"Produced:  {item}")
#
#
# #02 consumer function to get elements from the queue
# def consumer(q):
#   while True:
#     item = q.get()
#     if item is None:
#       break
#     print(f"Consumed:  {item}")
#
#
# if __name__ == "__main__":
#   #creating a multiprocessing queue
#   q = multiprocessing.Queue()
#
#   #creating the producer and consumer processes
#   producer_process = multiprocessing.Process(target=producer, args=(q,))
#   consumer_process = multiprocessing.Process(target=consumer, args=(q,))
#
#   #starting the processes
#   producer_process.start()
#   consumer_process.start()
#
#   #finish the producer, signal the consumer to exit
#   producer_process.join()
#   q.put(None) #signaling the consumer about no more data in the queue
#   consumer_process.join()

'''using .pipe allow interprocess communication by initiating 
a connection between the processes where one process writes 
to the pipe and other process reads from the pipe. '''

# def send_message(conn):
#     conn.send("Hello from the sender process!")
#
# def receive_message(conn):
#     print(conn.recv())
#
# if __name__ == "__main__":
#   conn1, conn2 = multiprocessing.Pipe()
#   p1 = multiprocessing.Process(target=send_message, args=(conn1,))
#   p2 = multiprocessing.Process(target=receive_message,args=(conn2,))
#   p1.start()
#   p2.start()
#   p1.join()
#   p2.join()


'''2) Scalability: Processes can improve the scalability of 
applications by distributing workload across multiple processes, 
allowing them to handle higher loads and concurrent requests 
efficiently. This is particularly useful for web servers, 
APIs, and other server-side applications.'''


'''3) Distributed Computing: A Task can be distributed among 
multiple machines connected over a network and it comes in 
handy when a large amount of computing power is required 
e.g big data analysis or deep learning.'''
# def process_data(data_chunk):
#     # Process data and return result
#     return [x * 2 for x in data_chunk]
#
# def process_wrapper(queue, data_chunk):
#     result = process_data(data_chunk)
#     queue.put(result)
#
# if __name__ == "__main__":
#     # Define the data to be processed
#     data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     # Split the data into chunks for parallel processing
#     chunk_size = len(data) // multiprocessing.cpu_count()
#     data_chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
#
#     # Create and start processes for each data chunk
#     processes = []
#     results = multiprocessing.Queue()
#     for chunk in data_chunks:
#         process = multiprocessing.Process(target=process_wrapper, args=(results, chunk))
#         process.start()
#         processes.append(process)
#
#     # Wait for all processes to finish
#     for process in processes:
#         process.join()
#
#     # Gather results from the queue
#     processed_data = []
#     while not results.empty():
#         processed_data.extend(results.get())
#
#     # Combine processed data
#     final_result = sum(processed_data)
#
#     print("Final Result:", final_result)


'''4) Resource Isolation: Processes provide isolation between different components 
of an application, ensuring that issues in one process do not affect others. 
This is valuable for building robust and resilient systems, especially in 
scenarios where failure of one component should not impact the entire system.
'''
# import os
# def process_task():
#     pid = os.getpid()
#     print(f"Process {pid} performing task.")
#
# if __name__ == "__main__":
#     processes = []
#     for _ in range(3):
#         process = multiprocessing.Process(target=process_task)
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     print("All processes have completed their tasks.")



'''5) Fault Tolerance: By running critical components of an 
application as separate processes, fault tolerance can be improved. 
If one process fails or crashes due to an error, other processes 
can continue running, ensuring uninterrupted operation of the system.'''

# import time
# import random
#
# def critical_component():
#     # Simulate critical component execution
#     while True:
#         try:
#             # Simulate some critical operation
#             result = 100 / random.randint(0, 1)
#             print(f"Critical component result: {result}")
#             return
#         except Exception as e:
#             print(f"Critical component encountered an error: {e}")
#             # Sleep for a while before retrying
#             time.sleep(1)
#
# if __name__ == "__main__":
#     # Create a separate process for the critical component
#     process = multiprocessing.Process(target=critical_component)
#     process.start()
#
#     # Main process continues to execute other tasks
#     while True:
#         # Simulate other tasks
#         print("Main process executing other tasks...")
#         time.sleep(2)


'''Why to use process/multiprocessing'''

'''
CPU-Bound Tasks: Multiprocessing is suitable for CPU-bound 
tasks that require intensive computation, as it allows multiple 
processes to execute on different CPU cores concurrently, leveraging 
parallelism to improve performance.

Parallel Processing: Multiprocessing enables parallel execution of 
multiple tasks on multicore processors, making it ideal for tasks that 
can be divided into independent subtasks that can execute simultaneously.

GIL Avoidance: In Python, multiprocessing can be used to bypass the 
Global Interpreter Lock (GIL), which restricts the execution of Python
bytecode in multiple threads. This allows for true parallelism in CPU-bound tasks.

Distributed Computing: Multiprocessing can facilitate distributed 
computing by running multiple processes across multiple nodes or 
machines, enabling scalable and high-performance computing for 
large-scale data processing tasks.

Fault Isolation: Multiprocessing provides fault isolation between processes, 
as each process has its own memory space. This helps prevent issues such 
as memory leaks or crashes in one process from affecting others.

Resource Intensive Applications: Multiprocessing is suitable for 
resource-intensive applications that require efficient utilization of 
CPU resources, such as scientific computing, image processing, or 
machine learning tasks.

Task Parallelism: In applications with multiple independent tasks, 
multiprocessing can be used to execute these tasks concurrently, 
reducing overall execution time and improving system throughput.

Process Pooling: Multiprocessing allows for the creation of process pools, 
where a pool of worker processes can be reused to execute multiple tasks, 
reducing the overhead of process creation and termination.

Scalability: Multiprocessing can improve the scalability of applications 
by distributing workload across multiple processes, enabling them to handle 
higher loads and concurrent requests efficiently.

External Libraries: Some external libraries or frameworks are designed to 
leverage multiprocessing for parallel execution, such as joblib for 
parallel computing in Python or Apache Spark for distributed data processing.
'''



'''Why to not use process/multiprocessing'''

'''
I/O-Bound Tasks: Multiprocessing may not be suitable for I/O-bound tasks 
that spend most of their time waiting for I/O operations to complete, as 
the overhead of inter-process communication (IPC) can outweigh the benefits 
of parallelism.

High process creation cost: Creating new processes incurs a significant 
overhead compared to threads. Each process requires its own memory space, 
resources, and initialization, leading to increased startup time and 
resource consumption.

Lack of shared memory: Unlike threads, processes do not share memory by default. 
Sharing data between processes often involves serialization and deserialization, 
which can introduce additional complexity and overhead.

Serialization challenges: Passing data between processes typically requires 
serialization, which involves converting complex data structures into a format 
that can be transmitted across process boundaries. Serialization and deserialization 
operations can be computationally expensive and may not always be straightforward 
for complex data types or objects.

Limited communication options: Inter-process communication (IPC) mechanisms such 
as pipes, queues, and shared memory are used to exchange data between processes. 
However, these mechanisms may have limitations in terms of throughput, latency, 
and complexity, especially when dealing with large volumes of data or real-time 
communication requirements.

Scalability concerns: While multiprocessing can leverage multiple CPU cores and 
provide parallel execution of tasks, the scalability of multiprocessing may be 
limited by the overhead of process creation and management. Excessive process 
creation can lead to resource contention, increased memory consumption, and 
degraded performance, particularly on systems with limited resources.

Deployment considerations: Multiprocessing may not be suitable for all deployment 
environments, especially in constrained environments like serverless platforms or 
certain cloud environments where process creation and resource allocation are restricted.
'''