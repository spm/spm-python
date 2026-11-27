from spm._runtime import Runtime


def spm_fMRI_design_show(*args, **kwargs):
    r"""
      Interactive review of fMRI design matrix  
        FORMAT spm_fMRI_design_show(SPM,s,i)  
         
        Sess(s).U(i)  -  see spm_fMRI_design for session s, trial i.  
         
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_fMRI_design_show.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fMRI_design_show", *args, **kwargs, nargout=0)
