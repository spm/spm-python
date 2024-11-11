from spm.__wrapper__ import Runtime


def cfg_dbstop(*args, **kwargs):
    """
    cfg_dbstop is a function.  
          cfg_dbstop(fh)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_dbstop.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_dbstop", *args, **kwargs, nargout=0)
