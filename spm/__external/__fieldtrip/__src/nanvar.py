from spm._runtime import Runtime


def nanvar(*args, **kwargs):
    r"""
      FORMAT: Y = NANVAR(X,FLAG,DIM)  
          
           This file is intended as a drop-in replacement for Matlab's nanvar. It  
           originally forms part of the NaN suite:  
           http://www.mathworks.com/matlabcentral/fileexchange/6837-nan-suite/  
           and was modified to be compatible.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/nanvar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nanvar", *args, **kwargs)
