from spm._runtime import Runtime


def _read_ply(*args, **kwargs):
    r"""
      READ_PLY reads triangles, tetrahedrons or hexahedrons from a Stanford *.ply file  
         
        Use as  
          [vert, face, prop, face_prop] = read_ply(filename)  
         
        Documentation is provided on  
          http://paulbourke.net/dataformats/ply/  
          http://en.wikipedia.org/wiki/PLY_(file_format)  
         
        See also WRITE_PLY, WRITE_VTK, READ_VTK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ply.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ply", *args, **kwargs)
