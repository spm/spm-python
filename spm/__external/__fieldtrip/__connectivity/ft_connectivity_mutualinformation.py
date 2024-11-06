from spm.__wrapper__ import Runtime


def ft_connectivity_mutualinformation(*args, **kwargs):
    """
      FT_CONNECTIVITY_MUTUALINFORMATION computes mutual information using either the  
        information breakdown toolbox (ibtb), as described in Magri et al., BMC  
        Neuroscience 2009, 1471-2202, or Robin Ince's Gaussian copula based parametric  
        approach (gcmi).  
         
        Use as  
          mi = ft_connectivity_mutualinformation(inputdata, ...)  
         
        The input data should be a Nchan x Nobservations matrix.  
         
        The output mi contains the estimated mutual information between all channels and  
        the reference channels.  
         
        Additional input arguments come as key-value pairs:  
          method     = string, 'ibtb' or 'gcmi' (default = 'gcmi')  
         
        The default method has changed from 'ibtb' to 'gcmi' in December 2022. The former method  
        is based on an external toolbox that is not actively supported anymore. Moreover, the  
        Gaussian-Copula based Mutual Information does not depend on a binning strategy, and may  
        provide reasonable results also in the presence of low amounts of data. The change in   
        default reflects the default defined in ft_connectivityanalysis.  
         
        Additional input arguments for the 'ibtb' method:  
          'histmethod' = The way that histograms are generated from the data. Possible values  
                         are 'eqpop' (default), 'eqspace', 'ceqspace', 'gseqspace'.  
                         See the help of the 'binr' function in the ibtb toolbox for more information.  
          'numbin'     = scalar value. The number of bins used to create the histograms needed for  
                         the entropy computations  
          'opts'       = structure that is passed on to the 'information' function in the ibtb  
                         toolbox. See the help of that function for more information.  
          'refindx'    = scalar value or 'all'. The channel that is used as 'reference channel'.  
         
        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/ft_connectivity_mutualinformation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivity_mutualinformation", *args, **kwargs)
