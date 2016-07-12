To run the programme, navigate to the folder in cmd (Windows) or terminal (Unix) and
type:

```bash
python main.py
```

NB:
Python must be in the system path

## ClientConfig

This client has default parameters for both the port number and host to which it is to connect. If the user
desires to define these values for themselves, they may do this easily through the client_config.json file.
This .json file may have the following keys:

| key  | description of value                                    |
|------|---------------------------------------------------------|
| port | the port number that the client would try to connect to |
| host | the host that the client would try to connect to        |