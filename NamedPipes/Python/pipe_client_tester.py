import os

PIPE_REQUEST_NAME = "pipe_request"
PIPE_RESPONSE_NAME = "pipe_response"

def open_pipes():
    """Open pipe_request and pipe_response """
    pipe_response = os.open(PIPE_RESPONSE_NAME, os.O_RDONLY)
    pipe_request = os.open(PIPE_REQUEST_NAME, os.O_WRONLY)

    start_pipe_read_and_write(pipe_response, pipe_request)


def start_pipe_read_and_write(pipe_response, pipe_request):
    """"First open pipe_response and then pipe_request, as in the other process pipe_response will be the first being opened"""

    while True:
    
        test_payload = '\0\0'

        if os.write(pipe_request, test_payload.encode()) is -1:
            break

        result = os.read(pipe_response, 1)

        if len(result) != 1:
            break

        result = os.read(pipe_response, len(result))

        print ("[CLIENT] Server response", result)

open_pipes()











