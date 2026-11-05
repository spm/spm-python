from spm._runtime import Runtime


def spm_opm_hfc(*args, **kwargs):
    r"""
      remove interference that behaves as if it was from a harmonic (magnetic) field  
        FORMAT D = spm_opm_hfc(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                                - Default: no Default  
          S.L             - Spherical harmonic order (1=homogenous field)  - Default: 1  
          S.usebadchans   - logical to correct channels marked as bad      - Default: 0  
          S.chunkSize     - max memory usage(for large datasets)           - Default 512(MB)  
          S.badChanThresh - threshold (std) to identify odd channels       - Default 50 (pT)  
          S.balance       - logical to update forward model                - Default 1  
          S.prefix        - prefix to filename                             - Default 'h'  
        Output:  
          D               - denoised MEEG object (also written to disk)  
          Yinds           - the indices of filtered channels  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_hfc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_hfc", *args, **kwargs)
