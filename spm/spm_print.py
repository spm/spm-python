from spm.__wrapper__ import Runtime


def spm_print(*args, **kwargs):
    """
      Print figure   
        FORMAT spm_print(fname,F,opts)  
        fname  - output filename [Default: 'spm_<date>']  
        F      - figure handle or tag [Default: 'Graphics']  
        opts   - structure containing printing options  
                 [Default: defaults.ui.print from spm_defaults.m]  
         
        FORMAT spm_print(job)  
        Run a batch print job (see spm_cfg_print)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_print.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_print", *args, **kwargs)
