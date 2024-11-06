from spm.__wrapper__ import Runtime


def _read_asa_bnd(*args, **kwargs):
    """
      READ_ASA_BND reads an ASA boundary triangulation file  
        converting the units of the vertices to mm  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_bnd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_asa_bnd", *args, **kwargs)
