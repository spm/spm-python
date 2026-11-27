from spm._runtime import Runtime


def spm_dartel_dotprods(*args, **kwargs):
    r"""
      Generate a kernel from dot-products of images  
        FORMAT spm_dartel_dotprods(job)  
        job.images  - Images to use  
        job.dotprod - Part of filename for results  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_dotprods.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_dotprods", *args, **kwargs, nargout=0)
