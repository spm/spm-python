from spm._runtime import Runtime


def _read_vtk(*args, **kwargs):
    r"""
      READ_VTK reads a triangulation from a VTK (Visualisation ToolKit) format file.  
        Supported are triangles, triangle strips, and other polygons.  
         
        Use as  
          [pnt, tri] = read_vtk(filename)  
         
        See https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html  
        and https://www.princeton.edu/~efeibush/viscourse/vtk.pdf  
         
        See also WRITE_VTK, READ_VTK_XML  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_vtk.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_vtk", *args, **kwargs)
