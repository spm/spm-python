from spm.__wrapper__ import Runtime


def spm_opm_opreg(*args, **kwargs):
  """  Read magnetometer data and optionally set up forward model  
    FORMAT D = spm_opm_create(S)  
      S               - input structure  
    Optional fields of S:  
      S.headfile     - path to headshape file      - Default:required  
      S.helmetref      - 3 x 3 matrix of fiducials  - Default:required  
      S.headhelmetref  - 3 x 3 matrix of fiducials  - Default:required  
      S.headfid        - 3 x 3 matrix of fiducials  - Default:required  
      S.headhelmetfid  - 3 x 3 matrix of fiducials  - Default:required  
    Output:  
     tHelm       - transformed helmet object  
   __________________________________________________________________________  
    Copyright (C) 2018-2022 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_opreg.m)
  """

  return Runtime.call("spm_opm_opreg", *args, **kwargs)
