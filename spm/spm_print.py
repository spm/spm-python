from spm._runtime import Runtime


def spm_print(*args, **kwargs):
    r"""
      Print figure   
        FORMAT spm_print(fname,F,opts)  
        fname  - output filename [Default: 'spm_<date>']  
        F      - figure handle or tag [Default: 'Graphics']  
        opts   - structure containing printing options  
                 [Default: defaults.ui.print from spm_defaults.m]  
         
        FORMAT spm_print(job)  
        Run a batch print job (see spm_cfg_print)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_print.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_print", *args, **kwargs)
