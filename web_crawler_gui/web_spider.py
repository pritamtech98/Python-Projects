from basic_methods import *
from linkfinder import link_finder
from urllib.request import *
from domain_extraction import *

class spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name, queue_file, crawl_file):
        spider.project_name=project_name
        spider.base_url=base_url
        spider.domain_name=domain_name
        spider.queue_file=spider.project_name+'/'+queue_file
        spider.crawled_file=spider.project_name+'/'+crawl_file
        self.boot(queue_file, crawl_file)
        self.crawl_page('first spider', spider.base_url)

    @staticmethod
    def boot(queue_file, crawl_file):
        create_project_dir(spider.project_name)
        create_project_files(spider.project_name, spider.base_url, queue_file, crawl_file)
        spider.queue=file_to_set(spider.queue_file)
        spider.crawled=file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, base_url):
        if base_url not in spider.crawled:
            print(thread_name+"  is running:  "+base_url)
            print('Queue '+str(len(spider.queue))+'  |  Crawled '+str(len(spider.crawled)))
            spider.add_links_to_queue(spider.gather_links(base_url))
            spider.queue.remove(base_url)
            spider.crawled.add(base_url)
            spider.update_files()


    @staticmethod
    def gather_links(page_url):
        html_string=''
        try:
            response=urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):  #checks whether our url contains text file or any html file
                html_bytes=response.read()   #if our url contains text file, then it will read the entire text, otherwise if it is html file, it will read the whole html file in bytes
                html_string=html_bytes.decode('utf-8')
            finder=link_finder(spider.base_url, page_url)
            finder.feed(html_string)

        except Exception:
            print("Error: cannot crawl page, may be link is expired")
            return set()
        return finder.return_links()

    @staticmethod
    def add_links_to_queue(links):
        for el in links:
            if(el in spider.queue):
                continue
            if(el in spider.crawled):
                continue
            if(spider.domain_name != get_main_domain_name(el)):
                continue
            spider.queue.add(el)

    @staticmethod
    def update_files():
        set_to_file(spider.queue, spider.queue_file)
        set_to_file(spider.crawled, spider.crawled_file)