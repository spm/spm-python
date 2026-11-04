from spm._runtime import Runtime


def spm_deformations(*args, **kwargs):
    r"""
      Various deformation field utilities  
        FORMAT out = spm_deformations(job)  
        job - a job created via spm_cfg_deformations.m  
        out - a struct with fields  
              .def    - file name of created deformation field  
              .warped - file names of warped images  
         
        See spm_cfg_deformations.m for more information.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_deformations.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_deformations", *args, **kwargs)
