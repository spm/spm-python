from spm.__wrapper__ import Runtime


def ft_dipolesimulation(*args, **kwargs):
    """
      FT_DIPOLESIMULATION simulates channel-level time-series data that consists of the  
        the spatial distribution of the the field or potential of one or multiple dipoles.  
         
        Use as  
          data = ft_dipolesimulation(cfg)  
        which will return a raw data structure that resembles the output of  
        FT_PREPROCESSING.  
         
        The dipoles position and orientation have to be specified with  
          cfg.sourcemodel.pos        = [Rx Ry Rz] (size Nx3)  
          cfg.sourcemodel.mom        = [Qx Qy Qz] (size 3xN)  
          cfg.sourcemodel.unit       = string, can be 'mm', 'cm', 'm' (default is automatic)  
         
        The timecourse of the dipole activity is given as a cell-array with one  
        dipole signal per trial  
          cfg.sourcemodel.signal     = cell-array with one dipole signal per trial  
        or by specifying the parameters of a sine-wave signal  
          cfg.sourcemodel.frequency  =   in Hz  
          cfg.sourcemodel.phase      =   in radians  
          cfg.sourcemodel.amplitude  =   per dipole  
         
        The number of trials and the time axes of the trials can be specified by  
          cfg.fsample     = simulated sample frequency (default = 1000)  
          cfg.trllen      = length of simulated trials in seconds (default = 1)  
          cfg.numtrl      = number of simulated trials (default = 10)  
          cfg.baseline    = number (default = 0.3)  
        or by  
          cfg.time        = cell-array with one time axis per trial, for example obtained from an existing dataset  
         
        Random white noise can be added to the data in each trial, either by  
        specifying an absolute or a relative noise level  
          cfg.relnoise    = add noise with level relative to data signal  
          cfg.absnoise    = add noise with absolute level  
          cfg.randomseed  = 'yes' or a number or vector with the seed value (default = 'yes')  
         
        Optional input arguments are  
          cfg.channel    = Nx1 cell-array with selection of channels (default = 'all'),  
                           see FT_CHANNELSELECTION for details  
          cfg.dipoleunit = units for dipole amplitude (default nA*m)  
          cfg.chanunit   = Nx1 cell-array with units for the channel data  
         
        Optionally, you can modify the leadfields by reducing the rank, i.e. remove the weakest orientation  
          cfg.reducerank    = 'no', or number (default = 3 for EEG, 2 for MEG)  
          cfg.backproject   = 'yes' or 'no',  determines when reducerank is applied whether the  
                              lower rank leadfield is projected back onto the original linear  
                              subspace, or not (default = 'yes')  
         
        The volume conduction model of the head should be specified as  
          cfg.headmodel     = structure with volume conduction model, see FT_PREPARE_HEADMODEL  
         
        The EEG or MEG sensor positions should be specified as  
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS  
         
        See also FT_SOURCEANALYSIS, FT_DIPOLEFITTING, FT_TIMELOCKSIMULATION,  
        FT_FREQSIMULATION, FT_CONNECTIVITYSIMULATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_dipolesimulation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_dipolesimulation", *args, **kwargs)
