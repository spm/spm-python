from spm.__wrapper__ import Runtime


def ft_headmovement(*args, **kwargs):
    """
      FT_HEADMOVEMENT outputs a raw data structure, or cell-array of data structures  
        reflecting the variability in the subject's head poisition relative to the   
        MEG sensors, based on continuous head position information. Current support is  
        only for CTF-data. The output timeseries contain the raw HLC data, and a  
        parametrization of the head movement in terms of translation and  
        rotations in 3D space. The grad structure(s) have head position information  
        incorporated in the coils' position/orientation and/or in the tra  
        matrix, depending on the method used.  
         
        Use as  
          data = ft_headmovement(cfg)  
         
        where the configuration should contain  
          cfg.dataset      = string with the filename  
          cfg.method       = string, 'updatesens' (default), 'cluster', 'avgoverrpt',  
                             'pertrial_cluster', 'pertrial' (default = 'updatesens')  
         
        optional arguments are  
          cfg.trl          = empty (default), or Nx3 matrix with the trial  
                             definition (see FT_DEFINETRIAL). When specified as empty,  
                             the whole recording is used.  
          cfg.numclusters  = number of segments with constant headposition in  
                             which to split the data (default = 10). This argument  
                             is only used for the methods that use clustering ('updatesens',  
                              'cluster', 'pertrial_cluster').  
         
        If cfg.method = 'updatesens', the grad in the single output structure has  
        a specification of the coils expanded as per the centroids of the position  
        clusters (obtained by kmeans clustering of the HLC time series). The balancing matrix   
        is a weighted concatenation of the original tra-matrix. This method requires   
        cfg.numclusters to be specified  
         
        If cfg.method = 'avgoverrpt', the grad in the single output structure has  
        a specification of the coils according to the average head position  
        across the specified samples.  
         
        If cfg.method = 'cluster', the cell-array of output structures represent  
        the epochs in which the head was considered to be positioned close to the  
        corresponding kmeans-cluster's centroid. The corresponding grad-structure  
        is specified according to this cluster's centroid. This method requires  
        cfg.numclusters to be specified.  
         
        If cfg.method = 'pertrial', the cell-array of output structures contains  
        single trials, each trial with a trial-specific grad structure. Note that  
        this is extremely memory inefficient with large numbers of trials, and  
        probably an overkill.  
         
        If cfg.method = 'pertrial_clusters', the cell-array of output structures  
        contains sets of trials where the trial-specific head position was  
        considered to be positioned close to the corresponding kmeans-cluster's  
        centroid. The corresponding grad-structure is specified accordin to the  
        cluster's centroid. This method requires cfg.numclusters to be specified.  
         
        The updatesens method and related methods are described by Stolk et al., Online and  
        offline tools for head movement compensation in MEG. NeuroImage, 2012.  
         
        See also FT_REGRESSCONFOUND, FT_REALTIME_HEADLOCALIZER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_headmovement.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmovement", *args, **kwargs)
