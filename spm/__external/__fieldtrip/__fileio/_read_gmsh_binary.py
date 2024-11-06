from spm.__wrapper__ import Runtime


def _read_gmsh_binary(*args, **kwargs):
    """
      READ_GMSH_BINARY reads a gmsh .msh binary file. Current support is only  
        for version 2. There are some ASCII-readers floating around on the net,  
        but they do not seem to work with the primary use case in FieldTrip (and  
        the test data that I have available), which is SimNibs generated data.  
         
        See also MESH_LOAD_GMSH4  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_gmsh_binary.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_gmsh_binary", *args, **kwargs)
