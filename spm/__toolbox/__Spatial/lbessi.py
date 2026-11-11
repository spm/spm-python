from spm._runtime import Runtime


def lbessi(*args, **kwargs):
    r"""
      GPU single precision f = log(besseli(nu, z))  
        FORMAT f = lbessi(nu,z)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/lbessi.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("lbessi", *args, **kwargs)
