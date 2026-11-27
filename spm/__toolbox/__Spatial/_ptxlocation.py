from spm._runtime import Runtime


def _ptxlocation(*args, **kwargs):
    r"""
      Location of a PTX file used in GPU computations  
        FORMAT ptx = ptxlocation(nam)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/private/ptxlocation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ptxlocation", *args, **kwargs)
