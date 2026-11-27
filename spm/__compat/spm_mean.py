from spm._runtime import Runtime


def spm_mean(*args, **kwargs):
    r"""
      Compute a mean image from a set  
        FORMAT spm_mean(P)  
        P   - list of images to average [Default: GUI]  
       __________________________________________________________________________  
         
        spm_mean_ui simply averages a set of images to produce a mean image  
        that is written as type int16 to "mean.img" (in the current directory).  
         
        The images must have the same dimensions, orientations and the same  
        voxel sizes.  
         
        This is not a "softmean" - zero voxels are treated as zero.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_mean.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mean", *args, **kwargs, nargout=0)
