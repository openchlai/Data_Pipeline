# Data_Pipeline
This script will enable the management and manipulation of media as recorded within the `Helpline Case Management`

# System Requirements

The following instructions make assumption you are using the following `stack` or `environment`
## Ubuntu
## Python3 (3.10 and above)

# CREATE PYTHON VIRTUAL ENV

We recommend `workon` command, but you can use `virtualenv` to manage your virtual environments. Below instructions can work on `MacOS` and `Windows OS`, just make adjustment where applicable

```sh
sudo apt install python3-pip python3-virtualenv
```

## Create the following `virtualenvs` dir as hidden folder in your $HOME

```sh
mkdir $HOME/.virtualenvs
pip3 install virtualenvwrapper
```

## Update your `local env` by editing `.bashrc` file. You can use `vim` or `nano`, or any CLI text editor

```sh
nano $HOME/.bashrc
```
		
## Paste the following at the bottom of thr `.bashrc` file

```sh
#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/home/bitzml/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```

## Source the updated `.bashrc` file

```sh
source .bashrc
```

## Create the Virtual Environment, here we call it `bitzml` for `Bitz Machine Learning`

```sh
mkvirtualenv bitzml
# workon or lsvirtualenv
```

## You can remove the `virtual env` with the following command
```sh
rmvirtualenv bitzml
```

## You can copy the `virtual env` to something else:
```sh
cpvirtualenv bitzml newbitzml
```
## To start the `virtual env`

```sh
workon bitzml
```

# INSTALL `ffmpeg` & `sox`
We need this libraries within the `OS` to perform media manipulation and conversion

```sh
sudo apt install ffmpeg sox
```

## Install all required libraries from a text file as follows:

```sh
pip install -r requirements.txt
```
