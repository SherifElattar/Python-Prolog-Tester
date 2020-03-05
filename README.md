# Python-Prolog-Tester
This is a small script that runs multiple queries for a Prolog file and matches them to input cases with provided answers

### Prerequisites

What things you need to install the software and how to install them

```
python 3.6.5 +
pip 9.0.3 +
Swi-Prolog
```

Make sure to have SWI-prolog and python added to your environment variables. 
#### Adding swipl to environment variables on Windows 10:
1. Tap the search bar on the Windows task bar.
2. Search for PATH
3. Choose "Edit the System environment variable"
4. Select "Environemnt Variables"
5. From the User Variables, click on "Path" and click edit
6. Press New, then browse and navigate to the installion directory of SWI-Prolog
7. Add the bin folder of SWI-Prolog to the environemnt path and navigate outside the environment variables window

### Installing

A step by step series of examples that tell you how to get a development env running

Clone into the repo.

```
git clone https://github.com/SherifElattar/Python-Prolog-Tester
```
Install the required package

```
pip install pyswip
```
Copy your .pl file to the repo folder.
Change line 9 on the ```test.py``` to match your .pl file name

### Usage
Run the command ```py test.py```

### Optional Flags
```-v``` or ```-verbose``` displays the output for every query

```-q``` or ```-query``` displays the input of each query and wether your answer matched the provided answer or not

