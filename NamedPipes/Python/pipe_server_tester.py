import os
import time

number_of_bytes_expected_to_be_read = 2

PIPE_REQUEST_NAME = "pipe_request"
PIPE_RESPONSE_NAME = "pipe_response"

def initialize_pipes():
    """Create pipe_request and pipe_response """
    
    """Crete pipe to read"""
    create_pipe(PIPE_REQUEST_NAME)
    
    """Create pipe to write"""
    create_pipe(PIPE_RESPONSE_NAME)

    open_pipes()

def create_pipe(pipe_name):
    """Delete pipe before create"""
    if os.path.exists(pipe_name):
        os.unlink(pipe_name)

    os.mkfifo(pipe_name)

def open_pipes():
    pipe_response = os.open(PIPE_RESPONSE_NAME, os.O_WRONLY)
    pipe_request = os.open(PIPE_REQUEST_NAME, os.O_RDONLY)

    start_pipe_read_and_write(pipe_response, pipe_request)


def start_pipe_read_and_write(pipe_response, pipe_request):
    """"First open pipe_response and then pipe_request, as in the other process pipe_response will be the first being opened"""

    count = 0

    while True:
        
        count = count + 1
        
        if not write_on_pipe(pipe_response, count):
            break
        
        time.sleep(1)
        
        if not read_from_pipe(pipe_request):
            break



def write_on_pipe(pipe_response, count):
    count_str = str(count)
    payload = bytearray()
    payload.append(len(count_str))
    payload.append(count)

    print("[Python server process] Payload to be sent: ", payload)

    result = os.write(pipe_response, payload)

    if result is -1:
        return False

    return True


def read_from_pipe(pipe_request):
    
    result = os.read(pipe_request, number_of_bytes_expected_to_be_read)

    if len(result) is not number_of_bytes_expected_to_be_read:
        return False

    print("[Python server process] Read result", result)

    return True
    

initialize_pipes()











