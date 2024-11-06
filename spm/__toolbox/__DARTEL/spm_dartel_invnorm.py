from spm.__wrapper__ import Runtime


def spm_dartel_invnorm(*args, **kwargs):
    """
      Warp template to match individuals  
        FORMAT spm_dartel_invnorm(job)  
        job.flowfields - Filenames of flowfields  
        job.images     - Filenames of images to warp  
        job.interp     - Interpolation method  
        job.K          - 2^K timesteps are used  
         
        This function may be useful fo warping labels on to images.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_invnorm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_invnorm", *args, **kwargs)
