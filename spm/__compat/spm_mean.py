from spm.__wrapper__ import Runtime


def spm_mean(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_mean.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mean", *args, **kwargs, nargout=0)
