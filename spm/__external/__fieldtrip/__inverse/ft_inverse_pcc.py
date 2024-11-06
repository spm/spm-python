from spm.__wrapper__ import Runtime


def ft_inverse_pcc(*args, **kwargs):
    """
      FT_INVERSE_PCC implements a linearly-constrained miminum variance beamformer that  
        allows for post-hoc computation of canonical or partial coherence or correlation.  
        Moreover, if cortico-cortical interactions are computed, the spatial filters are  
        computed with a paired dipole as sourcemodel, thus suppressing the distortive  
        effect of correlated activity from the seed region.  
         
        Use as  
          [estimate] = ft_inverse_pcc(sourcemodel, sens, headmodel, dat, cov, ...)  
        where  
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL  
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS  
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL  
          dat         is the data matrix with the ERP or ERF  
          cov         is the data covariance or cross-spectral density matrix  
        and  
          estimate    contains the estimated source parameters  
         
        Additional input arguments should be specified as key-value pairs and can include  
          'refchan'  
          'refdip'  
          'supchan'  
          'supdip'  
          'feedback'  
          'keepcsd'  
          'keepfilter'  
          'keepleadfield'  
          'keepmom'  
          'lambda'  
          'projectnoise'  
          'realfilter'  
          'fixedori'  
         
        These options influence the forward computation of the leadfield  
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)  
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')  
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')  
          'normalizeparam'  = parameter for depth normalization (default = 0.5)  
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)  
         
        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/ft_inverse_pcc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_pcc", *args, **kwargs)
