from spm._runtime import Runtime


def _cellStruct2StructCell(*args, **kwargs):
    r"""
      Converts a cell-array of structure arrays into a structure array  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/cellStruct2StructCell.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cellStruct2StructCell", *args, **kwargs)
