from spm._runtime import Runtime


def spm_dcm_eeg_channelmodes(*args, **kwargs):
    r"""
      Return the channel eigenmodes  
        FORMAT [U] = spm_dcm_eeg_channelmodes(dipfit,Nm)  
        FORMAT [U] = spm_dcm_eeg_channelmodes(dipfit,Nm,xY)  
        dipfit  - spatial model specification  
        Nm      - number of modes required (upper bound)  
        xY      - data structure  
        U       - channel eigenmodes  
       __________________________________________________________________________  
         
        Uses SVD (an eigensolution) to identify the patterns with the greatest   
        prior covariance; assuming independent source activity in the specified   
        spatial (forward) model.   
         
        if xY is specifed a CVA (a generalised eigensolution) will be used to   
        find the spatial modes that are best by the spatial model  
         
        U is scaled to ensure trace(U'*L*L'*U) = Nm  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_dcm_eeg_channelmodes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_eeg_channelmodes", *args, **kwargs)
