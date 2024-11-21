from spm.__wrapper__ import Runtime


def fiff_read_mri(*args, **kwargs):
    """
       
        [stack] = fiff_read_mri(fname,read_data)  
         
        read_data argument is optional, if set to false the pixel data are  
        not read. The default is to read the pixel data  
         
        Read a fif format MRI description file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_mri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_mri", *args, **kwargs)
