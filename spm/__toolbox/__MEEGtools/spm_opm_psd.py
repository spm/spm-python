from spm.__wrapper__ import Runtime


def spm_opm_psd(*args, **kwargs):
    """
      Compute PSD for OPM data (for checking noise floor)  
        FORMAT [po,freq,sel] = spm_opm_psd(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                       - Default: no Default  
          S.triallength   - window size (ms)                      - Default: 1000  
          S.bc            - boolean to dc correct                 - Default: 0  
          S.channels      - channel  to estimate PSD from         - Default: 'ALL'  
          S.plot          - boolean to plot or not                - Default: 0  
          S.units         - units of measurement                  - Default: 'fT'  
          S.constant      - constant line to draw as reference    - Default: 15  
          S.wind          - function handle for window            - Default: @hanning  
          S.plotbad       - place asterisk over unusual channels  - Default: 0  
       	S.interact		- allow inspection of channels			- Default: 0  
       	S.select		- enable selection of channels			- Default: 0  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_psd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_psd", *args, **kwargs)
