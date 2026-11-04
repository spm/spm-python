from spm._runtime import Runtime


def _browse_simpleFFT(*args, **kwargs):
    r"""
      BROWSE_SIMPLEFFT is a helper function for FT_DATABROWSER that shows a  
        simple FFT of the data.  
         
        Included are a button to switch between log and non-log space, and a  
        selection button to deselect channels, for the purpose of zooming in on  
        bad channels.  
         
        See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/browse_simpleFFT.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("browse_simpleFFT", *args, **kwargs, nargout=0)
