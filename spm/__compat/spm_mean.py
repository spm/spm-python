from spm.__wrap__ import _Runtime


def spm_mean(*args, **kwargs):
  """  Compute a mean image from a set  
    FORMAT spm_mean(P)  
    P   - list of images to average [Default: GUI]  
   __________________________________________________________________________  
     
    spm_mean_ui simply averages a set of images to produce a mean image  
    that is written as type int16 to "mean.img" (in the current directory).  
     
    The images must have the same dimensions, orientations and the same  
    voxel sizes.  
     
    This is not a "softmean" - zero voxels are treated as zero.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/compat/spm_mean.m)
  """

  return _Runtime.call("spm_mean", *args, **kwargs, nargout=0)
