from spm._runtime import Runtime


def spm_dcm_voi(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_voi.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_voi", *args, **kwargs)
