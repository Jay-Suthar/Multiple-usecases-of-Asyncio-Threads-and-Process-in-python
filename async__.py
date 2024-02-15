# import asyncio
#
#
# async def main():
#     print("Starting asynchronous tasks...")
#
#     task1 = asyncio.create_task(task1_function())
#     task2 = asyncio.create_task(task2_function())
#
#     await task1
#     await task2
#
#     print("All tasks completed.")
#
#
# async def task1_function():
#     print("Task 1 started.")
#     await asyncio.sleep(1)
#     print("Task 1 completed.")
#
#
# async def task2_function():
#     print("Task 2 started.")
#     await asyncio.sleep(1)
#     print("Task 2 completed.")
#
#
# asyncio.run(main())


# import asyncio
#
#
# async def func1():
#     print("Function 1 started..")
#     await asyncio.sleep(2)
#     print("Function 1 Ended")
#
#
# async def func2():
#     print("Function 2 started..")
#     await asyncio.sleep(3)
#     print("Function 2 Ended")
#
#
# async def func3():
#     print("Function 3 started..")
#     await asyncio.sleep(1)
#     print("Function 3 Ended")
#
#
# async def main():
#     L = await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )
#     print("Main Ended..")


# asyncio.run(main())
# Asynchronous programming allows only one part of a program to run at a specific time.

# Consider three functions in a Python program: fn1(), fn2(), and fn3().

# In asynchronous programming, if fn1() is not actively executing
# (e.g., it’s asleep, waiting, or has completed its task), it won’t block the entire program.

# Instead, the program optimizes CPU time by allowing other functions (e.g., fn2())
# to execute while fn1() is inactive.

# Only when fn2() finishes or sleeps, the third function, fn3(), starts executing.

# This concept of asynchronous programming ensures that one task is performed at a time,
# and other tasks can proceed independently.


# import asyncio
# from datetime import datetime

# async def async_sleep(num):
#     print(f"Sleeping {num} seconds.")
#     await asyncio.sleep(num)


# async def main():
#     start = datetime.now()

#     coro_objs = []
#     for i in range(1, 4):
#         coro_objs.append(async_sleep(i))

#     await asyncio.gather(*coro_objs)

#     duration = datetime.now() - start
#     print(f"Took {duration.total_seconds():.2f} seconds.")

# asyncio.run(main())

#
# import asyncio
# from datetime import datetime
#
#
# async def async_sleep(num):
#     print(f"Sleeping {num} seconds.")
#     await asyncio.sleep(num)
#
#
# async def main():
#     start = datetime.now()
#
#     for i in range(1, 4):
#         await async_sleep(i)
#
#     duration = datetime.now() - start
#     print(f"Took {duration.total_seconds():.2f} seconds.")
#
#
# asyncio.run(main())


# example-1 (basic)
# import asyncio

# async def foo():
#     await asyncio.sleep(2)
#     print("Hello from foo!")

# async def bar():
#     await asyncio.sleep(1)
#     print("Hello from bar!")

# async def main():
#     task1 = asyncio.create_task(foo())
#     task2 = asyncio.create_task(bar())
#     await task1
#     await task2

# asyncio.run(main())


# example-2 (This example demonstrates how to fetch multiple
# URLs concurrently using asyncio and await.
# The fetch_url function makes asynchronous HTTP requests,
# and we use asyncio.gather to collect the results in parallel.)
# import asyncio
# import aiohttp
# from datetime import datetime
#
#
# async def fetch_url(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()
#
#
# async def main():
#     start = datetime.now()
#     urls = ["https://example.com", "https://python.org", "https://google.com"]
#     tasks = [fetch_url(url) for url in urls]
#     results = await asyncio.gather(*tasks)
#     for url, content in zip(urls, results):
#         print(f"Fetched {len(content)} bytes from {url}")
#
#     duration = datetime.now() - start
#     print(f"Took {duration.total_seconds():.2f} seconds.")


# asyncio.run(main())

# import time
# import asyncio
# import requests
#
#
# async def function1():
#     print("func 1")
#     URL = "https://pixewall.com/wp-content/uploads/2023/04/Night-Sky-Clouds-Sunset-Scenery-4k-Wallpapers-scaled.jpg"
#     response = requests.get(URL)
#     open("instagram.ico", "wb").write(response.content)
#
#     return "Jay"
#
#
# async def function2():
#     print("func 2")
#     URL = "https://wallpapers.com/images/featured/4k-nature-ztbad1qj8vdjqe0p.jpg"
#     response = requests.get(URL)
#     open("instagram2.jpg", "wb").write(response.content)
#
#     return "Suthar"
#
#
# async def function3():
#     print("func 3")
#     URL = "https://pixewall.com/wp-content/uploads/2023/03/4k-Cityscape-Desktop-Wallpaper.png"
#     response = requests.get(URL)
#     open("instagram3.ico", "wb").write(response.content)
#
#     return "GLSDJGLJ"
#
#
# async def main():
# await function1()
# await function2()
# await function3()
# return 3
# L = await asyncio.gather(
#     function1(),
#     function2(),
#     function3(),
# )
# print(L)
# task = asyncio.create_task(function1())
# # await function1()
# await function2()
# await function3()
#
# asyncio.run(main())


# Example-3 (using asyncio.wait_for())
# we use asyncio.wait_for to set a timeout for the slow_operation.
# If it takes longer than 3 seconds, it raises a TimeoutError.
# import asyncio
# async def slow_operation():
#     await asyncio.sleep(5)
#     return "Operation complete!"
# async def main():
#     try:
#         result = await asyncio.wait_for(slow_operation(), timeout=3)
#         print(result)
#     except asyncio.TimeoutError:
#         print("Operation timed out!")
# asyncio.run(main())


# Example-4 (error handling)
# async def fetch_data():
#     try:
#         await asyncio.sleep(2)
#         result = 10 / 0  # This raises a ZeroDivisionError
#     except ZeroDivisionError as e:
#         return f"Error: {e}"
#     return "Data fetched successfully!"
# async def main():
#     result = await fetch_data()
#     print(result)
# asyncio.run(main())


# Example-5 (concurrent i/o opr.)
# tasks are executed concurrently, and the completion order may differ.
# async def io_operation(task_name, delay):
#     await asyncio.sleep(delay)
#     print(f"Task {task_name} completed")
# async def main():
#     tasks = [
#         io_operation("A", 3),
#         io_operation("B", 1),
#         io_operation("C", 2),
#     ]
#     await asyncio.gather(*tasks)
# asyncio.run(main())


# Example-6 (Running Coroutines in Parallel)
# async def square(x):
#     await asyncio.sleep(1)
#     return x * x
# async def cube(x):
#     await asyncio.sleep(1)
#     return x * x * x
# async def main():
#     start = datetime.now()
#     results = await asyncio.gather(square(2), cube(3))
#     print("Square:", results[0])
#     print("Cube:", results[1])
#     duration = datetime.now() - start
#     print(f"Took {duration.total_seconds():.2f} seconds.")
# asyncio.run(main())


# Example-7 (Parallel Execution with asyncio.as_completed())
# asyncio.as_completed allows you to iterate over completed tasks as they finish
# we print the results as they become available, not necessarily in the order they started.
# async def foo():
#     await asyncio.sleep(2)
#     return "Foo done"
#
# async def bar():
#     await asyncio.sleep(1)
#     return "Bar done"
#
# async def main():
#     start = datetime.now()
#     tasks = [foo(), bar()]
#     for result in asyncio.as_completed(tasks):
#         print(await result)
#     duration = datetime.now() - start
#     print(f"Took {duration.total_seconds():.2f} seconds.")
#
# asyncio.run(main())


# Example-8 (real use case)
# consider we want to extract some information from few web pages concurrently(web scraping)
# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# async def fetch_and_parse_url(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             page_content = await response.text()
#             soup = BeautifulSoup(page_content, "html.parser")
#             title = soup.title.string
#             return f"Title of {url}: {title}"
# async def main():
#     urls = [
#         "https://example.com",
#         "https://python.org",
#         "https://google.com",
#     ]
#     tasks = [fetch_and_parse_url(url) for url in urls]
#     results = await asyncio.gather(*tasks)
#     for result in results:
#         print(result)
# asyncio.run(main())


# Misc. Examples(use case in LLM models)
# import asyncio
# from openai import AsyncOpenAI
# The openai library provides an asynchronous client AsyncOpenAI.
# Here is an example on how to run multiple requests onto
# the chat completions API using asyncio.as_completed():
# async def chat_completion(client, prompt, **kwargs):
#     messages = [{"role": "user", "content": prompt}]
#     return await client.chat.completions.create(
#         messages=messages,
#         **kwargs
#     )
#
# async def run_chat_completions(client, prompts: str, **kwargs):
#     calls = [chat_completion(client, prompt, **kwargs) for prompt in prompts]
#     for completed_task in asyncio.as_completed(calls):
#         response = await completed_task
#         print(response)
#
# async def main(prompts, **kwargs):
#     async with AsyncOpenAI() as client:
#         await run_chat_completions(client, prompts, **kwargs)
#
# prompts = ["Hello"] * 10
# asyncio.run(main(prompts, model="gpt-3.5-turbo-1106"))
# In the above example, the prompt “Hello” is sent 10 times to the GPT-3.5 model
# and each response is printed as it gets completed.
# This is significantly faster than running them sequentially.


'''MORE USE-CASES ->'''
"""1) Web Servers and Web Applications: Asyncio is commonly used in web servers 
and web frameworks to handle concurrent requests efficiently. 
Web servers built with asyncio, such as FastAPI and Sanic, 
can handle thousands of simultaneous connections without 
the need for multiple threads or processes."""

# from fastapi import FastAPI
# import asyncio
#
# app = FastAPI()
#
#
# @app.get("/")
# async def read_root():
#     await asyncio.sleep(1)
#     return {"message": "Hello, world!"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     await asyncio.sleep(1)
#     return {"item_id": item_id, "message": "Item retrieved"}
#
#
# import uvicorn
#
# uvicorn.run(app, host="127.0.0.1", port=80)

'''2) Networking: Asyncio is ideal for networking applications 
where you need to manage multiple connections simultaneously. 
It’s commonly used in chat servers, IoT applications, and network
monitoring tools.'''

# import asyncio
#
# # Dictionary to store connected clients
# connected_clients = {}
#
# # Handle incoming client connections
# async def handle_client(reader, writer):
#     client_address = writer.get_extra_info('peername')
#     print(f"New client connected: {client_address}")
#
#     # Add client to the connected_clients dictionary
#     connected_clients[client_address] = writer
#
#     try:
#         while True:
#             # Read data from the client
#             data = await reader.read(100)
#             if not data:
#                 break
#
#             # Echo the received data back to the client
#             print(f"Received data from {client_address}: {data.decode()}")
#             writer.write(data)
#             await writer.drain()
#     except asyncio.CancelledError:
#         pass
#     finally:
#         # Close the connection
#         writer.close()
#         del connected_clients[client_address]
#         print(f"Connection closed with {client_address}")
#
# async def main():
#     # Create a TCP server
#     server = await asyncio.start_server(
#         handle_client, '127.0.0.1', 8888)
#
#     # Print server address
#     print(f"Server listening on {server.sockets[0].getsockname()}")
#
#     # Serve clients indefinitely
#     async with server:
#         await server.serve_forever()
#
# # Run the main coroutine
# asyncio.run(main())
'''This example demonstrates how asyncio can be used to manage multiple 
client connections efficiently in a networking application. Each client 
connection is handled concurrently, allowing the server to scale and
 handle multiple connections simultaneously.'''

'''3) Data Streaming: Consider a scenario where you want to process a 
continuous stream of sensor data and perform real-time analysis. 
Asyncio can help you efficiently handle this data streaming task. 
Below is a simplified example of using Asyncio to simulate the processing of sensor data.'''
# import asyncio
# import random
#
#
# async def process_sensor_data(sensor_id):
#     while True:
#         data = random.randint(0, 100)  # Simulate sensor data
#         print(f"Sensor {sensor_id} data: {data}")
#         # Perform real-time analysis here
#         await asyncio.sleep(1)  # Simulate data streaming interval
#
#
# async def main():
#     sensor_count = 3
#     tasks = []
#     for sensor_id in range(sensor_count):
#         task = asyncio.create_task(process_sensor_data(sensor_id))
#         tasks.append(task)
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())
'''In this example, we create multiple asynchronous tasks (coroutines) 
to process data from different sensors concurrently. Each coroutine 
simulates sensor data and performs real-time analysis. The await 
asyncio.sleep(1) line simulates the data streaming interval.'''

'''4)GUI Applications Example: Asyncio can also be used to create 
responsive graphical user interfaces (GUIs) by allowing non-blocking 
interactions between the user and the application. Here’s a simple 
example using the asyncio library alongside tkinter, 
a popular GUI library for Python:'''
# import asyncio
# import tkinter as tk
#
#
# async def update_label(label):
#     while True:
#         label.config(text="Processing...")
#         await asyncio.sleep(1)  # Simulate a time-consuming task
#         label.config(text="Ready")
#         await asyncio.sleep(1)
#
#
# async def main():
#     root = tk.Tk()
#     root.title("Asyncio GUI Example")
#     label = tk.Label(root, text="Ready")
#     label.pack()
#     asyncio.create_task(update_label(label))
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

'''In this example, we create a simple GUI application using tkinter, 
and an asyncio task updates a label with "Processing..." and "Ready" 
messages alternately. The GUI remains responsive even when the 
update_label coroutine is executing, demonstrating the 
non-blocking nature of Asyncio in a GUI context.'''