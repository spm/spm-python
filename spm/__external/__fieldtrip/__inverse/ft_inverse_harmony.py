from spm.__wrapper__ import Runtime


def ft_inverse_harmony(*args, **kwargs):
    """
      FT_INVERSE_HARMONY computes a linear estimate of the current in a distributed  
        source model using a mesh harmonic based low-pass filter.  
         
        Use as  
          [estimate] = ft_inverse_harmony(sourcemodel, sens, headmodel, dat, ...)  
        where  
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL  
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS  
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL  
          dat         is the data matrix with the ERP or ERF  
        and  
          estimate    contains the estimated source parameters  
         
        Additional input arguments should be specified as key-value pairs and can include  
          'noisecov'             = Nchan x Nchan matrix with noise covariance  
          'noiselambda'          = scalar value, regularisation parameter for the noise covariance matrix (default=0)  
          'filter_order'         = scalar, order of the mesh Butterwirth filter  
          'filter_bs'            = scalar, stop-band of the mesh Butterworth filter  
          'number_harmonics'     = Integer, number of mesh harmonics used (can be empty, the default will then be identity)  
          'lambda'               = scalar, regularisation parameter (can be empty, it will then be estimated from snr)  
          'snr'                  = scalar, signal to noise ratio  
          'scalesourcecov'       = 'no' or 'yes', scale the source covariance matrix R such that trace(leadfield*R*leadfield')/trace(C)=1  
          'connected_components' = number of connected components of the source mesh (1 or 2)  
          'prewhiten'            = 'no' or 'yes', prewhiten the leadfield matrix with the noise covariance matrix C  
         
        These options influence the forward computation of the leadfield  
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        This implements  
        - Petrov Y (2012) Harmony: EEG/MEG Linear Inverse Source Reconstruction in the  
          Anatomical Basis of Spherical Harmonics. PLoS ONE 7(10): e44439.  
          doi:10.1371/journal.pone.0044439  
         
        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/ft_inverse_harmony.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_harmony", *args, **kwargs)
