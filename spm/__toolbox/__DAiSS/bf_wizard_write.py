from spm.__wrapper__ import Runtime


def bf_wizard_write(*args, **kwargs):
  """  A handy command-line based batch filler with some defaults for DAiSS  
    write module, pick a few options, and it will default for unpopulated  
    fields  
     
    Currently supported output methods include:  
      - nifti (for volumetric data)  
      - gifti (for surface data)  
      - spmmeeg (for virtual electrodes)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_write.m)
  """

  return Runtime.call("bf_wizard_write", *args, **kwargs)
