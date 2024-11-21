from spm.__wrapper__ import Runtime


def ft_connectivity_powcorr_ortho(*args, **kwargs):
    """
      FT_CONNECTIVITY_POWCORR_ORTHO computes power correlation after removing  
        the zero-lag contribution on a trial-by-trial basis, according to Hipp's  
        Nature Neuroscience paper.  
         
        Use as  
          [c] = ft_connectivity_powcorr(inputdata, ...)  
         
        Where the input is a Nchan*Nrpt matrix containing the complex-valued amplitude  
        and phase information at a given frequency.  
         
        The output c is a Nchan*Nref matrix that contain the power correlation for all  
        channels orthogonalised relative to the reference channel in the first Nref  
        columns, and the power correlation for the reference channels orthogonalised  
        relative to the channels in the second Nref columns.  
         
        Additional optional input arguments come as key-value pairs:  
          'refindx'  = index/indices of the channels that serve as a reference channel (default is all)  
          'tapvec'   = vector with the number of tapers per trial  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_powcorr_ortho.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_powcorr_ortho", *args, **kwargs)
