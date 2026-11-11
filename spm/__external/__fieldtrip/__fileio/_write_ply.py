from spm._runtime import Runtime


def _write_ply(*args, **kwargs):
    r"""
      WRITE_PLY writes triangles, tetrahedrons or hexahedrons to a Stanford *.ply format file  
         
        Use as  
          write_ply(filename, vertex, element)  
         
        Documentation is provided on  
          http://paulbourke.net/dataformats/ply/  
          http://en.wikipedia.org/wiki/PLY_(file_format)  
         
        See also READ_PLY, READ_VTK, WRITE_VTK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_ply.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_ply", *args, **kwargs, nargout=0)
