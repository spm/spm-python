from spm.__wrapper__ import Runtime


def ft_write_headshape(*args, **kwargs):
    """
      FT_WRITE_HEADSHAPE writes a head surface, cortical sheet or geometrical descrition  
        of the volume conduction model or source model to a file for further processing in  
        external software.  
         
        Use as  
          ft_write_headshape(filename, mesh, ...)  
        or  
          ft_write_headshape(filename, pos, ...)  
        where the input mesh is a structure containing the vertices and triangles (mesh.pos  
        and mesh.tri), or where the input pos is a Nx3 matrix that describes the surface  
        vertices.  
         
        Required input arguments should be specified as key-value pairs and should include  
          'format'		   = string, see below  
         
        Optional input arguments should be specified as key-value pairs and can include  
          'data'         = data vector or matrix, the size along the 1st dimension should correspond to the number of vertices  
          'unit'         = string, desired geometrical units for the data, for example 'mm'  
          'coordsys'     = string, desired coordinate system for the data  
          'jmeshopt'     = cell-array with {'name', 'value'} pairs, options for writing JSON/JMesh files  
         
        Supported output formats are  
          'freesurfer'      Freesurfer surf-file format, using write_surf from FreeSurfer  
          'gifti'           see https://www.nitrc.org/projects/gifti/  
          'gmsh_ascii'      see https://gmsh.info  
          'gmsh_binary'     see https://gmsh.info  
          'mne_pos'         MNE source grid in ascii format, described as 3D points  
          'mne_tri'         MNE surface desciption in ascii format  
          'neurojson_bmesh' NeuroJSON binary JSON-based format  
          'neurojson_jmesh' NeuroJSON ascii JSON-based format  
          'off'             see http://www.geomview.org/docs/html/OFF.html  
          'ply'             Stanford Polygon file format, for use with Paraview or Meshlab  
          'stl'             STereoLithography file format, for use with CAD and generic 3D mesh editing programs  
          'tetgen'          see https://wias-berlin.de/software/tetgen/  
          'vista'           see http://www.cs.ubc.ca/nest/lci/vista/vista.html  
          'vtk'             Visualization ToolKit file format, for use with Paraview  
         
        See also FT_READ_HEADSHAPE, FT_WRITE_DATA, FT_WRITE_MRI, FT_WRITE_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_headshape.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_write_headshape", *args, **kwargs, nargout=0)
