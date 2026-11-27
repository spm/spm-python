from spm._runtime import Runtime


def spm_eeg_test_coverage(*args, **kwargs):
    r"""
      Return number of M/EEG functions and number of associated tests  
        FORMAT [coverage, tocover] = spm_eeg_test_coverage  
         
        Output:  
          coverage - number of M/EEG tested functions  
          tocover  - number of M/EEG functions   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/spm_eeg_test_coverage.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_test_coverage", *args, **kwargs)
