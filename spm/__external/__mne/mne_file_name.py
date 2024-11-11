from spm.__wrapper__ import Runtime


def mne_file_name(*args, **kwargs):
    """
       
          [name] = mne_file_name(dir,name)  
         
          Compose a file name under MNE_ROOT  
         
          dir     - Name of the directory containing the file name  
          name    - Name of the file under that directory  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_file_name.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_file_name", *args, **kwargs)
