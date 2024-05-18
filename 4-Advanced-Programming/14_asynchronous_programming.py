import asyncio

'''
create an async function
'''
# async def print_values(values, delay):
#     for item in values:
#         print(item)
#         await asyncio.sleep(delay)

# async def main():
#     task1 = asyncio.create_task(print_values([1, 3, 5], 0.2))
#     task2 = asyncio.create_task(print_values([2, 4], 0.3))

#     await task1
#     await task2

# asyncio.run(main())  # 1 2 3 4 5

'''
gather coroutines
'''
# async def printing(values, delay):
#     for item in values:
#         print(item)
#         await asyncio.sleep(delay)
#     return delay

# async def main2():
#     values = await asyncio.gather(printing([1, 3, 5], 0.2),
#                                   printing([2, 4], 0.3))
#     print(values)

# asyncio.run(main2())  # 1 2 3 4 5  [0.2, 0.3]

'''
practical example of asynchronous programming
'''
# async def fetch_data():
#     print("Start fetching")
#     await asyncio.sleep(2)
#     print("Done fetching")
#     return [1, 2, 3, 4, 5, 6]

# async def run_algorithm():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(0.5)

# async def main3():
#     data = await asyncio.gather(fetch_data(), run_algorithm())

# asyncio.run(main3())

'''
asynchronous generator
'''
# async def gen(n):
#     for i in range(n):
#         yield i
#         await asyncio.sleep(0.5)

# async def main4():
#     async for i in gen(10):
#         print(i)

# asyncio.run(main4())  # 0 1 2 3 4 5 6 7 8 9

'''
Write a function named "add_one" that accepts a coroutine as a mandatory parameter then calls the coroutine
and returns the coroutines return value plus one
'''

async def add_one(coroutine):
    return_value = await coroutine()
    return return_value + 1

'''
Schedule the existing function to run multiple times such that lst = [1, 3, 2, 4, 6, 5] at the end of the program.
Run all your functions calls concurrently using asyncio. Your code should not take longer than 1 second to run.
'''

# async def append_two_values(lst, value1, value2):
#     lst.append(value1)
#     await asyncio.sleep(0.5)
#     lst.append(value2)
#
# lst = []
#
# async def main(lst):
#     futures = [append_two_values(lst, 1, 4), append_two_values(lst, 3, 6), append_two_values(lst, 2, 5)]
#     await asyncio.gather(*futures)
#
# asyncio.run(main(lst))



