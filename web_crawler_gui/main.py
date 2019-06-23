import threading
from queue import Queue
from web_spider import spider
from domain_extraction import *
from basic_methods import *

def get_queueobj(queue):
    return queue
# Create worker threads (will die when main exits)
# def create_workers(NUMBER_OF_THREADS):
#     for _ in range(NUMBER_OF_THREADS):
#         t = threading.Thread(target=work)
#         t.daemon = True
#         t.start()
#
#
# # Do the next job in the queue
# def work():
#     while True:
#         url = main_page.queobj.get()
#         spider.crawl_page(threading.current_thread().name, url)
#         main_page.queobj.task_done()
#
#
# # Each queued link is a new job
# def create_jobs(NUMBER_OF_THREADS, QUEUE_FILE):
#     for link in file_to_set(QUEUE_FILE):
#         main_page.queobj.put(link)
#         main_page.queobj.join()
#     crawl(NUMBER_OF_THREADS, QUEUE_FILE)
#
#
# # Check if there are items in the queue, if so crawl them
# def crawl(NUMBER_OF_THREADS, QUEUE_FILE):
#     queued_links = file_to_set(QUEUE_FILE)
#     if len(queued_links) > 0:
#         print(str(len(queued_links)) + ' links in the queue')
#         create_jobs(NUMBER_OF_THREADS, QUEUE_FILE)


