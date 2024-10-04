from spm.__wrap__ import _Runtime


def test_spm_run_dcm_bms(*args, **kwargs):
  """  Unit Tests for config/spm_run_dcm_bms. Tests are provided with and  
    without evidence for a particular model with artificially generated free  
    energies. Additionally, tests are included using real DCM files for  
    software testing.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_run_dcm_bms.m)
  """

  return _Runtime.call("test_spm_run_dcm_bms", *args, **kwargs)
