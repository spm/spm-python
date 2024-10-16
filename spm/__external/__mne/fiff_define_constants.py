from spm.__wrapper__ import Runtime


def fiff_define_constants(*args, **kwargs):
  """  Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>  
             Matti Hämäläinen <msh@nmr.mgh.harvard.edu>  
     
    License: BSD-3-Clause  
    Copyright the MNE-Python contributors.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_define_constants.m)
  """

  return Runtime.call("fiff_define_constants", *args, **kwargs)
