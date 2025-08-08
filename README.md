```
   ___  ____  __  __
  / __)(  _ \(  \/  )
  \__ \ )___/ )    (   Statistical Parametric Mapping
  (___/(__)  (_/\/\_)  SPM - https://www.fil.ion.ucl.ac.uk/spm/
```

```
Copyright (C) 1991,1994-2025 Wellcome Centre for Human Neuroimaging
```

# The Python interface to _[SPM](https://www.fil.ion.ucl.ac.uk/spm/docs/)_
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spm-python)
![PyPI - License](https://img.shields.io/pypi/l/spm-python)
![PyPI - Version](https://img.shields.io/pypi/v/spm-python)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/spm/spm-python/.github%2Fworkflows%2Frun_unit_tests.yml)

> [!WARNING]
> This project is **young** and might contain bugs.
> **If you experience any issues, please [let us know](https://github.com/spm/spm-python/issues)!**

## Installation instructions

### Important - Windows

Python installation made from Microsoft Store on Windows will not work
(raises DeclarativeService.dll not found), install it from Python website.

### Important - Python/MATLAB compatibility

Specific versions of MATLAB are compatible with
[specific versions of Python](https://uk.mathworks.com/support/requirements/python-compatibility.html).

By default, spm-python uses:
- Python 3.6: R2020b
- Python 3.7: R2021b
- Python 3.8: R2023a
- Python 3.9-3.12: R2025a
- Python 3.13: Unsupported

### Option 1 - Install the MATLAB runtime on first use

1. Install SPM-Python
   ```shell
   pip install spm-python
   ```
2. Run spm
   ```shell
   spm
   ```
3. Follow the instructions

- **Advantages**
  - Installs the runtime that is required for your python version
  - Does not resintall anything if a compatible runtime already exists
- **Drawbacks**
  - May need to be run in proviledged mode (e.g., `sudo`)
  - May be fiddly on Windows

### Option 2 - Install the MATLAB runtime manually

1. Install the appropriate [MATLAB Runtime](https://uk.mathworks.com/products/compiler/matlab-runtime.html)
2. Install SPM:
   ```python
   pip install spm-python
   ```

- **Advantages**
  - Graphical interface for installing the runtime
- **Drawbacks**
  - The correct runtime must be selected for your python version

### Option 3 - Install the MATLAB runtime using an installation script

1. Install SPM-Python
   ```shell
   pip install spm-python
   ```
2. Run the installer
   ```shell
   install_matlab_runtime --version R2025a --yes
   ```

- **Advantages**
  - Exposes installation options (`install_matlab_runtime --help`)
  - Allows any runtime version to be installed. One may do:
    ```shell
    pip install spm-python[R2023b]
    install_matlab_runtime --version R2023b
    ```
- **Drawbacks**
  - For advanced users

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
spm('defaults', 'eeg')
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
S.data = 'OPM_meg_001.cMEG'
S.positions = 'OPM_HelmConfig.tsv'
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
S.plot = 1
S.D = mD
[_,freq] = spm_opm_psd(S, nargout=2)
```

### 5. Other examples
In Matlab:
```Matlab
S = [];
S.D = D;
S.freq = [10];
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
