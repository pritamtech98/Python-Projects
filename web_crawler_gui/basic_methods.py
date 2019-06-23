import os


def create_project_dir(directory_name):

    if not os.path.exists(directory_name):
        print("creating project: ", directory_name)
        os.makedirs(directory_name)


def create_project_files(project_name, base_url, queue_file, crawl_file):
    queue = os.path.join(project_name, queue_file)
    crawled = os.path.join(project_name, crawl_file)
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(file_path, content):
    f=open(file_path, 'w')
    f.write(content)


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def append_file(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content + '\n')


def set_to_file(links, file_path):
    delete_file(file_path)
    for el in sorted(links):
        append_file(file_path, el)

def delete_file(file_path):
    open(file_path, 'w').close()
