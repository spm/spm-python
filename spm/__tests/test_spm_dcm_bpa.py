from spm.__wrapper__ import Runtime


def test_spm_dcm_bpa(*args, **kwargs):
    """
      Unit Tests for spm_cfg_dcm_peb (PEB batch)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_dcm_bpa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("test_spm_dcm_bpa", *args, **kwargs)
