from spm.__wrapper__ import Runtime


def ft_headmodel_bemcp(*args, **kwargs):
    """
      FT_HEADMODEL_BEMCP creates a volume conduction model of the head  
        using the boundary element method (BEM) for EEG. This function  
        takes as input the triangulated surfaces that describe the boundaries  
        and returns as output a volume conduction model which can be used  
        to compute leadfields.  
         
        The implementation of this function is based on Christophe Phillips'  
        MATLAB code, hence the name "bemcp".  
         
        Use as  
          headmodel = ft_headmodel_bemcp(mesh, ...)  
         
        Optional input arguments should be specified in key-value pairs and can  
        include  
          conductivity     = vector, conductivity of each compartment  
          checkmesh        = 'yes' or 'no'  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_bemcp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_bemcp", *args, **kwargs)
