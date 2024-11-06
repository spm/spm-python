from spm.__wrapper__ import Runtime


def ft_inverse_dipolefit(*args, **kwargs):
    """
      FT_INVERSE_DIPOLEFIT performs an equivalent current dipole fit with a single  
        or a small number of dipoles to explain an EEG or MEG scalp topography.  
         
        Use as  
          [estimate] = ft_inverse_dipolefit(sourcemodel, sens, headmodel, dat, ...)  
        where  
          sourcemodel is the input source model with a single or a few dipoles  
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS  
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL  
          dat         is the data matrix with the ERP or ERF  
        and  
          estimate    contains the estimated source parameters  
         
        Additional input arguments should be specified as key-value pairs and can include  
          'display'     = Level of display [ off | iter | notify | final ]  
          'optimfun'    = Function to use [fminsearch | fminunc ]  
          'maxiter'     = Maximum number of function evaluations allowed [ positive integer ]  
          'constr'      = Structure with constraints  
          'metric'      = Error measure to be minimised [ rv | var | abs ]  
          'checkinside' = Boolean flag to check whether dipole is inside source compartment [ 0 | 1 ]  
          'mleweight'   = weight matrix for maximum likelihood estimation, e.g. inverse noise covariance  
         
        These options influence the forward computation of the leadfield  
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        The constraints on the source model are specified in a structure  
          constr.symmetry   = boolean, dipole positions are symmetrically coupled to each other  
          constr.fixedori   = boolean, keep dipole orientation fixed over whole data window  
          constr.rigidbody  = boolean, keep relative position of multiple dipoles fixed  
          constr.mirror     = vector, used for symmetric dipole models  
          constr.reduce     = vector, used for symmetric dipole models  
          constr.expand     = vector, used for symmetric dipole models  
          constr.sequential = boolean, fit different dipoles to sequential slices of the data  
         
        The maximum likelihood estimation implements  
        - Lutkenhoner B. "Dipole source localization by means of maximum likelihood  
          estimation I. Theory and simulations" Electroencephalogr Clin Neurophysiol. 1998  
          Apr;106(4):314-21.  
         
        See also FT_DIPOLEFITTING, FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/ft_inverse_dipolefit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_dipolefit", *args, **kwargs)
