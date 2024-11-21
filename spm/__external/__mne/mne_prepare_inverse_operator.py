from spm.__wrapper__ import Runtime


def mne_prepare_inverse_operator(*args, **kwargs):
    """
       
        [inv] = mne_prepare_inverse_operator(orig,nave,lambda2,dSPM,sLORETA)  
         
        Prepare for actually computing the inverse  
         
        orig        - The inverse operator structure read from a file  
        nave        - Number of averages (scales the noise covariance)  
        lambda2     - The regularization factor  
        dSPM        - Compute the noise-normalization factors for dSPM?  
        sLORETA     - Compute the noise-normalization factors for sLORETA?  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_prepare_inverse_operator.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_prepare_inverse_operator", *args, **kwargs)
