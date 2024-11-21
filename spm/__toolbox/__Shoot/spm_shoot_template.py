from spm.__wrapper__ import Runtime


def spm_shoot_template(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_template.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_template", *args, **kwargs)
