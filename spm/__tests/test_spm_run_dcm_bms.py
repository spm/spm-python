from spm.__wrapper__ import Runtime


def test_spm_run_dcm_bms(*args, **kwargs):
    """
      Unit Tests for config/spm_run_dcm_bms. Tests are provided with and  
        without evidence for a particular model with artificially generated free  
        energies. Additionally, tests are included using real DCM files for  
        software testing.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_run_dcm_bms.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("test_spm_run_dcm_bms", *args, **kwargs)
