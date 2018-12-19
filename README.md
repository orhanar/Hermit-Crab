
# Hermit Crab

Multi-Client Multi-Threaded Reverse Shell in Python


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need IDE for Python such as [PyCharm](https://www.jetbrains.com/pycharm/) and Python 3.6.x installed with cx_Freeze Module
```
In Pycharm Go To File->Settings->Project_Interpreter and select your Python directory.If under packages you can't see cx_Freeze Module,click + sign at the right and search for cx_Freeze within available packages and install it.
```

### Installing

1) Clone the Project

```
Go To Project Page and Click Green Clone or Download Button on Github.
```

2) Setting Up the Github Desktop

```
After you downloaded Github Desktop or Git Bash and you logged in with your profile, clone the repository using the link you got on directory you want.
```

3) Selecting the project type

```
You can then go to directory you cloned the project and go to Single_Client or Multiple_Clients Section based on program you want to run.
```

4) Opening Files

```
Open Client.py and Server.py from directory you picked using PyCharm or any other Python IDE.
```

5) Running Files

```
First run the Server.py.Then go to Client.py and edit host variable with the IP Address of your Server.Then run Client.py
```


## Running the tests

Basic tests for the Single_Client setup includes command dir and cd .. 
For Multiple_Client setup you can run list to list of connected devices.quit for quiting from the devices you are connected to and normal cd and dir commands while you are connected to the specific device. Also you can test select x from Hermit Crab cmd where x is number of device you want to connect to.

### Break down into end to end tests

These tests check whether you can connect to the client and whether you can run commands on them.


## Deployment

You can deploy Multiple_Client Client.py file by going to directory it is in and running python Setup.py build.Then you can save and run your Server.py on your Server.

## Built With

* Cx_Freeze
* Python


## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Orhan Arifoglu** - *Initial work* 

See also the list of [contributors](https://github.com/lemikistu/Hermit-Crab/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Disclaimer

* This reverse shell should only be used in the lawful, remote administration of authorized systems. Accessing a computer network without authorization or permission is illegal.In such a cases of misuse, author of the program do not take any responsibility.
