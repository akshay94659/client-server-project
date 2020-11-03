# coen-6313-A1
This project is a part of the assignment for the course COEN-6313 at Concordia University. A client server program using two different Serialization and De-serialization methods.

### Installing Dependencies
1. `git clone https://github.com/ahujasushant/coen-6313-A1.git` if you have the access rights.
2. If you don't have the access extract the zip file and `cd PATH_TO_DIR/coen-6313-A1` 
3. If you have the conda installed on your system, you can simply run the following command
`conda env export > environment.yml`. One can install conda and setup on their system using this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and follow the instructions as it says.
4. For the successful running of both the servers and clients, one needs to have protobuf server installed. You can install it using this [link](https://developers.google.com/protocol-buffers) and follow the instructions depending upon your OS.


### Running JSON Based Serialization:
1. Run `python json_server_response.py`
Your server should be running on `http://127.0.0.1:5000/`
2. Run `python json_client_request.py`
3. Enter the values as asked.
4. You should get a response.

### Running Binary Based Serialization:
1. Run `python protobuf_server.py`
2. Run `python protobuf_client.py`
3. Enter the values as asked.
4. You should get a response.

### Deployment