from spm._runtime import Runtime


def writeMarkerFile(*args, **kwargs):
    r"""
       Version 1.0   27 Oct. 2006  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/writeMarkerFile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("writeMarkerFile", *args, **kwargs, nargout=0)
