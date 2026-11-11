from spm._runtime import Runtime


def _surf_to_tetgen(*args, **kwargs):
    r"""
      This function converts a triangulated mesh in FieldTrip format into a  
        surface structure readable by Tetgen software  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/surf_to_tetgen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("surf_to_tetgen", *args, **kwargs, nargout=0)
