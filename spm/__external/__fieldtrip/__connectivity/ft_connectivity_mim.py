from spm.__wrapper__ import Runtime


def ft_connectivity_mim(*args, **kwargs):
    """
      FT_CONNECTIVITY_MIM computes the multivariate interaction measure from a  
        data-matrix containing the cross-spectral density. This implements the method  
        described in Ewald et al., Estimating true brain connectivity from EEG/MEG data  
        invariant to linear and static trasformations in sensor space. Neuroimage, 2012;  
        476:488.  
         
        Use as  
          [m] = hcp_connectivity_mim(inputdata, ...)  
         
        The input data should be an array organized as  
          Channel x Channel x Frequency  
         
        The output m contains the newChannel x newChannel x Frequency connectivity measure,  
        with newChannel equal to max(indices).  
         
        Additional optional input arguments come as key-value pairs:  
          'indices' = 1xN vector with indices of the groups to which the channels belong,  
                      e.g. [1 1 2 2] for a 2-by-2 connectivity between 2 planar MEG channels.  
         
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_mim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_mim", *args, **kwargs)
