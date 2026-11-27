from spm._runtime import Runtime


def spm_preproc_write(*args, **kwargs):
    r"""
      Write out VBM preprocessed data  
        FORMAT spm_preproc_write(p,opts)  
        p    - results from spm_prep2sn  
        opts - writing options.  A struct containing these fields:  
               biascor - write bias corrected image  
               cleanup - level of brain segmentation cleanup  
               GM      - flags for which images should be written  
               WM      - similar to GM  
               CSF     - similar to GM  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/OldSeg/spm_preproc_write.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_preproc_write", *args, **kwargs, nargout=0)
