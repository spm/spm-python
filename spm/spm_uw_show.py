from spm._runtime import Runtime


def spm_uw_show(*args, **kwargs):
    r"""
      Manage graphical output for spm_uw_estimate  
        FORMAT spm_uw_show(mode,p1,...)  
         
        mode      - Verb specifying action.  
        p1-p6     - Depends on mode.  
         
        FORMAT spm_uw_show('FinIter',SS,beta,fot,sot,ref,q)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_uw_show.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_uw_show", *args, **kwargs, nargout=0)
