<img src="sw_logo.png" width="64">

# TEC and Bias receiver estimation [STUDY CASE]
[![](https://img.shields.io/github/license/embrace-inpe/swds-api-downloader.svg)](https://github.com/embrace-inpe/swds-api-downloader/blob/master/LICENSE)
[![](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/INPE-EMBRACE-orange.svg)](http://www2.inpe.br/climaespacial/portal/pt/)

This is an example for using the application TEC (by station) and receiver bias estimation through GNSS data processing and analysis (library available in ), used for monitoring of ionospheric terrestrial layer. 

Please, fell free to read more in [EMBRACE](http://www2.inpe.br/climaespacial/portal/pt/).

#### Contributors involved
###### Departamento de Ciências Espaciais e Atmosféricas (CEA-II) - INPE
Dr. Cristiano Max Wrasse (Pesquisador) [_cristiano.wrasse@inpe.br_]  
Dr. Cosme A. O. B. Figueiredo [_cosme.figueiredo@inpe.br_]  

###### Development team - EMBRACE/INPE
Dr. Rodolfo G. Lotte [_rodolfo.lotte@inpe.br_]  
 
***
## GNSS's versions file covered:
- GNSS rinex version 3.01
- GNSS rinex version 3.02
- GNSS rinex version 3.03

PS:. The EMBRACE TEC and Bias estimation make use of external library `georinex` for reading rinex files, which includes 
other versions! To read more about, check the [link](https://pypi.org/project/georinex/).

## Requirements
Besides the Python libraries required for this current source-code, global libraries is mandatory to the well execution of all the workflow.

```
sudo apt-get install libgeos-dev
```

## Features
This module includes the calculation of:

- Automatic download and interpretation of Orbit and DCB files, both under MGEX (Multi-GNSS Experiment) format
- Cycle-Slip correction
- Relative TEC
- Slant Factor
- Daily TEC and receiver bias estimation
- Absolute TEC
- Vertical TEC



## Output
This module runs for a set of rinex files. For each rinex processed, a python dictionary JSON-like structured is generated.

The python dictionary outcome, will comprises the following format:



## Contributing:
### TODO list: 
Of course, the model is far completed. Besides the TODOs marks into the code, the analysis for another 
situations are still demanded. If you notice some kind of mistake in the code, or just notice that could improve or 
optimize any method, please, fell free to clone this project and help our team to get better estimates.

### Preparing your environment:
To contribute, you have to clone this repository and start your analysis/debugs/ so on.

After to clone the repository [git](https://github.com/embrace-inpe/tec) in your local directory, 
the following the instructions will guide you to execute the model in your computer.

1. [Updating your Python](#1-Updating-your-Python)
2. [Create a isolated Python environment with virtualenv](#2-Create-a-isolated-Python-environment-with-virtualenv)
3. [Installing dependencies with `pip`](#3-Installing-dependencies-with)
4. [Setting up the constants](#4-Setting up the constants)
5. [Executing the `main.py`](#5-Executing-the)
6. [Performance](#6-Performance)

#### 1. Updating your Python
The EMBRACE TEC and Bias estimation was developed using version Python 3.7+. If you do not have this version in your computer, an upgrade will be need. 

First, check the version of your python typing `python -V`. If old versions are diplayed, thus, follow the steps below. For most of Ubuntu users, two versions are available on the OS, `python2.7`, and `python3`, which still do not fill the requirement due the `python3` be usually under version 3.6 (to check this, please, type `python3 -V`). If not, the following steps can solve the problem.

To start the upgrade, update your system:
```
sudo apt-get update && sudo apt-get upgrade && sudo apt-get update
```
then, run:
```
sudo apt-get install python3.7
```

If everything is ok, edit your `bashrc` file:
```
sudo nano ~/.bashrc
```
and update the file:
```
source ~/.bashrc
```

and include at the last line: `alias python=python3.7`. Type:
```
python -V
``` 

#### 2. Create a isolated Python environment with virtualenv
The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories ([SOURCE])(https://docs.python.org/3/library/venv.html). 

Thus, everything installed inside this environment, do not get mixed with the system programs or configurations. So, go to `tec/` (root path) and create an isolated environment with:

```console
$ python -m venv .venv
```

To activate your `.venv`, type the following: 

```console
$ source .venv/bin/activate
```

If everything is ok, you will see the virtual env prefix:
```console
(.venv) usuario@maquina:<seu-diretorio>$ your commands here
```

Now, everything installed through `pip`, will be encapsulated by the `venv`, and will be available only in this 
respective scope.

To deactivate, just type: 

```console
$ deactivate
```

#### 3. Installing the dependencies with `pip`
After you have set all the variables in `.env` with you personal information, you need to install the 
dependencies listed in `requirements.txt`:
```
pip install -r requirements.txt
```
Then, run:
```
python runtests.py
```

#### 4. Setting up the constants in `.env`
The `settings.py` is the module responsible to store all the constants used by the model. Besides these constants, 
another ones are also essential to make the process possible, the ones respected to your 
computer!

So, in this case, the constants that change the computer by computer, is setup in `.env` file. 
Here, you can set what you want to consider in the modelling. For instance, the 
constellations, the minimum required rinex version, the resolution of estimation (1 hour, 
10 minutes, so on), and the paths the rinex are! 

First, copy the file `.env-example` and rename for `.env`. You will see all variables setted like:
```
PATH_DCB=
PATH_ORBIT=
PATH_GLONASS_CHANNEL=
RINEX_FOLDER=

MIN_REQUIRED_VERSION=2.11
CONSTELATIONS=['G', 'R', 'E', 'C']
TEC_RESOLUTION=hours
TEC_RESOLUTION_VALUE=1
KEYS_SAVE=['time', 'slant-dtec', 'slant', 'detrended', 'bias', 'quality', 'vertical']
```

- `PATH_DCB`: The path to save the DCB file
- `PATH_ORBIT`: The path to save the orbit file
- `PATH_GLONASS_CHANNEL`: The path to save the GLONASS channels to calc the frequencies by PRN. It will be download if GLONASS used or not
- `RINEX_FOLDER`: The path with rinex content
- `MIN_REQUIRED_VERSION`: The minimum rinex version required
- `TEC_RESOLUTION`: This parameter specify the resolution to be read in the rinex. Usually, the rinex have 30 or 15 seconds resolution. Thus, the solution matrix construct during the estimation process, could be either 15 seconds or an hourly average matrix. So, the solution (bias estimation) will be less or more precise depending the resolution used. However, if a too high resolution is used, such as 15 seconds, the matrix can get a high dimension and might dispend too much computacional costs. The recommend resolution is something between 10 minutes and 1 hour. So, the value here should be `hours` or `minutes`, depeding the choise.
- `TEC_RESOLUTION_VALUE`: If the above item is `hours`, this item value should be `1` (one hour), or `10`, if setted up `minutes` (10 minutes).
- `KEYS_SAVE`: As mentioned above, the outcome for each rinex file is a dictionary, with other sub-dicts inside it, storing each of the TEC workflow (e.g. slant, relative, detrended, absolute, bias, vertical, so on). Later, each of these keys should be stored in a database. Here, are specified only the dict-keys you want to go to the database at the end, specially because not only sub-dicts are essential to have stored. 
 
#### 5. Executing the `main.py`
Once the `.venv` activated, the paths with rinex are correctly setted in `.env` (P.S. do not get confused: the `.venv` is your environment variable, which is not related to `.env`, that is your local constants). 

The main execution should be made by the `main.py` script, in `/tec`:
```console
$ python main.py
```

If all correct, the output will be something like:
```console
[2019.06.02 13:34:01] {tec.py         :81  } INFO : - ango2220.14o - TEC by fractions of 1 hours a day, and bias receiver estimation 
[2019.06.02 13:34:01] {tec.py         :82  } INFO : Preparing inputs... 
[2019.06.02 13:34:01] {helper.py      :843 } INFO : >> Validating file and measures... 
[2019.06.02 13:34:01] {helper.py      :845 } INFO : >>>> Rinex version 3.01! 
[2019.06.02 13:34:01] {helper.py      :756 } INFO : >>>>>> Column L1 is not available for constellation E. TEC wont be consider for this constellation! 
[2019.06.02 13:34:01] {helper.py      :756 } INFO : >>>>>> Column L1 is not available for constellation C. TEC wont be consider for this constellation! 
[2019.06.02 13:34:01] {helper.py      :857 } INFO : >> Reading rinex measures... Only constellation(s) ['G'] will be considered! 
[2019.06.02 13:34:35] {helper.py      :882 } INFO : >> Downloading GLONASS channels in https://www.glonass-iac.ru/en/CUSGLONASS/ for pseudorange calculation... 
[2019.06.02 13:34:35] {downloads.py   :78  } INFO : >>>> Glonass Channel File already exist. Download skipped! 
[2019.06.02 13:34:35] {parser.py      :166 } INFO : >> Starting GLONASS channels parsing... 
[2019.06.02 13:34:35] {helper.py      :918 } INFO : >> Downloading Orbit files...
[...]
```

#### 6. Performance


## Log
Download errors will be listed in tec.log on root path.

## Help
Any question or suggestion, please, contact our support sending an email to `desenvolvimento.emabrace@inpe.br` or any 
of the contributers.


