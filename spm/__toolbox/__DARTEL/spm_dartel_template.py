from spm.__wrap__ import _Runtime


def spm_dartel_template(*args, **kwargs):
  """  Iteratively compute a template with mean shape and intensities  
    FORMAT spm_dartel_template(job)  
     
    The outputs are flow fields, and a series of Template images.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_template.m)
  """

  return _Runtime.call("spm_dartel_template", *args, **kwargs)
