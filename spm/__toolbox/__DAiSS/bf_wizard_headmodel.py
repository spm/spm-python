from spm.__wrap__ import _Runtime


def bf_wizard_headmodel(*args, **kwargs):
  """  A handy command-line based batch filler with some defaults for SPM  
    head model specification for MEEG data. Will generate the job which  
    performs coregistration between the data and the MRI  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_headmodel.m)
  """

  return _Runtime.call("bf_wizard_headmodel", *args, **kwargs)
