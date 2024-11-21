from spm.__wrapper__ import Runtime


def ft_headmodel_duneuro(*args, **kwargs):
    """
      FT_HEADMODEL_DUNEURO creates a volume conduction model of the head  
        using the finite element method (FEM) for EEG and MEG. Different source models  
        are implemented, including the St. Venant, the subtraction and partial  
        integration model. This function takes as input a mesh with tetrahedral  
        or hexahedral elements and corresponding conductivities and returns  
        as output a volume conduction model which can be used to compute EEG/MEG  
        leadfields.  
         
        Use as  
          headmodel = ft_headmodel_duneuro(mesh,'conductivity', conductivities, ...)  
          headmodel = ft_headmodel_duneuro(mesh,'grid_filename', grid_filename, 'tensors_filename', tensors_filename, ...)  
         
        Required input arguments should be specified in key-value pairs and have  
        to include either  
          grid_filename   = string, filename for grid in "msh" fileformat (see here: https://gmsh.info/doc/texinfo/gmsh.html#File-formats)  
          tensors_filename= string, filename for conductivities, txt file with conductivity values  
         
        or  
          conductivity    = vector, conductivity values for tissues  
         
        Optional input arguments are passed with  
          duneuro_settings = (optional) struct, which can contain the following fields  
         
          type            = string, 'fitted' (default)  
          solver_type     = string, 'cg' (default)  
          electrodes      = string, 'closest_subentity_center' (default)  
          subentities     = string, e.g. '1 2 3' (default) or '3'  
          forward         = string, 'venant' (default), 'partial_integration'  
          intorderadd     = string, e.g. '2' (default)  
          intorderadd_lb  = string, e.g. '2' (default)  
          initialization  = string, e.g. 'closest_vertex' (default)  
          numberOfMoments = string, e.g. '3' (default)  
          referenceLength = string, e.g. '20' (default)  
          relaxationFactor= string, e.g. '1e-6' (default)  
          restrict        = string, e.g. 'true' (default)  
          weightingExponent= string, e.g. '1' (default)  
          post_process    = string, e.g. 'true' (default)  
          subtract_mean   = string, e.g. 'true' (default)  
          reduction       = string, e.g. '1e-10' (default)  
          intorderadd_meg = integer, e.g.'0' (default)  
          mixedMoments    = logical, e.g. 'true' (default)  
          meg_type        = string, e.g. 'physical' (default)  
          meg_eneablecache= logical, e.g. 'false (default)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_duneuro.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_duneuro", *args, **kwargs)
