# Project Title

Named pipes implementation for inter-process communication in Python

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install Python 3 on Raspberry

```
sudo apt-get install python3
```

### Installing

Move pipe_client_tester.py and pipe_server_tester.py for a folder on Raspberry.

You can use FileZilla to move files to raspberry over SSH.


## Running

Open two SSH connections with Raspberry Pi

First run the server

```
python3 pipe_server_tester.py
```

Then run the client

```
python3 pipe_client_tester.py
```

## Acknowledgments

* This code was used for a solution to communicate with an existing project without being intrusive to the existing process and with low impact