import logging
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.WARNING)
def show(*msgs):
    all_msgs = ""
    for msg in msgs:
        all_msgs += str(msg)

    logging.debug(all_msgs)

def error(*msgs):
    all_msgs = ""
    for msg in msgs:
        all_msgs += str(msg)
    logging.error(all_msgs)