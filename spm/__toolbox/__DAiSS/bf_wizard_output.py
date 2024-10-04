from spm.__wrap__ import _Runtime


def bf_wizard_output(*args, **kwargs):
  """  A handy command-line based batch filler with some defaults for DAiSS  
    output module, pick a few options, and it will default for unpopulated  
    fields  
     
    Current *definitely* supported output methods include:  
      - image_dics  
      - image_mv  
      - image_power  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_output.m)
  """

  return _Runtime.call("bf_wizard_output", *args, **kwargs)
