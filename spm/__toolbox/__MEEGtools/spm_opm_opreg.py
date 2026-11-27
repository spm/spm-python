from spm._runtime import Runtime


def spm_opm_opreg(*args, **kwargs):
    r"""
      Read magnetometer data and optionally set up forward model  
        FORMAT D = spm_opm_create(S)  
          S               - input structure  
        Optional fields of S:  
          S.headfile       - path to headshape file      - Default:required  
          S.helmetref1      - 3 x 3 matrix of 1st set ref points  - Default:required  
          S.headhelmetref1  - 3 x 3 matrix of 1st set ref points  - Default:required  
          S.headref2        - 3 x 3 matrix of 2st set ref points  - Default:required  
          S.headhelmetref2  - 3 x 3 matrix of 2st set ref points  - Default:required  
          S.fiducials       - 3 x 3 matrix of fiducials  - Default:required  
         
        1st set of ref points connects a helmet scan to the scan of participant with  
        a helmet   
        2st set of ref points connects the scan of participant with helmet to the scan  
        of participant without a helmet   
         
        Output:  
         tHelm       - transformed helmet object  
       __________________________________________________________________________  
        Copyright (C) 2018-2022 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_opreg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_opreg", *args, **kwargs)
