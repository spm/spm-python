from spm.__wrapper__ import Runtime


def bf_isfield(*args, **kwargs):
    """
      Efficiently identify if a field is contained within a BF file  
        FORMAT bool = bf_isfield(BF,field)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_isfield.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_isfield", *args, **kwargs)
