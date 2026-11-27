from spm._runtime import Runtime


def fiff_read_mri(*args, **kwargs):
    r"""
       
        [stack] = fiff_read_mri(fname,read_data)  
         
        read_data argument is optional, if set to false the pixel data are  
        not read. The default is to read the pixel data  
         
        Read a fif format MRI description file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_mri.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_mri", *args, **kwargs)
