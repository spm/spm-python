from spm.__wrapper__ import Runtime


def ft_inverse_sam(*args, **kwargs):
    """
      FT_INVERSE_SAM scans on pre-defined dipole locations with a single dipole and  
        returns the Synthetic Aperture Magnetometry (SAM) beamformer estimates.  
         
        Use as  
          [estimate] = ft_inverse_sam(sourcemodel, sens, headmodel, dat, cov, ...)  
        where  
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL  
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS  
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL  
          dat         is the data matrix with the ERP or ERF  
          cov         is the data covariance or cross-spectral density matrix  
        and  
          estimate    contains the estimated source parameters  
         
        Additional input arguments should be specified as key-value pairs and can include  
          'feedback'  
          'fixedori'          deprecated, control behaviour via 'reducerank' instead  
          'noisecov'  
          'toi'  
         
        If no orientation is specified, the SAM beamformer will try to estimate the orientation from the data.  
        The beamformer will either try to estimate the whole orientation, or only its tangential component.  
        This is controlled by the 'reducerank' parameter. For reducerank=3, the whole orientation is estimated,  
        and for reducerank=2 only the tangential component is estimated, based on an svd of the dipole's leadfield,  
        treating the 3d component as the 'radial' orientation.  
         
        These options influence the forward computation of the leadfield, if it has not yet been precomputed  
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/ft_inverse_sam.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_sam", *args, **kwargs)
