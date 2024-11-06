from spm.__wrapper__ import Runtime


def _write_vtk(*args, **kwargs):
    """
      WRITE_VTK writes a mesh to a VTK (Visualisation ToolKit) format file.  
        Supported are triangles, tetraheders and hexaheders.  
         
        Use as  
          write_vtk(filename, pos, tri, val)  
          write_vtk(filename, pos, tet, val)  
          write_vtk(filename, pos, hex, val)  
        where pos describes the vertex positions and tri/tet/hex describe the connectivity  
        of the surface or volume elements.   
          
        The optional val argument can be used to write scalar or vector values for  
        each vertex or element.  
         
        See also READ_VTK, WRITE_PLY  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_vtk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_vtk", *args, **kwargs, nargout=0)
