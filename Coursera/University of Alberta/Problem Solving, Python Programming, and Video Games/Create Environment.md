# Creating the environment for Problem Solving

Having Anaconda installed, create an environment with Python 3.6.

```
$ conda create -n Alberta-Problem-Solving python=3.6
$ conda activate Alberta-Problem-Solving
```

Next, we have to install PyGame.

```
$ pip install pygame
```

In case of getting the following error when trying to install pygame:

```
$ pip pygame
Traceback (most recent call last):
  File "/home/roger/Installed/anaconda3/envs/Alberta-Problem-Solving/bin/pip", line 7, in <module>
    from pip._internal.cli.main import main
ModuleNotFoundError: No module named 'pip._internal.cli.main'
```

We have to first update pip, using:

```
$ conda update -n base -c defaults conda
$ conda install pip
```

Once we have all installed, we can test it by typing into the terminal: 

```
python -m pygame.examples.aliens
```

If the game starts, then you have installed pygame successfully!

