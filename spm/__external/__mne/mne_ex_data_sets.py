from spm.__wrapper__ import Runtime


def mne_ex_data_sets(*args, **kwargs):
    """
          
          Find all evoked response data from a given file  
         
          [res] = mne_ex_data_sets(fname)  
         
          fname   - Name of the file to look at  
          res     - Structure containing the result  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_ex_data_sets.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_ex_data_sets", *args, **kwargs)
