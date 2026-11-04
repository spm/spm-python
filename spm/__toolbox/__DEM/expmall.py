from spm._runtime import Runtime


def expmall(*args, **kwargs):
    r"""
    expmall is a function.  
          dx = expmall(J, f, t, EP)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/expmall.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("expmall", *args, **kwargs)
