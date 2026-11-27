from spm._runtime import Runtime


def spm_data_hdr_read(*args, **kwargs):
    r"""
      Get data information from file  
        FORMAT V = spm_data_hdr_read(P)  
        P        - a char or cell array of filenames  
         
        V        - a structure array containing data information  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_data_hdr_read.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_data_hdr_read", *args, **kwargs)
