from spm._runtime import Runtime


def ft_headmodel_hbf(*args, **kwargs):
    r"""
      FT_HEADMODEL_HBF creates a volume conduction model of the head  
        using the boundary element method (BEM) for M/EEG. This function  
        takes as input the triangulated surfaces that describe the boundaries  
        and returns as output a volume conduction model which can be used  
        to compute leadfields.  
          
        The implementation of this function is based on Matti Stenroos' public  
        version of the Hesinki BEM Freamework hence the name "hbf".  
         
        Use as  
          headmodel = ft_headmodel_hbf(mesh, ...)  
         
        Optional input arguments should be specified in key-value pairs and can  
        include  
          conductivity     = 2 x n array, conductivity on inside and outside of  
                                      compartment  
          checkmesh        = 'yes' or 'no'  
          isolatedsource   = which compartment number should ISA apply to?   
                              DEFAULT: []  
         
        See also FT_PREPARE_HEADMODEL, FT_COMPUTE_LEADFIELD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/ft_headmodel_hbf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_headmodel_hbf", *args, **kwargs)
