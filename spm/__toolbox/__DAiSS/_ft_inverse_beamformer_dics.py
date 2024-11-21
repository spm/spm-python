from spm.__wrapper__ import Runtime


def _ft_inverse_beamformer_dics(*args, **kwargs):
    """
      FT_INVERSE_BEAMFORMER_DICS estimates the source power or source  
        coherence according to the Dynamic Imaging of Coherent Sources  
        method.  
         
        Use as  
          estimate = ft_inverse_beamformer_dics(leadfield, Cf, ...)  
        where  
          leadfield  = leadfield/filter of the source of interest or a cell-array with leadfields/filters for multiple sources  
          Cf         = cross-spectral density matrix of the data  
        and  
          estimate   = structure with the estimated source parameters  
         
        Additional options should be specified in key-value pairs and can be  
         'Pr'               = power of the external reference channel  
         'Cr'               = cross spectral density between all data channels and the external reference channel  
         'invCf'            = pre-computed inverse covariance matrix  
         'refdip'           = location of dipole with which coherence is computed  
         'lambda'           = regularisation parameter  
         'powmethod'        = can be 'trace' or 'lambda1'  
         'feedback'         = give ft_progress indication, can be 'text', 'gui' or 'none'  
         'filterinput'      = 'leafield' input is pre-computed filter        can be 'yes' or 'no'  
         'fixedori'         = use fixed or free orientation,                 can be 'yes' or 'no'  
         'projectnoise'     = project noise estimate through filter,         can be 'yes' or 'no'  
         'realfilter'       = construct a real-valued filter,                can be 'yes' or 'no'  
         'keepfilter'       = remember the beamformer filter,                can be 'yes' or 'no'  
         'keepleadfield'    = remember the forward computation,              can be 'yes' or 'no'  
         'keepcsd'          = remember the estimated cross-spectral density, can be 'yes' or 'no'  
         'filteronly'       = only compute and return the filter,            can be 'yes' or 'no'  
         
        This implements Joachim Gross et al. 2001  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/ft_inverse_beamformer_dics.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inverse_beamformer_dics", *args, **kwargs)
