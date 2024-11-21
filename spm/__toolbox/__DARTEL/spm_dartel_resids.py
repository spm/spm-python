from spm.__wrapper__ import Runtime


def spm_dartel_resids(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_resids.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_resids", *args, **kwargs)
