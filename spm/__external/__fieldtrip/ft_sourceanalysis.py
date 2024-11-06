from spm.__wrapper__ import Runtime


def ft_sourceanalysis(*args, **kwargs):
    """
      FT_SOURCEANALYSIS performs beamformer dipole analysis on EEG or MEG data  
        after preprocessing and a timelocked or frequency analysis  
         
        Use as  
          [source] = ft_sourceanalysis(cfg, freq)  
        or  
          [source] = ft_sourceanalysis(cfg, timelock)  
         
        where the second input argument with the data should be organised in a structure  
        as obtained from the FT_FREQANALYSIS or FT_TIMELOCKANALYSIS function. The  
        configuration "cfg" is a structure containing the specification of the head model,  
        the source model, and other options.  
         
        The different source reconstruction algorithms that are implemented are  
          cfg.method     = 'lcmv'    linear constrained minimum variance beamformer  
                           'sam'     synthetic aperture magnetometry  
                           'dics'    dynamic imaging of coherent sources  
                           'pcc'     partial canonical correlation/coherence  
                           'mne'     minimum norm estimation  
                           'rv'      scan residual variance with single dipole  
                           'music'   multiple signal classification  
                           'sloreta' standardized low-resolution electromagnetic tomography  
                           'eloreta' exact low-resolution electromagnetic tomography  
        The DICS and PCC methods are for frequency or time-frequency domain data, all other  
        methods are for time domain data. ELORETA can be used both for time, frequency and  
        time-frequency domain data.  
         
        The complete grid with dipole positions and optionally precomputed leadfields is  
        constructed using FT_PREPARE_SOURCEMODEL. It can be specified as as a regular 3-D  
        grid that is aligned with the axes of the head coordinate system using  
          cfg.xgrid               = vector (e.g. -20:1:20) or 'auto' (default = 'auto')  
          cfg.ygrid               = vector (e.g. -20:1:20) or 'auto' (default = 'auto')  
          cfg.zgrid               = vector (e.g.   0:1:20) or 'auto' (default = 'auto')  
          cfg.resolution          = number (e.g. 1 cm) for automatic grid generation  
        If the source model destribes a triangulated cortical sheet, it is described as  
          cfg.sourcemodel.pos     = N*3 matrix with the vertex positions of the cortical sheet  
          cfg.sourcemodel.tri     = M*3 matrix that describes the triangles connecting the vertices  
        Alternatively the position of a few dipoles at locations of interest can be  
        user-specified, for example obtained from an anatomical or functional MRI  
          cfg.sourcemodel.pos     = N*3 matrix with position of each source  
          cfg.sourcemodel.inside  = N*1 vector with boolean value whether grid point is inside brain (optional)  
          cfg.sourcemodel.dim     = [Nx Ny Nz] vector with dimensions in case of 3-D grid (optional)  
         
        Besides the source positions, you may also include previously computed  
        spatial filters and/or leadfields using  
          cfg.sourcemodel.filter  
          cfg.sourcemodel.leadfield  
         
        The following strategies are supported to obtain statistics for the source parameters using  
        multiple trials in the data, either directly or through a resampling-based approach  
          cfg.rawtrial      = 'no' or 'yes'   construct filter from single trials, apply to single trials. Note that you also may want to set cfg.keeptrials='yes' to keep all trial information, especially if using in combination with sourcemodel.filter  
          cfg.jackknife     = 'no' or 'yes'   jackknife resampling of trials  
          cfg.pseudovalue   = 'no' or 'yes'   pseudovalue resampling of trials  
          cfg.bootstrap     = 'no' or 'yes'   bootstrap resampling of trials  
          cfg.numbootstrap  = number of bootstrap replications (e.g. number of original trials)  
        If none of these options is specified, the average over the trials will  
        be computed prior to computing the source reconstruction.  
         
        To obtain statistics over the source parameters between two conditions, you  
        can also use a resampling procedure that reshuffles the trials over both  
        conditions. In that case, you should call the function with two datasets  
        containing single trial data like  
          [source] = ft_sourceanalysis(cfg, freqA, freqB)  
          [source] = ft_sourceanalysis(cfg, timelockA, timelockB)  
        and you should specify  
          cfg.randomization      = 'no' or 'yes'  
          cfg.permutation        = 'no' or 'yes'  
          cfg.numrandomization   = number, e.g. 500  
          cfg.numpermutation     = number, e.g. 500 or 'all'  
         
        If you have not specified a sourcemodel with pre-computed leadfields, the leadfield  
        for each source position will be computed on the fly, in the lower level function that  
        is called for the heavy lifting. In that case you can modify parameters for the forward  
        computation, e.g. by reducing the rank (i.e. remove the weakest orientation), or by  
        normalizing each column.  
          cfg.reducerank      = 'no', or number (default = 3 for EEG, 2 for MEG)  
          cfg.backproject     = 'yes' or 'no',  determines when reducerank is applied whether the  
                                lower rank leadfield is projected back onto the original linear  
                                subspace, or not (default = 'yes')  
          cfg.normalize       = 'yes' or 'no' (default = 'no')  
          cfg.normalizeparam  = depth normalization parameter (default = 0.5)  
          cfg.weight          = number or Nx1 vector, weight for each dipole position to compensate  
                                for the size of the corresponding patch (default = 1)  
         
        Other configuration options are  
          cfg.channel       = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.frequency     = single number (in Hz)  
          cfg.latency       = single number in seconds, for time-frequency analysis  
          cfg.refchan       = reference channel label (for coherence)  
          cfg.refdip        = reference dipole location (for coherence)  
          cfg.supchan       = suppressed channel label(s)  
          cfg.supdip        = suppressed dipole location(s)  
          cfg.keeptrials    = 'no' or 'yes'  
          cfg.keepleadfield = 'no' or 'yes'  
         
        Some options need to be specified as method specific options, and determine the low-level computation of the inverse operator.  
        The functionality (and applicability) of the (sub-)options are documented in the lower-level ft_inverse_<method> functions.   
        Replace <method> with one of the supported methods.    
          cfg.<method>.lambda        = number or empty for automatic default  
          cfg.<method>.kappa         = number or empty for automatic default  
          cfg.<method>.tol           = number or empty for automatic default  
          cfg.<method>.projectnoise  = 'no' or 'yes'  
          cfg.<method>.keepfilter    = 'no' or 'yes'  
          cfg.<method>.keepcsd       = 'no' or 'yes'  
          cfg.<method>.keepmom       = 'no' or 'yes'  
          cfg.<method>.feedback      = 'no', 'text', 'textbar', 'gui' (default = 'text')  
         
        The volume conduction model of the head should be specified as  
          cfg.headmodel     = structure with volume conduction model, see FT_PREPARE_HEADMODEL  
         
        The EEG or MEG sensor positions can be present in the data or can be specified as  
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_SOURCEDESCRIPTIVES, FT_SOURCESTATISTICS, FT_PREPARE_LEADFIELD,  
        FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourceanalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sourceanalysis", *args, **kwargs)
