from spm._runtime import Runtime


def spm_imshow(*args, **kwargs):
    r"""
      rendering of an RGB image sequence  
        FORMAT spm_imshow(I)  
         
        I(pixels x pixels x rgb x time)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_imshow.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_imshow", *args, **kwargs, nargout=0)
