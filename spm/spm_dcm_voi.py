from spm.__wrapper__ import Runtime


def spm_dcm_voi(*args, **kwargs):
    """
      Insert new regions into a DCM  
        FORMAT DCM = spm_dcm_voi(DCM,VOIs)  
         
        DCM   - DCM structure or its filename  
        VOIs  - cell array of new VOI filenames   
                eg. {'VOI_V1','VOI_V5','VOI_SPC'}  
         
        The TR, TE and delays are assumed to be the same as before.  
         
        This function can be used, for example, to replace subject X's data by   
        subject Y's. The model can then be re-estimated without having to go   
        through model specification again.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_voi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_voi", *args, **kwargs)
