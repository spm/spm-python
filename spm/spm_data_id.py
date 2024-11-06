from spm.__wrapper__ import Runtime


def spm_data_id(*args, **kwargs):
    """
      Generate a specific real number in a deterministic way from any data structure  
        FORMAT ID = spm_data_id(X)  
        X  - numeric, character, cell or structure array[s]  
        ID - specific ID  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_data_id.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_data_id", *args, **kwargs)
