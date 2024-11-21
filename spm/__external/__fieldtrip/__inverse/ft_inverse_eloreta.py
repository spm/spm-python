from spm.__wrapper__ import Runtime


def ft_inverse_eloreta(*args, **kwargs):
    """
      FT_INVERSE_ELORETA estimates the source activity using eLORETA  
         
        Use as  
          [estimate] = ft_inverse_eloreta(sourcemodel, sens, headmodel, dat, cov, ...)  
        where  
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL  
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS  
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL  
          dat         is the data matrix with the ERP or ERF  
          cov         is the data covariance or cross-spectral density matrix  
        and  
          estimate    contains the estimated source parameters  
         
        Additional input arguments should be specified as key-value pairs and can include  
          'keepfilter'       = remember the spatial filter,    can be 'yes' or 'no'  
          'keepleadfield'    = remember the forward computation,  can be 'yes' or 'no'  
          'keepmom'          = remember the dipole moment,        can be 'yes' or 'no'  
          'lambda'           = scalar, regularisation parameter (default = 0.05)  
         
        These options influence the forward computation of the leadfield  
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        If the dipole definition only specifies the dipole location, a rotating dipole  
        (regional source) is assumed on each location. If a dipole moment is specified, its  
        orientation will be used and only the strength will be fitted to the data.  
         
        This implements:   
        - R.D. Pascual-Marqui; Discrete, 3D distributed, linear imaging methods of electric  
          neuronal activity. Part 1: exact, zero error localization. arXiv:0710.3341   
          2007-October-17, http://arxiv.org/pdf/0710.3341  
         
        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/ft_inverse_eloreta.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_eloreta", *args, **kwargs)
