from spm._runtime import Runtime


def test_spm_gamrnd(*args, **kwargs):
    """
      Unit Tests for spm_gamrnd  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_gamrnd.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_gamrnd", *args, **kwargs)
