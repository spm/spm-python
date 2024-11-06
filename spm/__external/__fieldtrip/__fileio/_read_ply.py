from spm.__wrapper__ import Runtime


def _read_ply(*args, **kwargs):
    """
      READ_PLY reads triangles, tetraheders or hexaheders from a Stanford *.ply file  
         
        Use as  
          [vert, face, prop, face_prop] = read_ply(filename)  
         
        Documentation is provided on  
          http://paulbourke.net/dataformats/ply/  
          http://en.wikipedia.org/wiki/PLY_(file_format)  
         
        See also WRITE_PLY, WRITE_VTK, READ_VTK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ply.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ply", *args, **kwargs)
