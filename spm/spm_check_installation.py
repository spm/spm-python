from spm.__wrapper__ import Runtime


def spm_check_installation(*args, **kwargs):
    """
      Check SPM installation  
        FORMAT spm_check_installation('basic')  
        Perform a superficial check of SPM installation [default].  
         
        FORMAT spm_check_installation('full')  
        Perform an in-depth diagnostic of SPM installation.  
         
        FORMAT rev = spm_check_installation('rev')  
        Return a lower bound of SPM SVN Revision number.  
          
        FORMAT spm_check_installation('build')  
        Build signature of SPM distribution as used by 'full' option.  
        (for developers)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_check_installation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_check_installation", *args, **kwargs)
