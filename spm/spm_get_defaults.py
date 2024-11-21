from spm.__wrapper__ import Runtime


def spm_get_defaults(*args, **kwargs):
    """
      Get/set the defaults values associated with an identifier  
        FORMAT defaults = spm_get_defaults  
        Return the global "defaults" variable defined in spm_defaults.m.  
         
        FORMAT defval = spm_get_defaults(defstr)  
        Return the defaults value associated with identifier "defstr".   
        Currently, this is a '.' subscript reference into the global    
        "defaults" variable defined in spm_defaults.m.  
         
        FORMAT spm_get_defaults(defstr, defval)  
        Set the defaults value associated with identifier "defstr" to defval.  
        The new defaults value applies immediately to:  
        * new modules in batch jobs  
        * modules in batch jobs that have not been saved yet  
        This value will not be saved for future sessions of SPM. To make  
        persistent changes, see help section in spm_defaults.m.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_defaults.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_defaults", *args, **kwargs)
