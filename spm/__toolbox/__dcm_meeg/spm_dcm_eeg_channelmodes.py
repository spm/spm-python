from spm.__wrapper__ import Runtime


def spm_dcm_eeg_channelmodes(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_eeg_channelmodes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_eeg_channelmodes", *args, **kwargs)
