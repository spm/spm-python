from spm.__wrapper__ import Runtime


def _read_off(*args, **kwargs):
    """
      READ_OFF reads vertices and triangles from a OFF format triangulation file  
         
        [pnt, tri] = read_off(filename)  
         
        See also READ_TRI, READ_BND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_off.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_off", *args, **kwargs)
