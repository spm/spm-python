from spm.__wrapper__ import Runtime


def ft_inverse_rv(*args, **kwargs):
    """
      FT_INVERSE_RV scan with a single dipole and computes the residual variance  
        at each dipole location.  
         
        Use as  
          [estimate] = ft_inverse_rv(sourcemodel, sens, headmodel, dat, ...)  
        where  
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL  
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS  
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL  
          dat         is the data matrix with the ERP or ERF  
        and  
          estimate    contains the estimated source parameters  
         
        Additional input arguments should be specified as key-value pairs and can include  
          'feedback'         = can be 'none', 'gui', 'dial', 'textbar', 'text', 'textcr', 'textnl' (default = 'text')  
         
        These options influence the forward computation of the leadfield  
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/ft_inverse_rv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_rv", *args, **kwargs)
