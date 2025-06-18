from mpython import Runtime


def _cellStruct2StructCell(*args, **kwargs):
    """
      Converts a cell-array of structure arrays into a structure array


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/cellStruct2StructCell.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cellStruct2StructCell", *args, **kwargs)
