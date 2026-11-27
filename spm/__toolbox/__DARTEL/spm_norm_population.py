from spm._runtime import Runtime


def spm_norm_population(*args, **kwargs):
    r"""
      Obtain mapping from population average to ICBM space  
        FORMAT spm_norm_population(job)  
        job.template - name of population average template  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_norm_population.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_norm_population", *args, **kwargs)
