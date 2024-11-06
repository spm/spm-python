from spm.__wrapper__ import Runtime


def spm_dartel_dotprods(*args, **kwargs):
    """
      Generate a kernel from dot-products of images  
        FORMAT spm_dartel_dotprods(job)  
        job.images  - Images to use  
        job.dotprod - Part of filename for results  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_dotprods.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_dotprods", *args, **kwargs, nargout=0)
