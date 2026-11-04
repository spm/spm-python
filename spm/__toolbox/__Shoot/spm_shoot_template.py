from spm._runtime import Runtime


def spm_shoot_template(*args, **kwargs):
    r"""
      Iteratively compute a template with mean shape and intensities  
        FORMAT out = spm_shoot_template(job)  
        Fields of job:  
            job.images{1} first set of images (eg rc1*.nii)  
            job.images{2} second set of images (eg rc2*.nii)  
            etc  
         
        Other settings are defined in spm_shoot_defaults.m  
         
        The outputs are flow fields (v_*.nii), deformation fields (y_*.nii),  
        Jacobian determinants (j_*.nii) and a series of Template images.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Shoot/spm_shoot_template.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_shoot_template", *args, **kwargs)
