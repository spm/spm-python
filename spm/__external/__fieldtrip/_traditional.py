from spm.__wrapper__ import Runtime


def _traditional(*args, **kwargs):
    """
      TRADITIONAL creates the homogenous spatial transformation matrix  
        for a 9 parameter traditional "Talairach-model" transformation  
         
        Use as  
          [H] = traditional(f)  
         
        The transformation vector f should contain the   
          x-shift  
          y-shift  
          z-shift  
        followed by the  
          pitch (rotation around x-axis)  
          roll  (rotation around y-axis)  
          yaw   (rotation around z-axis)  
        followed by the   
          x-rescaling factor  
          y-rescaling factor  
          z-rescaling factor  
         
        The order in which the transformations are done is exactly opposite as  
        the list above, i.e. first z-rescale, ... and finally x-shift.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/traditional.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("traditional", *args, **kwargs)
