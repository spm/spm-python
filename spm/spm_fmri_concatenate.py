from spm.__wrapper__ import Runtime


def spm_fmri_concatenate(*args, **kwargs):
    """
      Adjust an SPM.mat which has concatenated sessions  
        FORMAT spm_fmri_concatenate(P, scans)  
        Session regressors are added and the high-pass filter and non-sphericity  
        estimates adjusted as if sessions are separate.  
         
        P     - filename of the SPM.mat file to adjust  
        scans - [1 x n] vector with the original number of scans in each session  
         
        The expected workflow is:  
         
        1. Manually specify a GLM with timeseries and onsets concatenated  
        2. Run spm_post_concatenate on the saved SPM.mat.  
        3. Estimate the SPM.mat in the normal way.  
         
        Tips:  
         
        - The BOLD-response may overhang from one session to the next. To reduce  
          this, acquire additional volumes at the end of each session and / or  
          add regressors to model the trials at the session borders.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fmri_concatenate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fmri_concatenate", *args, **kwargs)
