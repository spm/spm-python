from spm.__wrapper__ import Runtime


def spm_uw_show(*args, **kwargs):
    """
      Manage graphical output for spm_uw_estimate  
        FORMAT spm_uw_show(mode,p1,...)  
         
        mode      - Verb specifying action.  
        p1-p6     - Depends on mode.  
         
        FORMAT spm_uw_show('FinIter',SS,beta,fot,sot,ref,q)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uw_show.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uw_show", *args, **kwargs, nargout=0)
