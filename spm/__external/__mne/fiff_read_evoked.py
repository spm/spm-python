from spm.__wrapper__ import Runtime


def fiff_read_evoked(*args, **kwargs):
    """
       
        [data] = fiff_read_evoked(fname,setno)  
         
        Read one evoked data set  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_evoked.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_evoked", *args, **kwargs)
