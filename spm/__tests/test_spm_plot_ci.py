from spm.__wrapper__ import Runtime


def test_spm_plot_ci(*args, **kwargs):
  """  Unit Tests for spm_plot_ci  
    Ensures that all the different plot types run without error  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_plot_ci.m)
  """

  return Runtime.call("test_spm_plot_ci", *args, **kwargs)
