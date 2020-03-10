**** check python version and conda env
$ conda info -e : shows python3 conda environments based if we are in python version3 
or python2 conda environment if we are in python2
-- so need to change python3 conda env, since this code is based on python3:
1.  change ~/.bashrc -> anaconda3 : then $ source ~/.bashrc 
2. check $ python --version
3. $ conda info -e : check conda env based on python3
*** need change to this directory, which contain these codes!! ****
4. $ conda activate py37
5. $ (py37) jupyter notebook


