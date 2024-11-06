from spm.__wrapper__ import Runtime


def _write_ply(*args, **kwargs):
    """
      WRITE_PLY writes triangles, tetraheders or hexaheders to a Stanford *.ply format file  
         
        Use as  
          write_ply(filename, vertex, element)  
         
        Documentation is provided on  
          http://paulbourke.net/dataformats/ply/  
          http://en.wikipedia.org/wiki/PLY_(file_format)  
         
        See also READ_PLY, READ_VTK, WRITE_VTK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_ply.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_ply", *args, **kwargs, nargout=0)
