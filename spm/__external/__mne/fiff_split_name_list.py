from spm.__wrapper__ import Runtime


def fiff_split_name_list(*args, **kwargs):
    """
       
        [names] = fiff_split_name_list(list)  
         
         
        Split a name list containing colon-separated entries into a cell array  
        containing the strings  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_split_name_list.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_split_name_list", *args, **kwargs)
