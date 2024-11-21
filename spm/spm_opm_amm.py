from spm.__wrapper__ import Runtime


def spm_opm_amm(*args, **kwargs):
    """
      models brain signal and interference as a set of geometrically adaptive  
        multipole moments  
        FORMAT D = spm_opm_amm(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                                - Default: no Default  
          S.li             -  internal harmonic order   - Default: 9  
          S.le             -  external harmonic order   - Default: 2  
          S.window        - temporal window size (s)        - 10  
          S.prefix        - prefix to filename          - Default 'm'  
          S.corrLim       - correlation limit          - Default 1  
          S.plotSpheroid  - flag to plot spheroid      - Default 1  
        Output:  
          D               - denoised MEEG object (also written to disk)  
       __________________________________________________________________________  
        Copyright  Tim Tierney  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_opm_amm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_amm", *args, **kwargs)
