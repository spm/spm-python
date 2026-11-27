from spm._runtime import Runtime


def mne_ex_data_sets(*args, **kwargs):
    r"""
          
          Find all evoked response data from a given file  
         
          [res] = mne_ex_data_sets(fname)  
         
          fname   - Name of the file to look at  
          res     - Structure containing the result  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_data_sets.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_data_sets", *args, **kwargs)
