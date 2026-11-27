from spm._runtime import Runtime


def ft_headmodel_duneuro(*args, **kwargs):
    r"""
      FT_HEADMODEL_DUNEURO creates a volume conduction model of the head using the finite element method (FEM) for EEG and MEG.  
        Different source models are implemented, including the St. Venant, the subtraction and partial integration model. This   
        function takes as input a mesh with tetrahedral or hexahedral elements and corresponding conductivities and returns  
        as output a volume conduction model which can be used to compute EEG/MEG leadfields.  
         
        Use as  
          headmodel = ft_headmodel_duneuro(mesh,'conductivity', conductivities, ...)  
          headmodel = ft_headmodel_duneuro(mesh,'grid_filename', grid_filename, 'tensors_filename', tensors_filename, ...)  
         
        Required input arguments should be specified in key-value pairs and have to include either  
          grid_filename   = string, filename for grid in "msh" fileformat (see here: https://gmsh.info/doc/texinfo/gmsh.html#File-formats)  
          tensors_filename= string, filename for conductivities, txt file with conductivity values  
        or  
          conductivity    = vector, conductivity values for tissues  
          
        if a pair of filenames is provided, the input mesh is not considered, but will be generated from the grid_filename  
          
        In addition, an optional struct with configuration options can be provided, which can specify the options  
        related to the functional behavior of the duneuro software. See DUNEURO_DEFAULTS for the configureable options, and   
        their default values.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/ft_headmodel_duneuro.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_headmodel_duneuro", *args, **kwargs)
