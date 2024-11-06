from spm.__wrapper__ import Runtime


def _read_spmeeg_event(*args, **kwargs):
    """
      read_spmeeg_event() - import evtns from SPM5 and SPM8 meeg datasets  
         
        Usage:  
          >> header = read_spmeeg_event(filename);  
         
        Inputs:  
          filename - [string] file name  
         
        Outputs:  
          event   - FILEIO toolbox event structure  
        _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
        Vladimir Litvak  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_spmeeg_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_spmeeg_event", *args, **kwargs)
