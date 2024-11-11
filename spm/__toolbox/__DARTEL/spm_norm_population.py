from spm.__wrapper__ import Runtime


def spm_norm_population(*args, **kwargs):
    """
      Obtain mapping from population average to ICBM space  
        FORMAT spm_norm_population(job)  
        job.template - name of population average template  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_norm_population.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_norm_population", *args, **kwargs)
