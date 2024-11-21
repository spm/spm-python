from spm.__wrapper__ import Runtime


def spm_shoot_divergence(*args, **kwargs):
    """
      Compute divergences from velocity fields  
        FORMAT spm_shoot_divergence(job)  
        job.velocities - Filenames of initial velocity fields  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_divergence.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_divergence", *args, **kwargs)
