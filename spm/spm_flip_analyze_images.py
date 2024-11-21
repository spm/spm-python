from spm.__wrapper__ import Runtime


def spm_flip_analyze_images(*args, **kwargs):
    """
      Do Analyze format images need to be left-right flipped? The default  
        behaviour is to have the indices of the voxels stored as left-handed and  
        interpret the mm coordinates within a right-handed coordinate system.  
         
        Note: the behaviour used to be set in spm_defaults.m, but this has now  
        been changed.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_flip_analyze_images.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_flip_analyze_images", *args, **kwargs)
