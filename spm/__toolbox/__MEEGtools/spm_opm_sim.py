from spm.__wrapper__ import Runtime


def spm_opm_sim(*args, **kwargs):
    """
      Simulate magnetometer data  
        FORMAT D = spm_opm_create(S)  
          S               - input structure  
        Optional fields of S:  
        SENSOR LEVEL INFO  
          S.fs            - Sampling frequency (Hz)      - Default: REQUIRED if S.meg is empty  
        SIMULATION  
          S.wholehead     - whole head coverage flag     - Deafult: 1  
          S.space         - space between sensors(mm)    - Default: 35  
          S.offset        - scalp to sensor distance(mm) - Default: 6.5  
          S.nSamples      - number of samples            - Default: 1000  
          S.Dens          - number of density checks     - Default: 40  
          S.axis          - number of othogonal axes     - Default: 1  
        SOURCE LEVEL INFO  
          S.positions     - positions.tsv file           - Default:  
          S.sMRI          - Filepath to  MRI file        - Default: uses template  
          S.cortex        - Custom cortical mesh         - Default: Use inverse normalised cortical mesh  
          S.scalp         - Custom scalp mesh            - Default: Use inverse normalised scalp mesh  
          S.oskull        - Custom outer skull mesh      - Default: Use inverse normalised outer skull mesh  
          S.iskull        - Custom inner skull mesh      - Default: Use inverse normalised inner skull mesh  
          S.voltype       - Volume conducter Model type  - Default: 'Single Shell'  
          S.meshres       - mesh resolution(1,2,3)       - Default: 1  
          S.lead          - flag to compute lead field   - Default: 0  
        Output:  
         D           - MEEG object (also written to disk)  
         L           - Lead field (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_sim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_sim", *args, **kwargs)
