from spm.__wrapper__ import Runtime


def nanvar(*args, **kwargs):
    """
      FORMAT: Y = NANVAR(X,FLAG,DIM)  
          
           This file is intended as a drop-in replacement for Matlab's nanvar. It  
           originally forms part of the NaN suite:  
           http://www.mathworks.com/matlabcentral/fileexchange/6837-nan-suite/  
           and was modified to be compatible.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/nanvar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nanvar", *args, **kwargs)
