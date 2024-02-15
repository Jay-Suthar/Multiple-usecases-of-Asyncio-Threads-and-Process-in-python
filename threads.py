# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

'''basic example using Threads and ThreadPoolExecutor'''
# Indicates some task being done
# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
#     # return seconds
#
#
# def main():
#     time1 = time.perf_counter()
#     # Normal Code
#     # func(4)
#     # func(2)
#     # func(1)
#
#     # Same code using Threads
#     t1 = threading.Thread(target=func, args=[4])
#     t2 = threading.Thread(target=func, args=[2])
#     t3 = threading.Thread(target=func, args=[1])
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#     # Calculating Time
#     time2 = time.perf_counter()
#     print(time2 - time1)
#
# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         time1 = time.perf_counter()
#         # future1 = executor.submit(func, 3)
#         # future2 = executor.submit(func, 2)
#         # future3 = executor.submit(func, 4)
#         # print(future1.result())
#         # print(future2.result())
#         # print(future3.result())
#         l = [3, 5, 1, 2]
#         results = executor.map(func, l)
#         for result in results:
#             print(result)
#
#         time2 = time.perf_counter()
#         print(time2 - time1)
#
# main()
# poolingDemo()




'''Real use-cases of threads:

1) User Interface Responsiveness: In graphical user interface (GUI) applications, 
you can use threads to perform time-consuming tasks such as loading data from a 
database or processing large files without blocking the main UI thread. This 
ensures that the UI remains responsive to user interactions.'''

# import tkinter as tk
# import threading
# import time
#
#
# def time_consuming_task():
#     time.sleep(5)  # Simulate time-consuming task
#     print("Task completed")
#
#
# def start_task():
#     threading.Thread(target=time_consuming_task).start()
#
#
# root = tk.Tk()
# button = tk.Button(root, text="Start Task", command=start_task)
# button.pack()
# root.mainloop()



'''2) Multithreaded Servers: In server applications, multithreading 
allows the server to handle multiple client connections concurrently. 
Each client connection can be assigned to a separate thread, enabling 
the server to serve multiple clients simultaneously'''

# import socket
# import threading
#
#
# def handle_client(connection, address):
#     # Handle client request
#     print(f"Connection from {address}")
#     data = connection.recv(1024)
#     connection.sendall(data)
#     connection.close()
#
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("localhost", 8888))
# server.listen(5)
#
# while True:
#     connection, address = server.accept()
#     threading.Thread(target=handle_client, args=(connection, address)).start()



'''3)Parallel Processing: Tasks that can be divided into smaller 
independent subtasks can benefit from parallel processing using 
threads. For example, in data processing applications, you can 
use multiple threads to process different parts of a dataset 
concurrently, speeding up overall processing time.'''



'''4)Background Tasks: Threads are commonly used for running background 
tasks such as periodic data updates, logging, or monitoring system 
resources. These tasks can run concurrently with the main application 
logic without affecting its performance.'''
# import threading
# import time
#
#
# def background_task():
#     while True:
#         print("Background task is running")
#         time.sleep(3)
#
#
# threading.Thread(target=background_task, daemon=True).start()
#
# time.sleep(7)
# print("Main program continues to execute")



'''5) I/O-Bound Operations: Threads are well-suited for I/O-bound 
operations such as reading from or writing to files, network communication, 
or database queries. While one thread is waiting for I/O operations to complete, 
other threads can continue executing.'''
# import threading
# import requests
#
#
# def fetch_url(url):
#     response = requests.get(url)
#     print(f"Response from {url}: {response.status_code}")
#
#
# urls = ["https://www.example.com", "https://www.google.com", "https://www.github.com"]
# threads = []
#
# for url in urls:
#     thread = threading.Thread(target=fetch_url, args=(url,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()



'''6)Resource Pooling: Threads can be used to manage resource pools 
efficiently, such as database connections, network connections, or file handles.
Each thread can request a resource from the pool when needed and 
release it when finished, allowing for better resource utilization and scalability.'''

# import threading
# import queue
#
# class ResourcePool:
#     def __init__(self, max_resources):
#         self.max_resources = max_resources
#         self.available_resources = queue.Queue(maxsize=max_resources)
#         for _ in range(max_resources):
#             self.available_resources.put(object())
#
#     def acquire(self):
#         return self.available_resources.get()
#
#     def release(self, resource):
#         self.available_resources.put(resource)
#
# def worker(pool, thread_id):
#     resource = pool.acquire()
#     print(f"Thread {thread_id} acquired resource: {resource}")
#     # Do work with resource
#     pool.release(resource)
#     print(f"Thread {thread_id} released resource: {resource}")
#
# pool = ResourcePool(max_resources=3)
# threads = []
#
# for i in range(5):
#     thread = threading.Thread(target=worker, args=(pool, i))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()



'''7)Caching and Memoization: Threads can be used to implement 
caching mechanisms or memoization for expensive computations 
or data retrieval operations. Multiple threads can concurrently 
access and update a shared cache, reducing the time required to 
compute or retrieve data for subsequent requests.'''
# import threading
#
# class ThreadSafeDict(dict):
#     def __init__(self, *args, **kwargs):
#         self.lock = threading.Lock()
#         super().__init__(*args, **kwargs)
#
#     def __getitem__(self, key):
#         with self.lock:
#             return super().__getitem__(key)
#
#     def __setitem__(self, key, value):
#         with self.lock:
#             return super().__setitem__(key, value)
#
# class Memoize:
#     def __init__(self, func):
#         self.func = func
#         self.cache = ThreadSafeDict()
#
#     def __call__(self, *args):
#         if args not in self.cache:
#             self.cache[args] = self.func(*args)
#         return self.cache[args]
#
# @Memoize
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# def compute_fibonacci(n):
#     result = fibonacci(n)
#     print(f"Fibonacci({n}) = {result}")
#
# threads = []
# for i in range(10):
#     thread = threading.Thread(target=compute_fibonacci, args=(i,))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()



'''8)Web Scraping and Crawling: Threads can be used for 
web scraping and crawling tasks, where multiple URLs or 
web pages need to be fetched and processed concurrently.
Each thread can handle a subset of URLs, fetching 
HTML content, parsing data, and extracting relevant information in parallel.'''

# import threading
# import requests
# from bs4 import BeautifulSoup
#
# def fetch_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
#
# def scrape_page(url):
#     html_content = fetch_url(url)
#     if html_content:
#         soup = BeautifulSoup(html_content, 'html.parser')
#         # Extract relevant information from the page
#         # For demonstration, let's print the page title
#         title = soup.title.text.strip()
#         print(f"Title of {url}: {title}")
#
# def crawl(urls):
#     threads = []
#     for url in urls:
#         thread = threading.Thread(target=scrape_page, args=(url,))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
# # List of URLs to scrape
# urls = [
#     'https://example.com/page1',
#     'https://example.com/page2',
#     'https://example.com/page3',
#     # Add more URLs as needed
# ]
#
# crawl(urls)



'''Why to use threads/multithreading?'''

'''
I/O-Bound Tasks: Multithreading is suitable for tasks that are I/O-bound, 
such as network requests, file I/O, or database operations. 
Threads can perform these tasks concurrently, allowing the CPU 
to handle other work while waiting for I/O operations to complete.

Responsive User Interfaces: In graphical user interface (GUI) 
applications, multithreading can be used to keep the user 
interface responsive while performing background tasks 
such as data processing or downloading files.

Concurrency: Multithreading is useful for achieving concurrency, where 
multiple tasks can make progress independently. This can improve overall 
system throughput and resource utilization.

Asynchronous Programming: Multithreading can be used for asynchronous 
programming paradigms, such as implementing event-driven architectures 
or handling multiple asynchronous events concurrently.

Parallelism: Multithreading enables parallel execution of multiple 
tasks on multicore processors, leading to performance improvements 
for CPU-bound tasks that can be parallelized.

Task Parallelism: In applications with multiple independent tasks, 
multithreading can be used to execute these tasks concurrently, 
reducing overall execution time.

Background Processing: Multithreading is suitable for background 
processing tasks, such as batch processing, data synchronization, 
or periodic tasks that run alongside the main application.

Real-Time Systems: In real-time systems where tasks must meet strict 
timing constraints, multithreading can be used to handle multiple tasks 
concurrently, ensuring timely execution.

Resource Sharing: Multithreading allows multiple threads to share 
resources such as memory or data structures efficiently, enabling 
collaboration between different parts of the application.

Scalability: Multithreading can improve the scalability of applications 
by allowing them to handle multiple concurrent requests or connections 
efficiently, making them suitable for server applications.
'''


'''Why to not use threads/multithreading?'''

'''
CPU-Bound Tasks: Multithreading may not be suitable for 
CPU-bound tasks that require intensive computation, as the 
overhead of thread management and context switching may outweigh 
the benefits of parallelism.

Global Interpreter Lock (GIL): In Python, the Global Interpreter 
Lock (GIL) can limit the effectiveness of multithreading for 
CPU-bound tasks, as it prevents multiple threads from executing 
Python bytecode concurrently.

I/O-bound tasks with blocking calls: If the tasks involve I/O operations 
that are inherently blocking (e.g., network requests, file I/O), using 
threads may not provide significant performance improvements due to Python's 
GIL. In such scenarios, asynchronous programming with libraries like asyncio
or using asynchronous I/O libraries (e.g., aiohttp for web requests) might be more appropriate.

Shared State: Multithreading can lead to race conditions and 
synchronization issues when multiple threads access shared state 
concurrently. In such cases, other concurrency models like multiprocessing 
or asynchronous programming may be more appropriate.

Compatibility with third-party libraries: Some third-party libraries may not 
be thread-safe or may not support concurrent execution within a multithreaded 
environment. Using threads with such libraries could lead to 
unpredictable behavior or errors.

Platform Limitations: Some platforms or environments may impose 
limitations on multithreading, such as restricted thread counts or 
lack of support for multithreading. In such cases, alternative 
concurrency models should be considered.

Resource Contention: Multithreading can lead to resource contention, 
where multiple threads compete for limited resources such as CPU time, 
memory, or I/O bandwidth. This can degrade performance and lead to 
unpredictable behavior.

Thread Safety: Writing thread-safe code can be challenging, especially 
when dealing with shared mutable state. In scenarios where ensuring 
thread safety is difficult or impractical, multithreading should be avoided.


'''


