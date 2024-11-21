from spm.__wrapper__ import Runtime


def _cellStruct2StructCell(*args, **kwargs):
    """
      Converts a cell-array of structure arrays into a structure array  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/cellStruct2StructCell.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cellStruct2StructCell", *args, **kwargs)
