from spm.__wrapper__ import Runtime


def ft_layoutplot(*args, **kwargs):
    """
      FT_LAYOUTPLOT makes a figure with the 2-D layout of the channel positions  
        for topoplotting and the individual channel axes (i.e. width and height  
        of the subfigures) for multiplotting. A correct 2-D layout is a  
        prerequisite  for plotting the topographical distribution of the  
        potential or field distribution, or for plotting timecourses in a  
        topographical arrangement.  
         
        This function uses the same configuration options as prepare_layout and  
        as the topoplotting and multiplotting functions. The difference is that  
        this function plots the layout without any data, which facilitates  
        the validation of your 2-D layout.  
         
        Use as  
          ft_layoutplot(cfg, data)  
         
        There are several ways in which a 2-D layout can be made: it can be read  
        directly from a *.lay file, it can be created based on 3-D electrode or  
        gradiometer positions in the configuration or in the data, or it can be  
        created based on the specification of an electrode of gradiometer file.  
         
        You can specify either one of the following configuration options  
          cfg.layout      = filename containg the layout  
          cfg.rotate      = number, rotation around the z-axis in degrees (default = [], which means automatic)  
          cfg.projection  = string, 2D projection method can be 'stereographic', 'ortographic', 'polar', 'gnomic' or 'inverse' (default = 'orthographic')  
          cfg.elec        = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad        = structure with gradiometer definition or filename, see FT_READ_SENS  
          cfg.opto        = structure with optode definition or filename, see FT_READ_SENS  
          cfg.output      = filename to which the layout will be written (default = [])  
          cfg.montage     = 'no' or a montage structure (default = 'no')  
          cfg.image       = filename, use an image to construct a layout (e.g. usefull for ECoG grids)  
          cfg.box         = string, 'yes' or 'no' whether box should be plotted around electrode (default = 'yes')  
          cfg.mask        = string, 'yes' or 'no' whether the mask should be plotted (default = 'yes')  
          cfg.visible     = string, 'on' or 'off' whether figure will be visible (default = 'on')  
          cfg.figure      = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.position    = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer    = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO (default is automatic, try 'painters' when it crashes)  
         
        Alternatively the layout can be constructed from either  
          data.elec     structure with electrode positions  
          data.grad     structure with gradiometer definition  
         
        Alternatively, you can specify  
          cfg.layout = 'ordered'  
        which will give you a 2-D ordered layout. Note that this is only suited  
        for multiplotting and not for topoplotting.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
        If you specify this option the input data will be read from a *.mat  
        file on disk. This mat files should contain only a single variable named 'data',  
        corresponding to the input structure.  
         
        See also FT_PREPARE_LAYOUT, FT_TOPOPLOTER, FT_TOPOPLOTTFR, FT_MULTIPLOTER, FT_MULTIPLOTTFR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_layoutplot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_layoutplot", *args, **kwargs)
