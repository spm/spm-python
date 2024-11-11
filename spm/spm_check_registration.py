from spm.__wrapper__ import Runtime


def spm_check_registration(*args, **kwargs):
    """
      A visual check of image registration quality  
        FORMAT spm_check_registration  
        FORMAT spm_check_registration(images)  
        Orthogonal views of one or more images are displayed. Clicking in  
        any image moves the centre of the orthogonal views. Images are  
        shown in orientations relative to that of the first selected image.  
        The first specified image is shown at the top-left, and the last at  
        the bottom right. The fastest increment is in the left-to-right  
        direction (the same as you are reading this).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_check_registration.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_check_registration", *args, **kwargs, nargout=0)
