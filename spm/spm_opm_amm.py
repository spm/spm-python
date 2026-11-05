from spm._runtime import Runtime


def spm_opm_amm(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_opm_amm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_amm", *args, **kwargs)
