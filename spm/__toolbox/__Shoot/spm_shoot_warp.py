from spm.__wrapper__ import Runtime


def spm_shoot_warp(*args, **kwargs):
    """
      Register images with template  
        format spm_shoot_warp(job)  
        Fields of job:  
            job.images{1} first set of images (eg rc1*.nii)  
            job.images{2} second set of images (eg rc2*.nii)  
            etc  
            job.templates template files  
        Other settings are defined in spm_shoot_defaults.m  
         
        The outputs are flow fields (v*.nii), deformation fields (y*.nii) and  
        Jacobian determinants (j*.nii)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_warp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_warp", *args, **kwargs)
