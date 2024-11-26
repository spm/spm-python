```
   ___  ____  __  __
  / __)(  _ \(  \/  )  
  \__ \ )___/ )    (   Statistical Parametric Mapping
  (___/(__)  (_/\/\_)  SPM - https://www.fil.ion.ucl.ac.uk/spm/
```

```
Copyright (C) 1991,1994-2024 Wellcome Centre for Human Neuroimaging
```

# The Python interface to _[SPM](https://www.fil.ion.ucl.ac.uk/spm/docs/)_
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spm-python)
![PyPI - License](https://img.shields.io/pypi/l/spm-python)
![PyPI - Version](https://img.shields.io/pypi/v/spm-python)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/spm/spm-python/.github%2Fworkflows%2Frun_unit_tests.yml)


> [!WARNING]
> This project is **currently under construction** and might contain bugs. **If you experience any issues, please [let us know](https://github.com/spm/spm-python/issues)!**


## Installation instructions: 
0. Install Python and Pip. Python installation made from Microsoft Store on Windows will not work (raises DeclarativeService.dll not found), intall it from Python website. 
1. Install [Matlab Runtime 2024b](https://uk.mathworks.com/products/compiler/matlab-runtime.html) 
2. Install SPM:
   ```python
   pip install spm-python
   ```
3. That's all!

## Minimal example
Here is a minimal set of examples showcasing changes to do to use existing Matlab code in Python (taken from the [OPM tutorial](https://www.fil.ion.ucl.ac.uk/spm/docs/tutorials/opm/evoked/)).

### 1. Importing and setting up SPM
In Matlab:
```Matlab
 spm('defaults', 'eeg');
```
In Python: 
```Python
from spm import *
spm('defaults', 'eeg');
```

### 2. Constructing objects
In Matlab: 
```Matlab
S = [];
S.data = 'OPM_meg_001.cMEG';
S.positions = 'OPM_HelmConfig.tsv';
D = spm_opm_create(S);
```
In Python, create a `Struct()` instead of a `struct`:
```Python
S = Struct()
S.data='OPM_meg_001.cMEG'
S.positions='OPM_HelmConfig.tsv'
D = spm_opm_create(S)
```
Here, `D` will be a `meeg` object which contains a virtual representation of the Matlab object. Class methods should work as expected, e.g.:
```Python
D.fullfile()
>>> './OPM_meg_001.mat'
```
Note that the alternative call that exist in Matlab (i.e., `fullfile(D)`) will not work.  

### 3. Creating and handling figures
In Matlab: 
```Matlab
S = [];
S.triallength = 3000; 
S.plot = 1;
S.D = D;
S.channels = 'MEG';
spm_opm_psd(S);
ylim([1,1e5])
```
In Python:
```Python
S = Struct()
S.triallength = 3000
S.plot = 1
S.D = D
S.channels = 'MEG'
spm_opm_psd(S)
```
This opens a Matlab figure, but we do not have the possibility of manipulating it yet (e.g., calling `ylim`). As of now, we can view the figures, have GUI interactions, but cannot manipulate figures with Python code.

### 4. Variable number of output arguments
In Matlab:
```Matlab
S = [];
S.triallength = 3000; 
S.plot = 1;
S.D = mD;
[~,freq] = spm_opm_psd(S);
```
In Python, the number of output arguments must be specified by the `nargout` keyword argument:
```Python
S = Struct()
S.triallength = 3000
S.plot=1
S.D=mD
[_,freq] = spm_opm_psd(S, nargout=2)
```

### 5. Other examples 
In Matlab:
```Matlab 
S=[];
S.D=D;
S.freq=[10];
S.band = 'high';
fD = spm_eeg_ffilter(S);

S = [];
S.D = fD;
S.freq = [70];
S.band = 'low';
fD = spm_eeg_ffilter(S);
```
In Python: 
```Python
S = Struct()
S.D = D
S.freq = 10
S.band = 'high'
fD = spm_eeg_ffilter(S)

S = Struct()
S.D = fD
S.freq = 70
S.band = 'low'
fD = spm_eeg_ffilter(S)
```
