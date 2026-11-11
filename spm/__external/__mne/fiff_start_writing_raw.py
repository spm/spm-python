from spm._runtime import Runtime


def fiff_start_writing_raw(*args, **kwargs):
    r"""
       
        function [fid,cals] = fiff_start_writing_raw(name,info,sel)  
         
        name       filename  
        info       The measurement info block of the source file  
        sel        Which channels will be included in the output file (optional)  
        precision  Numeric precision with which the data will be written  
                   (optional). Default 'single', can also be 'double'  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_start_writing_raw.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_start_writing_raw", *args, **kwargs)
