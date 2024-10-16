from spm.__wrapper__ import Runtime


def fil_install(*args, **kwargs):
  """  Download files required for Factorisation-based Image Labelling  
    FORMAT [mufile,filfile] = fil_install(datadir)  
     
    https://figshare.com/projects/Factorisation-based_Image_Labelling/128189  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/fil_install.m)
  """

  return Runtime.call("fil_install", *args, **kwargs)
