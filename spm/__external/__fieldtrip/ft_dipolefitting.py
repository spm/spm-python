from spm.__wrapper__ import Runtime


def ft_dipolefitting(*args, **kwargs):
    """
      FT_DIPOLEFITTING perform grid search and non-linear fit with one or multiple  
        dipoles and try to find the location where the dipole model is best able  
        to explain the measured EEG or MEG topography.  
         
        This function will initially scan the whole brain with a single dipole on  
        a regular coarse grid, and subsequently start at the most optimal location  
        with a non-linear search. Alternatively you can specify the initial  
        location of the dipole(s) and the non-linear search will start from there.  
         
        Use as  
          [source] = ft_dipolefitting(cfg, data)  
         
        The configuration has the following general fields  
          cfg.numdipoles  = number, default is 1  
          cfg.symmetry    = 'x', 'y' or 'z' symmetry for two dipoles, can be empty (default = [])  
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),  
                            see FT_CHANNELSELECTION for details  
          cfg.gridsearch  = 'yes' or 'no', perform global grid search for initial  
                            guess for the dipole parameters (default = 'yes')  
          cfg.nonlinear   = 'yes' or 'no', perform nonlinear search for optimal  
                            dipole parameters (default = 'yes')  
         
        If a grid search is performed, a source model needs to be specified. This should either be   
        specified as cfg.sourcemodel (see below), or as a set of parameters to define a 3-D regular grid.  
        In the latter case, a complete grid is constructed using FT_PREPARE_SOURCEMODEL.  The specification   
        of a regular 3-D grid, aligned with the axes of the head coordinate system, can be obtained with   
          cfg.xgrid               = vector (e.g. -20:1:20) or 'auto' (default = 'auto')  
          cfg.ygrid               = vector (e.g. -20:1:20) or 'auto' (default = 'auto')  
          cfg.zgrid               = vector (e.g.   0:1:20) or 'auto' (default = 'auto')  
          cfg.resolution          = number (e.g. 1 cm)  
        If the source model destribes a triangulated cortical sheet, it is described as  
          cfg.sourcemodel.pos     = N*3 matrix with the vertex positions of the cortical sheet  
          cfg.sourcemodel.tri     = M*3 matrix that describes the triangles connecting the vertices  
        Alternatively the position of the dipoles at locations of interest can be  
        user-specified, for example obtained from an anatomical or functional MRI  
          cfg.sourcemodel.pos     = N*3 matrix with position of each source  
          cfg.sourcemodel.inside  = N*1 vector with boolean value whether grid point is inside brain (optional)  
          cfg.sourcemodel.dim     = [Nx Ny Nz] vector with dimensions in case of 3-D grid (optional)  
         
        If you do not start with a grid search, you have to give a starting location  
        for the nonlinear search  
          cfg.dip.pos     = initial dipole position, matrix of Ndipoles x 3  
         
        The conventional approach is to fit dipoles to event-related averages, which  
        within FieldTrip can be obtained from the FT_TIMELOCKANALYSIS or from  
        the FT_TIMELOCKGRANDAVERAGE function. This has the additional options  
          cfg.latency     = [begin end] in seconds or 'all' (default = 'all')  
          cfg.model       = 'moving' or 'regional'  
        A moving dipole model has a different position (and orientation) for each  
        timepoint, or for each component. A regional dipole model has the same  
        position for each timepoint or component, and a different orientation.  
         
        You can also fit dipoles to the spatial topographies of an independent  
        component analysis, obtained from the FT_COMPONENTANALYSIS function.  
        This has the additional options  
          cfg.component   = array with numbers (can be empty -> all)  
         
        You can also fit dipoles to the spatial topographies that are present  
        in the data in the frequency domain, which can be obtained using the  
        FT_FREQANALYSIS function. This has the additional options  
          cfg.frequency   = single number (in Hz)  
         
        Low level details of the fitting can be specified in the cfg.dipfit structure  
          cfg.dipfit.display      = level of display, can be 'off', 'iter', 'notify' or 'final' (default = 'iter')  
          cfg.dipfit.optimfun     = function to use, can be 'fminsearch' or 'fminunc' (default is determined automatic)  
          cfg.dipfit.maxiter      = maximum number of function evaluations allowed (default depends on the optimfun)  
          cfg.dipfit.checkinside  = boolean, check that the dipole remains in the source compartment (default = false)  
         
        Optionally, you can modify the leadfields by reducing the rank, i.e. remove the weakest orientation  
          cfg.reducerank    = 'no', or number (default = 3 for EEG, 2 for MEG)  
          cfg.backproject   = 'yes' or 'no',  determines when reducerank is applied whether the  
                              lower rank leadfield is projected back onto the original linear  
                              subspace, or not (default = 'yes')  
         
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
         
        See also FT_SOURCEANALYSIS, FT_PREPARE_LEADFIELD, FT_PREPARE_HEADMODEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_dipolefitting.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_dipolefitting", *args, **kwargs)
