from spm._runtime import Runtime


def ft_topoplotTFR(*args, **kwargs):
    """
      FT_TOPOPLOTTFR plots the topographic distribution over the head  
        of a 3-dimensional data representations such as time-frequency  
        representation of the power or coherence spectrum.  
         
        Use as  
          ft_topoplotTFR(cfg, freq)  
         
        The input freq structrure should contain a time-resolved power or  
        coherence spectrum from FT_FREQANALYSIS or FT_FREQDESCRIPTIVES.  
         
        The configuration can have the following parameters  
          cfg.parameter          = field that contains the data to be plotted as color, for example 'avg', 'powspctrm' or 'cohspctrm' (default is automatic)  
          cfg.maskparameter      = field in the data to be used for masking of data. It should have alues between 0 and 1, where 0 corresponds to transparent.  
          cfg.xlim               = limit for 1st dimension in data (e.g., time), can be 'maxmin' or [xmin xmax] (default = 'maxmin')  
          cfg.ylim               = limit for 2nd dimension in data (e.g., freq), can be 'maxmin' or [ymin ymax] (default = 'maxmin')  
          cfg.zlim               = limits for color dimension, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')  
          cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.refchannel         = name of reference channel for visualising connectivity, can be 'gui'  
          cfg.baseline           = 'yes','no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE or FT_FREQBASELINE  
          cfg.baselinetype       = 'absolute' or 'relative' (default = 'absolute')  
          cfg.trials             = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.colormap           = string, or Nx3 matrix, see FT_COLORMAP  
          cfg.marker             = 'on', 'labels', 'numbers', 'off'  
          cfg.markersymbol       = channel marker symbol (default = 'o')  
          cfg.markercolor        = channel marker color (default = [0 0 0] (black))  
          cfg.markersize         = channel marker size (default = 2)  
          cfg.markerfontsize     = font size of channel labels (default = 8 pt)  
          cfg.highlight          = 'off', 'on', 'labels', 'numbers'  
          cfg.highlightchannel   =  Nx1 cell-array with selection of channels, or vector containing channel indices see FT_CHANNELSELECTION  
          cfg.highlightsymbol    = highlight marker symbol (default = 'o')  
          cfg.highlightcolor     = highlight marker color (default = [0 0 0] (black))  
          cfg.highlightsize      = highlight marker size (default = 6)  
          cfg.highlightfontsize  = highlight marker size (default = 8)  
          cfg.hotkeys            = enables hotkeys (pageup/pagedown/m) for dynamic zoom and translation (ctrl+) of the color limits  
          cfg.colorbar           = 'yes'  
                                   'no' (default)  
                                   'North'              inside plot box near top  
                                   'South'              inside bottom  
                                   'East'               inside right  
                                   'West'               inside left  
                                   'NorthOutside'       outside plot box near top  
                                   'SouthOutside'       outside bottom  
                                   'EastOutside'        outside right  
                                   'WestOutside'        outside left  
          cfg.colorbartext       = string indicating the text next to colorbar  
          cfg.interplimits       = limits for interpolation (default = 'head')  
                                   'sensors'            to furthest sensor  
                                   'head'               to edge of head  
          cfg.interpolation      = 'linear','cubic','nearest','v4' (default = 'v4') see GRIDDATA  
          cfg.style              = plot style (default = 'both')  
                                   'straight'           colormap only  
                                   'contour'            contour lines only  
                                   'both'               both colormap and contour lines  
                                   'fill'               constant color between lines  
                                   'blank'              only the head shape  
                                   'straight_imsat'     colormap only, vector-graphics friendly  
                                   'both_imsat'         both colormap and contour lines, vector-graphics friendly  
          cfg.gridscale          = scaling grid size (default = 67)  
                                   determines resolution of figure  
          cfg.shading            = 'flat' or 'interp' (default = 'flat')  
          cfg.comment            = 'no', 'auto' or 'xlim' (default = 'auto')  
                                   'auto': date, xparam, yparam and parameter limits are printed  
                                   'xlim': only xparam limits are printed  
                                   'ylim': only yparam limits are printed  
          cfg.commentpos         = string or two numbers, position of the comment (default = 'leftbottom')  
                                   'lefttop' 'leftbottom' 'middletop' 'middlebottom' 'righttop' 'rightbottom'  
                                   'title' to place comment as title  
                                   'layout' to place comment as specified for COMNT in layout  
                                   [x y] coordinates  
          cfg.interactive        = Interactive plot 'yes' or 'no' (default = 'yes')  
                                   In a interactive plot you can select areas and produce a new  
                                   interactive plot when a selected area is clicked. Multiple areas  
                                   can be selected by holding down the SHIFT key.  
          cfg.directionality     = '', 'inflow' or 'outflow' specifies for  
                                   connectivity measures whether the inflow into a  
                                   node, or the outflow from a node is plotted. The  
                                   (default) behavior of this option depends on the dimor  
                                   of the input data (see below).  
          cfg.layout             = specify the channel layout for plotting using one of  
                                   the supported ways (see below).  
          cfg.interpolatenan     = string 'yes', 'no' (default = 'yes')  
                                   interpolate over channels containing NaNs  
         
        For the plotting of directional connectivity data the cfg.directionality  
        option determines what is plotted. The default value and the supported  
        functionality depend on the dimord of the input data. If the input data  
        is of dimord 'chan_chan_XXX', the value of directionality determines  
        whether, given the reference channel(s), the columns (inflow), or rows  
        (outflow) are selected for plotting. In this situation the default is  
        'inflow'. Note that for undirected measures, inflow and outflow should  
        give the same output. If the input data is of dimord 'chancmb_XXX', the  
        value of directionality determines whether the rows in data.labelcmb are  
        selected. With 'inflow' the rows are selected if the refchannel(s) occur in  
        the right column, with 'outflow' the rows are selected if the  
        refchannel(s) occur in the left column of the labelcmb-field. Default in  
        this case is '', which means that all rows are selected in which the  
        refchannel(s) occur. This is to robustly support linearly indexed  
        undirected connectivity metrics. In the situation where undirected  
        connectivity measures are linearly indexed, specifying 'inflow' or  
        'outflow' can result in unexpected behavior.  
         
        The layout defines how the channels are arranged. You can specify the  
        layout in a variety of ways:  
         - you can provide a pre-computed layout structure (see prepare_layout)  
         - you can give the name of an ascii layout file with extension *.lay  
         - you can give the name of an electrode file  
         - you can give an electrode definition, i.e. "elec" structure  
         - you can give a gradiometer definition, i.e. "grad" structure  
        If you do not specify any of these and the data structure contains an  
        electrode or gradiometer structure, that will be used for creating a  
        layout. If you want to have more fine-grained control over the layout  
        of the subplots, you should create your own layout file.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.inputfile   =  ...  
        If you specify this option the input data will be read from a *.mat  
        file on disk. This mat files should contain only a single variable named 'data',  
        corresponding to the input structure. For this particular function, the input should be  
        structured as a cell-array.  
         
        See also FT_TOPOPLOTER, FT_TOPOPLOTIC, FT_SINGLEPLOTTFR, FT_MULTIPLOTTFR, FT_PREPARE_LAYOUT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_topoplotTFR.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_topoplotTFR", *args, **kwargs)
