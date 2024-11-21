from spm.__wrapper__ import Runtime


def _read_vtk(*args, **kwargs):
    """
      READ_VTK reads a triangulation from a VTK (Visualisation ToolKit) format file  
        Supported are triangles and other polygons.  
         
        Use as  
          [pnt, tri] = read_vtk(filename)  
         
        See also WRITE_VTK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_vtk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_vtk", *args, **kwargs)
