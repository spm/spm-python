from spm._runtime import Runtime


def ft_headlight(*args, **kwargs):
    r"""
      FT_HEADLIGHT places a light along the direction of the camera and updates the light  
        position as you rotate the scene and the camera view point changes.  
         
        Use as  
          surf(peaks);  
          ft_headlight;  
         
        See https://stackoverflow.com/questions/30921003/matlab-how-to-make-camera-light-follow-3d-rotation  
         
        See also CAMLIGHT, ROTATE3D  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/ft_headlight.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_headlight", *args, **kwargs, nargout=0)
