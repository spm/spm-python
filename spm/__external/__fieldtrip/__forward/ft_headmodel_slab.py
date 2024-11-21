from spm.__wrapper__ import Runtime


def ft_headmodel_slab(*args, **kwargs):
    """
      FT_HEADMODEL_SLAB creates an EEG volume conduction model that  
        is described with an infinite conductive slab. You can think  
        of this as two parallel planes containing a mass of conductive  
        material (e.g. water) and externally to them a non-conductive material  
        (e.g. air).  
         
        Use as  
          headmodel = ft_headmodel_slab(mesh1, mesh2, Pc, varargin)  
        where  
          mesh1.pos = Nx3 vector specifying N points through which the 'upper' plane is fitted   
          mesh2.pos = Nx3 vector specifying N points through which the 'lower' plane is fitted   
          Pc        = 1x3 vector specifying the spatial position of a point lying in the conductive slab   
                     (this determines the plane's normal's direction)  
          
        Optional arguments should be specified in key-value pairs and can include  
          'sourcemodel'  = 'monopole'   
          'conductivity' = number ,  conductivity value of the conductive halfspace (default = 1)  
          
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_slab.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_slab", *args, **kwargs)
