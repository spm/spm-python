from spm._runtime import Runtime


def spm_dartel_resids(*args, **kwargs):
    r"""
      Generate residuals in a form suitable for generating a Fisher kernel  
        FORMAT spm_dartel_residuals(job)  
        job.flowfields  
        job.images  
        job.template  
        job.K  
         
        The aim is to obtain better pattern recognition through using  
        Fisher kernels.  See  Bishop's PRML or the work of Jaakkola and  
        Haussler for more information.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_resids.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_resids", *args, **kwargs)
