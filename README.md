# NamedPipes
Named pipes implementation for inter-process communication on a Raspberry

### Prerequisites

Visual Studio with C++ cross platform add-on

### Installing

Build the solution with visual studio and move the binnary produced to a raspberry folder

You can use FileZilla to move files to raspberry over SSH

Open SSH connection with Raspberry Pi

Give permitions to run ServerRPI.out

```
chmod 755 ServerRPI.out
```

## Running

First run the server

```
./PipeTester.out s
```

Then run the client

```
./PipeTester.out c
```

## Acknowledgments

* This code was used for a solution to communicate with an existing process without being intrusive to the existing process and with low impact
