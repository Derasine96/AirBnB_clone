# AirBnB clone - The console

## 0x00.Table of contents

	* [0x01 Introduction](#0x01-Introduction)
	* [0x02 Environment](#0x02-Environment)
	* [0x03 Installation](#0x03-Installation)
	* [0x04 Testing](#0x04-Testing)
	* [0x05 Usage](#0x05-Usage)
* [0x06 Authors](#0x06-Authors)

## 0x01 Introduction

	Team project to build a clone of [AirBnB](https://www.airbnb.com/).

	The console is a command interpreter to manage objects abstraction between objects and how they are stored.

	The console will perform the following tasks:

	* create a new object
	* retrive an object from a file
	* do operations on objects
	* destroy an object
	amongst others...

### Storage

	All the classes are handled by the `Storage` engine in the `FileStorage` Class.

## 0x02 Environment

	<!-- Style guidelines -->
	* Style guidelines:
	* [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
	* [PEP8](https://pep8.org/)

## 0x03 Installation

	change to the `AirBnb` directory and run the command:

	```bash
	./console.py
	```

### Execution

	In interactive mode

	```bash
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$
	```

	in Non-interactive mode

	```bash
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
	```

## 0x04 Testing

	All the test are defined in the `tests` folder.

### Documentation

	* Modules:

	```python
	python3 -c 'print(__import__("my_module").__doc__)'
	```

	* Classes:

	```python
	python3 -c 'print(__import__("my_module").MyClass.__doc__)'
	```

	* Functions (inside and outside a class):

	```python
	python3 -c 'print(__import__("my_module").my_function.__doc__)'
	```

	and

	```python
	python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	```

### Python Unit Tests

		* unittest module
		* File extension ``` .py ```
		* Files and folders star with ```test_```
		* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
		* Execution command: ```python3 -m unittest discover tests```
		* or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

		```bash
		echo "python3 -m unittest discover tests" | bash
		```

### run test in non-interactive mode

		To run the tests in non-interactive mode, and discover all the test, you can use the command:

		```bash
		python3 -m unittest discover tests
		```

## 0x05 Usage

		* Start the console in interactive mode:

		```bash
	$ ./console.py
(hbnb)
	```

	* Use help to see the available commands:

	```bash
	(hbnb) help

	Documented commands (type help <topic>):
		========================================
			EOF  all  count  create  destroy  help  quit  show  update

			(hbnb)
	```

	* Quit the console:

	```bash
	(hbnb) quit
	$
	```

### Commands

	> The commands are displayed in the following format *Command / usage / example with output*

	* Create

	> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

	```bash
	create <class>

	```

	```bash
	(hbnb) create BaseModel
	6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
	```

	* Show

	```bash
	show <class> <id>
	```

	```bash
	(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
	[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
	```

	* Destroy

	> *Deletes an instance of a given class with a given ID.*
	> *Update the file.json*

	```bash
	(hbnb) create User
	0c98d2b8-7ffa-42b7-8009-d9d54b69a472
	(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
	(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
	** no instance found **
(hbnb)
	```

	* all

	> *Prints all string representation of all instances of a given class.*
	> *If no class is passed, all classes are printed.*

	```bash
	(hbnb) create BaseModel
	ff74d560-42e1-453e-ad11-a4aec10da1cc
	(hbnb) all BaseModel
	["[BaseModel] (ff74d560-42e1-453e-ad11-a4aec10da1cc) {'id': 'ff74d560-42e1-453e-ad11-a4aec10da1cc', 'created_at': datetime.datetime(2023, 12, 10, 20, 34, 40, 821428), 'updated_at': datetime.datetime(2023, 12, 10, 20, 34, 40, 821605)}"]
	```

	* count

	> *Prints the number of instances of a given class.*

	```bash
	(hbnb) create City
	ff74d560-42e1-453e-ad11-a4aec10da1cc
	(hbnb) create City
	ff74d560-42e1-453e-ad11-a4aec10da1cc
	(hbnb) count City
	2
(hbnb)
	```

	* update

	> *Updates an instance based on the class name, id, and kwargs passed.*
	> *Update the file.json*

	```bash
	(hbnb) create User
	1afa163d-486e-467a-8d38-3040afeaa1a1
	(hbnb) update User 1afa163d-486e-467a-8d38-3040afeaa1a1 email "aysuarex@gmail.com"
	(hbnb) show User 1afa163d-486e-467a-8d38-3040afeaa1a1
	[User] (s) [User] (1afa163d-486e-467a-8d38-3040afeaa1a1) {'id': '1afa163d-486e-467a-8d38-3040afeaa1a1', 'created_at': datetime.datetime(2021, 11, 14, 23, 42, 10, 502157), 'updated_at': datetime.datetime(2021, 11, 14, 23, 42, 10, 502186), 'email': 'aysuarex@gmail.com'}
(hbnb)

	```
## Authors
	<details>
	<summary>Gbenga Etomu</summary>
	<ul>
	<li><a href="https://github.com/CyberGA">Github</a></li>
	<li><a href="https://www.twitter.CyberGA">Twitter</a></li>
	<li><a href="mailto:etomu.joshua@gmail.com">e-mail</a></li>
	</ul>
	</details>
	<details>
	<summary>Obikwelu Chidera</summary>
	<ul>

	<li><a href="https:/"https://github.com/Derasine96">Github</a></li>
	<li><a href="https://www.twitter.com/derasin_jay">Twitter</a></li>
	<li><a href="mailto:chidexobikwelu@gmail.com">e-mail</a></li>
	</ul>
	</details>
