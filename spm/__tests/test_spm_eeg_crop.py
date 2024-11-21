from spm.__wrapper__ import Runtime


def test_spm_eeg_crop(*args, **kwargs):
    """
      Unit Tests for spm_eeg_crop  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_eeg_crop.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("test_spm_eeg_crop", *args, **kwargs)
