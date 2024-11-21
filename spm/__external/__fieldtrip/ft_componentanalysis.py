from spm.__wrapper__ import Runtime


def ft_componentanalysis(*args, **kwargs):
    """
      FT_COMPONENTANALYSIS performs independent component analysis or other  
        spatio-temporal decompositions of EEG or MEG data. This function computes  
        the topography and timecourses of the components. The output of this  
        function can be further analyzed with FT_TIMELOCKANALYSIS or  
        FT_FREQANALYSIS.  
         
        Use as  
          [comp] = ft_componentanalysis(cfg, data)  
        where cfg is a configuration structure and the input data is obtained from  
        FT_PREPROCESSING or from FT_TIMELOCKANALYSIS.  
         
        The configuration should contain  
          cfg.method       = 'runica', 'fastica', 'binica', 'pca', 'svd', 'jader',  
                             'varimax', 'dss', 'cca', 'sobi', 'white' or 'csp'  
                             (default = 'runica')  
          cfg.channel      = cell-array with channel selection (default = 'all'),  
                             see FT_CHANNELSELECTION for details  
          cfg.split        = cell-array of channel types between which covariance  
                             is split, it can also be 'all' or 'no' (default = 'no')  
          cfg.trials       = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.numcomponent = 'all' or number (default = 'all')  
          cfg.demean       = 'no' or 'yes', whether to demean the input data (default = 'yes')  
          cfg.updatesens   = 'no' or 'yes' (default = 'yes')  
          cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'text')  
         
        The runica method supports the following method-specific options. The  
        values that these options can take can be found with HELP RUNICA.  
          cfg.runica.extended  
          cfg.runica.pca  
          cfg.runica.sphering  
          cfg.runica.weights  
          cfg.runica.lrate  
          cfg.runica.block  
          cfg.runica.anneal  
          cfg.runica.annealdeg  
          cfg.runica.stop  
          cfg.runica.maxsteps  
          cfg.runica.bias  
          cfg.runica.momentum  
          cfg.runica.specgram  
          cfg.runica.posact  
          cfg.runica.verbose  
          cfg.runica.logfile  
          cfg.runica.interput  
         
        The fastica method supports the following method-specific options. The  
        values that these options can take can be found with HELP FASTICA.  
          cfg.fastica.approach  
          cfg.fastica.numOfIC  
          cfg.fastica.g  
          cfg.fastica.finetune  
          cfg.fastica.a1  
          cfg.fastica.a2  
          cfg.fastica.mu  
          cfg.fastica.stabilization  
          cfg.fastica.epsilon  
          cfg.fastica.maxNumIterations  
          cfg.fastica.maxFinetune  
          cfg.fastica.sampleSize  
          cfg.fastica.initGuess  
          cfg.fastica.verbose  
          cfg.fastica.displayMode  
          cfg.fastica.displayInterval  
          cfg.fastica.firstEig  
          cfg.fastica.lastEig  
          cfg.fastica.interactivePCA  
          cfg.fastica.pcaE  
          cfg.fastica.pcaD  
          cfg.fastica.whiteSig  
          cfg.fastica.whiteMat  
          cfg.fastica.dewhiteMat  
          cfg.fastica.only  
         
        The binica method supports the following method-specific options. The  
        values that these options can take can be found with HELP BINICA.  
          cfg.binica.extended  
          cfg.binica.pca  
          cfg.binica.sphering  
          cfg.binica.lrate  
          cfg.binica.blocksize  
          cfg.binica.maxsteps  
          cfg.binica.stop  
          cfg.binica.weightsin  
          cfg.binica.verbose  
          cfg.binica.filenum  
          cfg.binica.posact  
          cfg.binica.annealstep  
          cfg.binica.annealdeg  
          cfg.binica.bias  
          cfg.binica.momentum  
         
        The dss method requires the following method-specific option and supports  
        a whole lot of other options. The values that these options can take can  
        be found with HELP DSS_CREATE_STATE.  
          cfg.dss.denf.function  
          cfg.dss.denf.params  
         
        The sobi method supports the following method-specific options. The  
        values that these options can take can be found with HELP SOBI.  
          cfg.sobi.n_sources  
          cfg.sobi.p_correlations  
         
        The csp method implements the common-spatial patterns method. For CSP, the  
        following specific options can be defined:  
          cfg.csp.classlabels = vector that assigns a trial to class 1 or 2.  
          cfg.csp.numfilters  = the number of spatial filters to use (default: 6).  
         
        The icasso method implements icasso. It runs fastica a specified number of  
        times, and provides information about the stability of the components found  
        The following specific options can be defined, see ICASSOEST:  
          cfg.icasso.mode  
          cfg.icasso.Niter  
         
        Instead of specifying a component analysis method, you can also specify  
        a previously computed unmixing matrix, which will be used to estimate the  
        component timecourses in this data. This requires  
          cfg.unmixing     = NxN unmixing matrix  
          cfg.topolabel    = Nx1 cell-array with the channel labels  
         
        You may specify a particular seed for random numbers called by  
        rand/randn/randi, or the random state used by a previous call to this  
        function to replicate results. For example:  
          cfg.randomseed   = integer seed value of user's choice  
          cfg.randomseed   = comp.cfg.callinfo.randomseed (from previous call)  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_TOPOPLOTIC, FT_REJECTCOMPONENT, FASTICA, RUNICA, BINICA, SVD,  
        JADER, VARIMAX, DSS, CCA, SOBI, ICASSO  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_componentanalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_componentanalysis", *args, **kwargs)
