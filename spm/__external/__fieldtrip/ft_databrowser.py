from spm.__wrapper__ import Runtime


def ft_databrowser(*args, **kwargs):
    """
      FT_DATABROWSER can be used for visual inspection of data. Artifacts that were  
        detected by artifact functions (see FT_ARTIFACT_xxx functions where xxx is the type  
        of artifact) are marked. Additionally data pieces can be marked and unmarked as  
        artifact by manual selection. The output cfg contains the updated specification of  
        the artifacts.  
         
        Use as  
          [cfg] = ft_databrowser(cfg)  
          [cfg] = ft_databrowser(cfg, data)  
        If you only specify the configuration structure, it should contain the name of the  
        dataset on your hard disk (see below). If you specify input data, it should be a  
        data structure as obtained from FT_PREPROCESSING or from FT_COMPONENTANALYSIS.  
         
        If you want to browse data that is on disk, you have to specify  
          cfg.dataset                 = string with the filename  
        Instead of specifying the dataset, you can also explicitely specify the name of the  
        file containing the header information and the name of the file containing the  
        data, using  
          cfg.datafile                = string with the filename  
          cfg.headerfile              = string with the filename  
         
        The following configuration options are supported:  
          cfg.ylim                    = vertical scaling, can be 'maxmin', 'maxabs' or [ymin ymax] (default = 'maxabs')  
          cfg.zlim                    = color scaling to apply to component topographies, 'minmax', 'maxabs' (default = 'maxmin')  
          cfg.blocksize               = duration in seconds for cutting continuous data in segments  
          cfg.trl                     = structure that defines the data segments of interest, only applicable for trial-based data  
          cfg.continuous              = 'yes' or 'no', whether the data should be interpreted as continuous or trial-based  
          cfg.allowoverlap            = 'yes' or 'no', whether data that is overlapping in multiple trials is allowed (default = 'no')  
          cfg.channel                 = cell-array with channel labels, see FT_CHANNELSELECTION  
          cfg.channelclamped          = cell-array with channel labels, that when using the 'vertical' viewmode will always be shown at the bottom. This is useful for showing ECG/EOG channels along with the other channels  
          cfg.compscale               = string, 'global' or 'local', defines whether the colormap for the topographic scaling is applied per topography or on all visualized components (default = 'local')  
          cfg.viewmode                = string, 'vertical', 'butterfly', or 'component' for visualizing ICA/PCA topographies together with the timecourses (default = 'vertical')  
          cfg.plotlabels              = 'yes', 'no' or 'some', whether to plot channel labels in vertical viewmode. The option 'some' plots one label for every ten channels, which is useful if there are many channels (default = 'some')  
          cfg.plotevents              = 'no' or 'yes', whether to plot event markers (default = 'yes')  
          cfg.ploteventlabels         = 'type=value', 'colorvalue' (default = 'type=value')  
          cfg.eventcolor              = string with line colors or Nx3 color map, colors used for plotting the different types of events (default is automatic)  
          cfg.artifactcolor           = string with line colors or Nx3 color map, colors used for plotting the different types of artifacts (default is automatic)  
          cfg.artfctdef.xxx.artifact  = Nx2 matrix with artifact segments see FT_ARTIFACT_xxx functions  
          cfg.selectfeature           = string, name of feature to be selected/added (default = 'visual')  
          cfg.selectmode              = 'markartifact', 'markpeakevent', 'marktroughevent' (default = 'markartifact')  
          cfg.colorgroups             = 'sequential', 'allblack', 'labelcharN' (N = Nth character in label), 'chantype' or a vector with the length of the number of channels defining the groups (default = 'sequential')  
          cfg.linecolor               = string with line colors or Nx3 color map (default = customized lines map with 15 colors)  
          cfg.linewidth               = linewidth in points (default = 0.5)  
          cfg.linestyle               = linestyle/marker type, see options of the PLOT function (default = '-')  
          cfg.verticalpadding         = number or 'auto', padding to be added to top and bottom of plot to avoid channels largely dissappearing when viewmode = 'vertical'/'component'  (default = 'auto'). The padding is expressed as a proportion of the total height added to the top and bottom. The setting 'auto' determines the padding depending on the number of channels that are being plotted.  
          cfg.selfun                  = string, name of function that is evaluated using the right-click context menu. The selected data and cfg.selcfg are passed on to this function.  
          cfg.selcfg                  = configuration options for function in cfg.selfun  
          cfg.seldat                  = 'selected' or 'all', specifies whether only the currently selected or all channels will be passed to the selfun (default = 'selected')  
          cfg.figure                  = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.visible                 = string, 'on' or 'off' whether figure will be visible (default = 'on')  
          cfg.position                = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer                = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO (default is automatic, try 'painters' when it crashes)  
          cfg.colormap                = string, or Nx3 matrix, see FT_COLORMAP  
         
        The following options for the scaling of the EEG, EOG, ECG, EMG, MEG and NIRS channels  
        is optional and can be used to bring the absolute numbers of the different  
        channel types in the same range (e.g. fT and uV). The channel types are determined  
        from the input data using FT_CHANNELSELECTION.  
          cfg.eegscale                = number, scaling to apply to the EEG channels prior to display  
          cfg.eogscale                = number, scaling to apply to the EOG channels prior to display  
          cfg.ecgscale                = number, scaling to apply to the ECG channels prior to display  
          cfg.emgscale                = number, scaling to apply to the EMG channels prior to display  
          cfg.megscale                = number, scaling to apply to the MEG channels prior to display  
          cfg.gradscale               = number, scaling to apply to the MEG gradiometer channels prior to display (in addition to the cfg.megscale factor)  
          cfg.magscale                = number, scaling to apply to the MEG magnetometer channels prior to display (in addition to the cfg.megscale factor)  
          cfg.nirsscale               = number, scaling to apply to the NIRS channels prior to display  
          cfg.mychanscale             = number, scaling to apply to the channels specified in cfg.mychan  
          cfg.mychan                  = Nx1 cell-array with selection of channels  
          cfg.chanscale               = Nx1 vector with scaling factors, one per channel specified in cfg.channel  
         
        You can specify preprocessing options that are to be applied to the  data prior to  
        display. Most options from FT_PREPROCESSING are supported. They should be specified  
        in the sub-structure cfg.preproc like these examples  
          cfg.preproc.lpfilter        = 'no' or 'yes'  lowpass filter (default = 'no')  
          cfg.preproc.lpfreq          = lowpass  frequency in Hz  
          cfg.preproc.demean          = 'no' or 'yes', whether to apply baseline correction (default = 'no')  
          cfg.preproc.detrend         = 'no' or 'yes', remove linear trend from the data (done per trial) (default = 'no')  
          cfg.preproc.baselinewindow  = [begin end] in seconds, the default is the complete trial (default = 'all')  
         
        In case of component viewmode, a layout is required. If no layout is specified, an  
        attempt is made to construct one from the sensor definition that is present in the  
        data or specified in the configuration.  
          cfg.layout                  = filename of the layout, see FT_PREPARE_LAYOUT  
          cfg.elec                    = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad                    = structure with gradiometer definition or filename, see FT_READ_SENS  
        Additional plotting options for the component viewmode:  
          cfg.gridscale               = scalar, number of points along both directions for interpolation (default = 45 here)  
          cfg.shading                 = string, 'none', 'flat', 'interp' (default = 'flat')  
          cfg.interplimits            = string, 'sensors' or 'mask' (default here = 'mask')  
          cfg.interpolation           = string, 'nearest', 'linear', 'natural', 'cubic' or 'v4' (default = 'v4')  
          cfg.contournum              = topoplot contour lines  
         
        The default font size might be too small or too large, depending on the number of  
        channels. You can use the following options to change the size of text inside the  
        figure and along the axes.  
          cfg.fontsize                = number, fontsize inside the figure (default = 0.03)  
          cfg.fontunits               = string, can be 'normalized', 'points', 'pixels', 'inches' or 'centimeters' (default = 'normalized')  
          cfg.axisfontsize            = number, fontsize along the axes (default = 10)  
          cfg.axisfontunits           = string, can be 'normalized', 'points', 'pixels', 'inches' or 'centimeters' (default = 'points')  
         
        When visually selection data, a right-click will bring up a context-menu containing  
        functions to be executed on the selected data. You can use your own function using  
        cfg.selfun and cfg.selcfg. You can use multiple functions by giving the names/cfgs  
        as a cell-array.  
         
        In butterfly and vertical mode, you can use the "identify" button to reveal the name of a  
        channel. Please be aware that it searches only vertically. This means that it will  
        return the channel with the amplitude closest to the point you have clicked at the  
        specific time point. This might be counterintuitive at first.  
         
        The "cfg.artfctdef" structure in the output cfg is comparable to the configuration  
        used by the artifact detection functions like FT_ARTIFACT_ZVALUE and in  
        FT_REJECTARTIFACT. It contains for each artifact type an Nx2 matrix in which the  
        first column corresponds to the begin samples of an artifact period, the second  
        column contains the end samples of the artifact periods.  
         
        In case the databrowser crashes and you cannot close the window, use delete(gcf) to  
        get rid of the figure.  
         
        See also FT_PREPROCESSING, FT_REJECTARTIFACT, FT_ARTIFACT_EOG, FT_ARTIFACT_MUSCLE,  
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MANUAL, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_CLIP,  
        FT_ARTIFACT_ECG, FT_COMPONENTANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_databrowser.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_databrowser", *args, **kwargs)
