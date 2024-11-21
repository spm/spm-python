from spm.__wrapper__ import Runtime


def ft_geometryplot(*args, **kwargs):
    """
      FT_GEOMETRYPLOT plots objects in 3D, such as sensors, headmodels, sourcemodels,  
        headshapes, meshes, etcetera. It provides an easy-to-use wrapper for the  
        corresponding FT_PLOT_XXX functions.  
         
        Use as  
          ft_geometryplot(cfg)  
        where the cfg structure contains the geometrical objects that have to be plotted  
          cfg.elec              = structure, see FT_READ_SENS  
          cfg.grad              = structure, see FT_READ_SENS  
          cfg.opto              = structure, see FT_READ_SENS  
          cfg.headshape         = structure, see FT_READ_HEADSHAPE  
          cfg.headmodel         = structure, see FT_PREPARE_HEADMODEL and FT_READ_HEADMODEL  
          cfg.sourcemodel       = structure, see FT_PREPARE_SOURCEMODEL  
          cfg.dipole            = structure, see FT_DIPOLEFITTING  
          cfg.mri               = structure, see FT_READ_MRI  
          cfg.mesh              = structure, see FT_PREPARE_MESH  
          cfg.axes              = string, 'yes' or 'no' (default = 'no')  
         
        Furthermore, there are a number of general options  
          cfg.unit              = string, 'mm', 'cm', 'm' with the geometrical units (default depends on the data)  
          cfg.coordsys          = string, with the coordinate system (default depends on the data)  
          cfg.figure            = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.figurename        = string, title of the figure window  
          cfg.position          = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer          = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO. The OpenGL renderer is required when using opacity (default = 'opengl')  
          cfg.title             = string, title of the plot  
         
        You can specify the style with which the objects are displayed using  
          cfg.elecstyle         = cell-array or structure, see below  
          cfg.gradstyle         = cell-array or structure, see below  
          cfg.optostyle         = cell-array or structure, see below  
          cfg.headshapestyle    = cell-array or structure, see below  
          cfg.headmodelstyle    = cell-array or structure, see below  
          cfg.sourcemodelstyle  = cell-array or structure, see below  
          cfg.dipolestyle       = cell-array or structure, see below  
          cfg.mristyle          = cell-array or structure, see below  
          cfg.meshstyle         = cell-array or structure, see below  
         
        For each of the xxxstyle options, you can specify a cell-array with key value pairs  
        similar as in FT_INTERACTIVEREALIGN. These options will be passed on to the  
        corresponding FT_PLOT_XXX function. You can also specify the options as a  
        structure. For example, the following two specifications are equivalent  
          cfg.headshapestyle = {'facecolor', 'skin', 'edgecolor', 'none'};  
        and  
          cfg.headshapestyle.facecolor = 'skin';  
          cfg.headshapestyle.edgecolor = 'none';  
         
        In the figure with graphical user interface you will be able to adjust most of the  
        settings that determine how the objects are displayed.  
         
        See also PLOTTING, FT_SOURCEPLOT, FT_INTERACTIVEREALIGN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_geometryplot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_geometryplot", *args, **kwargs)
