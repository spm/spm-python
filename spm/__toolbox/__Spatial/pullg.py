from spm._runtime import Runtime


def pullg(*args, **kwargs):
    r"""
      GPU single precision pullg  
        FORMAT g1 = pullg(f0, phi, sett)  
        f0   - 3D float array  
        phi  - 4D float array (dim(4)=3)  
        sett - Settings  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/pullg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pullg", *args, **kwargs)
