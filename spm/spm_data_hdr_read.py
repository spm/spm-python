from spm.__wrapper__ import Runtime


def spm_data_hdr_read(*args, **kwargs):
    """
      Get data information from file  
        FORMAT V = spm_data_hdr_read(P)  
        P        - a char or cell array of filenames  
         
        V        - a structure array containing data information  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_data_hdr_read.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_data_hdr_read", *args, **kwargs)
