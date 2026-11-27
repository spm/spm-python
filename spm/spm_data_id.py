from spm._runtime import Runtime


def spm_data_id(*args, **kwargs):
    r"""
      Generate a specific real number in a deterministic way from any data structure  
        FORMAT ID = spm_data_id(X)  
        X  - numeric, character, cell or structure array[s]  
        ID - specific ID  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_data_id.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_data_id", *args, **kwargs)
