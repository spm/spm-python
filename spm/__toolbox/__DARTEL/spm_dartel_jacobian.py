from spm.__wrapper__ import Runtime


def spm_dartel_jacobian(*args, **kwargs):
    """
      Generate Jacobian determinant fields  
        FORMAT spm_dartel_jacobian(job)  
        job.flowfields - Filenames of flowfields  
        job.K          - 2^K timesteps are used  
         
        Note that K needs to be reasonably large in order to obtain reasonable  
        Jacobian determinant fields.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_jacobian.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_jacobian", *args, **kwargs)
