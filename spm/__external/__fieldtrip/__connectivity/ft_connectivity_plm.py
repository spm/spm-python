from spm.__wrapper__ import Runtime


def ft_connectivity_plm(*args, **kwargs):
    """
      FT_CONNECTIVITY_PLM computes the phase linearity measurement from a cell array of  
        time-domain data, where each cell is an epoch. This implements the metric described  
        in Baselice et al. "Phase Linearity Measurement: a novel index for brain functional  
        connectivity", IEEE Transactions on Medical Imaging, 2018.  
         
        Use as  
          [p] = ft_connectivity_plm(inputdata, ...)  
         
        The input data input should be organized as a cell-array, one element for each  
        epoch/repetition. Each cell should be a matrix of of nchan x nsamples values.  
         
        Additional optional input arguments come as key-value pairs:  
          'bandwidth'	=	scalar, half-bandwidth parameter: the frequency range across which to integrate  
          'fsample'   = sampling frequency, needed to convert bandwidth to number of bins  
         
        The output p contains the phase linearity measurement in the [0, 1] interval. It is  
        organized as a 3D matrix of Nrpt x Nchan x Nchan dimensions.  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_plm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_plm", *args, **kwargs)
