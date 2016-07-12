To run the programme, navigate to the folder in cmd (Windows) or terminal (Unix) and
type:

```bash
python main.py
```

NB:
Python must be in the system path

## ServerConfig 

The server has default parameters for port number, host name, whether to concurrently process clients, and the 
IP addresses to block. If the user wishes to set thier own parameters for any of these values, they may edit
the server_config.json file. The possible keys in this .json file is described as follows:


| key               | description of value                                                                      |
|-------------------|-------------------------------------------------------------------------------------------|
| port              | the port number that the server expects clients to connect to, e.g. 12345                 |
| host              | the host of the server, e.g. "127.0.0.1"                                                  |
| use_multithreaded | *true* or *false*. Indicates whether to process multiple clients concurrently, e.g. true      |
| block_list        | array of strings. Each string is the host address of a blocked client, e.g. ["127.0.0.1"] |