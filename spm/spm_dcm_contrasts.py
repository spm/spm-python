from spm.__wrapper__ import Runtime


def spm_dcm_contrasts(*args, **kwargs):
    """
      Make contrast vector for a DCM  
        FORMAT con = spm_dcm_contrasts(DCM,D)  
         
        DCM    - DCM structure or its filename  
        D      - 'A','B' or 'C' i.e. connectivity matrix of interest  
         
        con    - column vector specifying contrast weights  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_contrasts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_contrasts", *args, **kwargs)
