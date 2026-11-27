from spm._runtime import Runtime


def _read_stl(*args, **kwargs):
    r"""
      READ_STL reads a triangulation from an ascii or binary *.stl file, which  
        is a file format native to the stereolithography CAD software created by  
        3D Systems.  
         
        Use as  
          [pnt, tri, nrm] = read_stl(filename)  
         
        The format is described at http://en.wikipedia.org/wiki/STL_(file_format)  
         
        See also WRITE_STL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_stl.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_stl", *args, **kwargs)
