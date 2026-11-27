from spm._runtime import Runtime


def fiff_read_meas_info(*args, **kwargs):
    r"""
       
        [info,meas] = fiff_read_meas_info(source,tree)  
         
        Read the measurement info  
         
        If tree is specified, source is assumed to be an open file id,  
        otherwise a the name of the file to read. If tree is missing, the  
        meas output argument should not be specified.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_meas_info.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_meas_info", *args, **kwargs)
