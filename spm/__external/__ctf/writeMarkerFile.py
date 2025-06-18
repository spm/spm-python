from mpython import Runtime


def writeMarkerFile(*args, **kwargs):
    """
       Version 1.0   27 Oct. 2006


    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/writeMarkerFile.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("writeMarkerFile", *args, **kwargs, nargout=0)
