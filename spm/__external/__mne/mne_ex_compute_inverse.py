from spm._runtime import Runtime


def mne_ex_compute_inverse(*args, **kwargs):
    r"""
       
        [res] = mne_ex_compute_inverse(fname_data,setno,fname_inv,nave,lambda2,dSPM,sLORETA)  
         
        An example on how to compute a L2-norm inverse solution  
        Actual code using these principles might be different because   
        the inverse operator is often reused across data sets.  
         
         
        fname_data  - Name of the data file  
        setno       - Data set number  
        fname_inv   - Inverse operator file name  
        nave        - Number of averages (scales the noise covariance)  
                      If negative, the number of averages in the data will be  
                      used  
        lambda2     - The regularization factor  
        dSPM        - do dSPM?  
        sLORETA     - do sLORETA?  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_compute_inverse.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_compute_inverse", *args, **kwargs)
