from spm.__wrapper__ import Runtime


def spm_get_ons(*args, **kwargs):
    """
      Return input [designed effects] structure  
        FORMAT [U] = spm_get_ons(SPM,s)  
         
        SPM   - SPM structure (see spm_fMRI_design.m)  
        s     - session number  
         
        U     - (1 x n)   struct array of (n) trial-specific structures  
         
          U(i).name   - cell of names for each input or cause  
          U(i).u      - inputs or stimulus function matrix  
          U(i).dt     - time bin (seconds)  
          U(i).ons    - onsets    (in SPM.xBF.UNITS)  
          U(i).dur    - durations (in SPM.xBF.UNITS)  
          U(i).orth   - orthogonalise inputs?  
          U(i).P      - parameter structure  
         
              U(i).P(p).name - parameter name  
              U(i).P(p).P    - parameter vector  
              U(i).P(p).h    - order of polynomial expansion  
              U(i).P(p).i    - sub-indices of u pertaining to P  
       __________________________________________________________________________  
         
        Note on Slice Timing:  
         
        With longs TRs you may want to shift the regressors so that they are  
        aligned to a particular slice. This is controlled by two variables:  
        fMRI_T is the number of time-bins per scan used when building regressors.  
        Onsets are defined in temporal units of scans starting at 0.  
        fMRI_T0 is the first time-bin at which the regressors are resampled to   
        coincide with data acquisition. If fMRI_T0 is set to 1 then the   
        regressors will be appropriate for the first slice.  
        If you want to temporally realign the regressors so that they match  
        responses in the middle slice then make fMRI_T0 = fMRI_T/2 (assuming  
        there is a negligible gap between volume acquisitions).  
        Default values are defined in spm_defaults.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_ons.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_ons", *args, **kwargs)
