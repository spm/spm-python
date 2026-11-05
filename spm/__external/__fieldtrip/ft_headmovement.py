from spm._runtime import Runtime


def ft_headmovement(*args, **kwargs):
    r"""
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
        or  
          data = ft_headmovement(cfg, data)  
         
        where the configuration should contain  
          cfg.method       = string, 'updatesens' (default), 'cluster', 'avgoverrpt',  
                             'pertrial_cluster', 'pertrial' (default = 'updatesens')  
          
        and, in case no additional data structure is provided  
          cfg.dataset      = string with the filename  
         
        optional arguments are  
          cfg.trl          = empty (default), or Nx3 matrix with the trial  
                             definition (see FT_DEFINETRIAL). When specified as empty,  
                             the whole recording is used. This option does not  
                             have an effect if there's an additional data input  
          cfg.numclusters  = number of segments with constant headposition in  
                             which to split the data (default = 10). This argument  
                             is only used for the methods that use clustering ('updatesens',  
                              'cluster', 'pertrial_cluster').  
         
        If cfg.method = 'none', the grad in the single output structure is the grad  
        as stored in the header of the recording, in dewar coordinates.  
         
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
         
        If cfg.method = 'pertrial', the first output argument contains the time  
        series of the HLC-coils, along with a grad in dewar coordinates. The  
        second output argument contains a 1xNtrial cell-array of grad structures,  
        expressed in head coordinates.  
         
        If cfg.method = 'pertrial_clusters', the cell-array of output structures  
        contains sets of trials where the trial-specific head position was  
        considered to be positioned close to the corresponding kmeans-cluster's  
        centroid. The corresponding grad-structure is specified accordin to the  
        cluster's centroid. This method requires cfg.numclusters to be specified.  
         
        The updatesens method and related methods are described by Stolk et al., Online and  
        offline tools for head movement compensation in MEG. NeuroImage, 2012.  
         
        See also FT_REGRESSCONFOUND, FT_REALTIME_HEADLOCALIZER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_headmovement.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_headmovement", *args, **kwargs)
