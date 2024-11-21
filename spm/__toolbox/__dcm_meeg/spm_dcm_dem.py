from spm.__wrapper__ import Runtime


def spm_dcm_dem(*args, **kwargs):
    """
      Estimate parameters of a DCM-DEM model  
        FORMAT DCM = spm_dcm_dem(DCM)  
         
        DCM  
           name: name string  
              Lpos:  Source locations  
              xY:    data   [1x1 struct]  
              xU:    design [1x1 struct]  
         
          Sname: cell of source name strings  
         
          options.trials       - indices of trials  
          options.Lpos         - source location priors  
          options.Tdcm         - [start end] time window in ms  
          options.D            - time bin decimation       (usually 1 or 2)  
          options.h            - number of DCT drift terms (usually 1 or 2)  
          options.Nmodes       - number of spatial models to invert  
          options.spatial      - 'ERP', 'LFP' or 'IMG'  
          options.onset        - stimulus onset (ms)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_dem.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_dem", *args, **kwargs)
