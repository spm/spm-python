from spm.__wrapper__ import Runtime


def _read_nimh_cortex(*args, **kwargs):
    """
      READ_NIMH_CORTEX  
         
        Use as  
         cortex = read_nimh_cortex(filename, ...)  
         
        Optional input arguments should come in key-value pairs and may  
        include  
          begtrial     = number (default = 1)  
          endtrial     = number (default = inf)  
          epp          = read the EPP data, 'yes' or 'no' (default = 'yes')  
          eog          = read the EOG data, 'yes' or 'no' (default = 'yes')  
          feedback     = display the progress on the screen, 'yes' or 'no' (default = 'no')  
         
        The output is a structure array with one structure for every trial that was read.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nimh_cortex.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nimh_cortex", *args, **kwargs)
