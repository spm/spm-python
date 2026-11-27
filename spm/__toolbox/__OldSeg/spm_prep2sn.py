from spm._runtime import Runtime


def spm_prep2sn(*args, **kwargs):
    r"""
      Convert the output from spm_preproc into an sn.mat file  
        FORMAT [po,pin] = spm_prep2sn(p)  
        p   - the results of spm_preproc  
         
        po  - the output in a form that can be used by spm_write_sn  
        pin - the inverse transform in a form that can be used by spm_write_sn  
         
        The outputs are saved in sn.mat files only if they are not requested LHS.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/OldSeg/spm_prep2sn.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_prep2sn", *args, **kwargs)
