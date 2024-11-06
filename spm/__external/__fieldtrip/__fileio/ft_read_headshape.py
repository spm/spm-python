from spm.__wrapper__ import Runtime


def ft_read_headshape(*args, **kwargs):
    """
      FT_READ_HEADSHAPE reads the fiducials and/or the measured headshape and/or meshes  
        that describe headsurfaces, headmodels or cortical sheets from a variety of files  
        (like CTF and Polhemus). The headshape and fiducials can for example be used for  
        coregistration.  
         
        Use as  
          [shape] = ft_read_headshape(filename, ...)  
        or  
          [shape] = ft_read_headshape({filename1, filename2}, ...)  
         
        If you specify the filename as a cell-array, the following situations are supported:  
         - a two-element cell-array with the file names for the left and right hemisphere,  
           e.g., FreeSurfer's {'lh.orig' 'rh.orig'}, or Caret's {'X.L.Y.Z.surf.gii' 'X.R.Y.Z.surf.gii'}  
         - a two-element cell-array points to files that represent the coordinates and topology  
           in separate files, e.g., Caret's {'X.L.Y.Z.coord.gii' 'A.L.B.C.topo.gii'}  
        By default all information from the two files will be assumed to correspond to the  
        left and right hemispeheres and concatenated. The option 'concatenate' can be set  
        to 'no' to prevent them from being concatenated in a single structure.  
         
        Additional options should be specified in key-value pairs and can include  
          'format'      = string, see below  
          'coordsys'    = string, e.g. 'head' or 'dewar' (only supported for CTF)  
          'unit'        = string, e.g. 'mm' (default is the native units of the file)  
          'concatenate' = 'yes' or 'no' (default = 'yes')  
          'image'       = path to corresponding image/jpg file  
          'surface'     = specific surface to be read (only for Caret spec files)  
          'refine'      = number, used for refining Structure Sensor meshes (default = 1)  
          'jmeshopt'    = cell-array with {'name', 'value'} pairs, options for reading JSON/JMesh files  
         
        Supported input file formats include  
          'gifti'           see https://www.nitrc.org/projects/gifti/  
          'gmsh_ascii'      see https://gmsh.info  
          'gmsh_binary'     see https://gmsh.info  
          'matlab'          containing FieldTrip or BrainStorm headshapes or cortical meshes  
          'mne_tri'         MNE surface description in ASCII format  
          'mne_pos'         MNE source grid in ascii format, described as 3D points  
          'neurojson_jmesh' NeuroJSON ascii JSON-based format  
          'neurojson_bmesh' NeuroJSON binary JSON-based format  
          'obj'             Wavefront .obj file obtained with the Structure Sensor  
          'off'             see http://www.geomview.org/docs/html/OFF.html  
          'ply'             Stanford Polygon file format, for use with Paraview or Meshlab  
          'stl'             STereoLithography file format, for use with CAD and/or generic 3D mesh editing programs  
          'tck'             Mrtrix track file  
          'trk'             Trackvis trk file  
          'vista'           see http://www.cs.ubc.ca/nest/lci/vista/vista.html  
          'vtk'             Visualization ToolKit file format, for use with Paraview  
          'vtk_xml'         Visualization ToolKit file format  
          'itab_asc'  
          'ctf_*'  
          '4d_*'  
          'neuromag_*'  
          'yokogawa_*'  
          'yorkinstruments_hdf5'  
          'polhemus_*'  
          'freesurfer_*'  
          'mne_source'  
          'spmeeg_mat'  
          'netmeg'  
          'tet'  
          'tetgen_ele'  
          'caret_surf'  
          'caret_coord'  
          'caret_topo'  
          'caret_spec'  
          'brainvisa_mesh'  
          'brainsuite_dfs'  
         
        See also FT_READ_HEADMODEL, FT_READ_SENS, FT_READ_ATLAS, FT_WRITE_HEADSHAPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_headshape.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_headshape", *args, **kwargs)
