from spm._runtime import Runtime


def mne_file_name(*args, **kwargs):
    r"""
       
          [name] = mne_file_name(dir,name)  
         
          Compose a file name under MNE_ROOT  
         
          dir     - Name of the directory containing the file name  
          name    - Name of the file under that directory  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_file_name.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_file_name", *args, **kwargs)
