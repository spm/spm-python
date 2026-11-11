from spm._runtime import Runtime


def spm_dartel_jacobian(*args, **kwargs):
    r"""
      Generate Jacobian determinant fields  
        FORMAT spm_dartel_jacobian(job)  
        job.flowfields - Filenames of flowfields  
        job.K          - 2^K timesteps are used  
         
        Note that K needs to be reasonably large in order to obtain reasonable  
        Jacobian determinant fields.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_jacobian.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_jacobian", *args, **kwargs)
