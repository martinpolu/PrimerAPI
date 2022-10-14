from servidor import start_server
from multiprocessing import cpu_count, freeze_support
from RequestAPI import GenerateRequest

if __name__ == "__main__":
    freeze_support()  # Needed for pyinstaller for multiprocessing on WindowsOS
    num_workers = int(cpu_count() * 0.75)
    start_server(num_workers=num_workers)
    GenerateRequest()

