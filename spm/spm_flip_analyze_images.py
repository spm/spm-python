from spm._runtime import Runtime


def spm_flip_analyze_images(*args, **kwargs):
    r"""
      Do Analyze format images need to be left-right flipped? The default  
        behaviour is to have the indices of the voxels stored as left-handed and  
        interpret the mm coordinates within a right-handed coordinate system.  
         
        Note: the behaviour used to be set in spm_defaults.m, but this has now  
        been changed.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_flip_analyze_images.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_flip_analyze_images", *args, **kwargs)
