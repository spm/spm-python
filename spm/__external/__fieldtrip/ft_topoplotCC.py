from spm.__wrapper__ import Runtime


def ft_topoplotCC(*args, **kwargs):
    """
      FT_TOPOPLOTCC plots the coherence or connectivity between channel pairs  
         
        Use as  
         ft_topoplotCC(cfg, freq)  
         
        The configuration should contain:  
          cfg.feedback      = string (default = 'textbar')  
          cfg.layout        = specification of the layout, see FT_PREPARE_LAYOUT  
          cfg.foi           = the frequency of interest which is to be plotted (default is the first frequency bin)  
          cfg.widthparam    = string, parameter to be used to control the line width (see below)  
          cfg.alphaparam    = string, parameter to be used to control the opacity (see below)  
          cfg.colorparam    = string, parameter to be used to control the line color  
          cfg.visible       = string, 'on' or 'off' whether figure will be visible (default = 'on')  
          cfg.figure        = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.position      = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer      = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO (default is automatic, try 'painters' when it crashes)  
         
        The widthparam should be indicated in pixels, e.g. usefull numbers are 1 and  
        larger.  
         
        The alphaparam should be indicated as opacity between 0 (fully transparent)  
        and 1 (fully opaque).  
         
        The default is to plot the connections as lines, but you can also use  
        bidirectional arrows:  
           cfg.arrowhead    = string, 'none', 'stop', 'start', 'both' (default = 'none')  
           cfg.arrowsize    = scalar, size of the arrow head in figure units,  
                              i.e. the same units as the layout (default is automatically determined)  
           cfg.arrowoffset  = scalar, amount that the arrow is shifted to the side in figure units,  
                              i.e. the same units as the layout (default is automatically determined)  
           cfg.arrowlength  = scalar, amount by which the length is reduced relative to the complete line (default = 0.8)  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
        If you specify this option the input data will be read from a *.mat  
        file on disk. This mat files should contain only a single variable named 'data',  
        corresponding to the input structure. For this particular function, the input should be  
        structured as a cell-array.  
         
        See also FT_PREPARE_LAYOUT, FT_MULTIPLOTCC, FT_CONNECTIVITYPLOT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_topoplotCC.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_topoplotCC", *args, **kwargs)
