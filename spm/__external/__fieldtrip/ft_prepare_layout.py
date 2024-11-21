from spm.__wrapper__ import Runtime


def ft_prepare_layout(*args, **kwargs):
    """
      FT_PREPARE_LAYOUT loads or creates a 2-D layout of the channel locations. This  
        layout is required for plotting the topographical distribution of the potential or  
        field distribution, or for plotting timecourses in a topographical arrangement.  
         
        Use as  
          layout = ft_prepare_layout(cfg)  
        or  
          layout = ft_prepare_layout(cfg, data)  
        where the optional data input argument is any of the FieldTrip data structures.  
         
        This returns a layout structure with the following elements  
          layout.pos     = Nx2 matrix with the position where each channel should be plotted  
          layout.label   = Nx1 cell-array with the channel labels  
          layout.width   = Nx1 vector with the width of each box for multiplotting  
          layout.height  = Nx1 vector with the height of each box for multiplotting  
          layout.mask    = optional cell-array with line segments that determine the area for topographic interpolation  
          layout.outline = optional cell-array with line segments that represent the head, nose, ears, sulci or other anatomical features  
          layout.color   = optional Nx3 matrix with rgb values for the channels' color, for fine-grained color behavior  
         
        There are several ways in which a 2-D layout can be made:  
        1) it can be read directly from a layout file  
        2) it can be created on basis of an image or photo,  
        3) it can be created from a projection of the 3-D sensor positions in the data, in the configuration, or in an electrode, gradiometer or optode file.  
         
        Layout files are MATLAB *.mat files containing a single structure representing the layout  
        (see above). The layout file can also be an ASCII file with the extension *.lay, although  
        this file format is no longer recommended, since there is less control over the outline  
        of the head and the mask within which the interpolation is done. A large number of  
        template layout files is provided in the fieldtrip/template/layout directory. See  
        also http://www.fieldtriptoolbox.org/template/layout  
         
        You can specify any one of the following configuration options  
          cfg.layout      = filename containg the input layout (*.mat or *.lay file), this can also be a layout  
                            structure, which is simply returned as-is (see below for details)  
          cfg.output      = filename (ending in .mat or .lay) to which the layout will be written (default = [])  
          cfg.feedback    = 'yes' or 'no', whether to show an image of the layout (default = 'no')  
          cfg.elec        = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad        = structure with gradiometer definition or filename, see FT_READ_SENS  
          cfg.opto        = structure with optode definition or filename, see FT_READ_SENS  
          cfg.rotate      = number, rotation around the z-axis in degrees (default = [], which means automatic)  
          cfg.center      = string, center and scale the electrodes in the sphere that represents the head, can be 'yes' or 'no' (default = 'no')  
          cfg.projection  = string, 2D projection method can be 'stereographic', 'orthographic', 'polar' or 'gnomic' (default = 'polar')  
                            When 'orthographic', cfg.viewpoint can be used to indicate to specificy projection (keep empty for legacy projection)  
          cfg.viewpoint   = string indicating the view point that is used for orthographic projection of 3-D sensor  
                            positions to the 2-D plane. The possible viewpoints are  
                            'left'      - left  sagittal view,     L=anterior, R=posterior, top=top, bottom=bottom  
                            'right'     - right sagittal view,     L=posterior, R=anterior, top=top, bottom=bottom  
                            'topleft'   - view from the top top,   L=anterior, R=posterior, top=top, bottom=bottom  
                            'topright'  - view from the top right, L=posterior, R=anterior, top=top, bottom=bottom  
                            'inferior'  - inferior axial view,     L=R, R=L, top=anterior, bottom=posterior  
                            'superior'  - superior axial view,     L=L, R=R, top=anterior, bottom=posterior  
                            'anterior'  - anterior  coronal view,  L=R, R=L, top=top, bottom=bottom  
                            'posterior' - posterior coronal view,  L=L, R=R, top=top, bottom=bottom  
                            'auto'      - automatic guess of the most optimal of the above  
                             tip: use cfg.viewpoint = 'auto' per iEEG electrode grid/strip/depth for more accurate results  
                             tip: to obtain an overview of all iEEG electrodes, choose superior/inferior, use cfg.headshape/mri, and plot using FT_LAYOUTPLOT with cfg.box/mask = 'no'  
          cfg.outline     = string, how to create the outline, can be 'circle', 'doublecirclecross', 'helmet', 'square', 'convex', 'headshape', 'mri' or 'no' (default is automatic)  
          cfg.mask        = string, how to create the mask, can be 'circle', 'extended', 'square', 'convex', 'headshape', 'mri' or 'no' (default is automatic)  
          cfg.headshape   = surface mesh (for example pial or head) to be used for generating an outline, see FT_READ_HEADSHAPE for details  
          cfg.mri         = segmented anatomical MRI to be used for generating an outline, see FT_READ_MRI and FT_VOLUMESEGMENT for details  
          cfg.montage     = 'no' or a montage structure (default = 'no')  
          cfg.image       = filename, use an image to construct a layout (useful for ECoG grids)  
          cfg.bw          = 'yes' or 'no', if an image is used and this option is true, the image is transformed in black and white (default = 'no', i.e. do not transform)  
          cfg.overlap     = string, how to deal with overlapping channels when the layout is constructed from a sensor configuration structure. This can be  
                            'shift'  - shift the positions in 2D space to remove the overlap (default)  
                            'keep'   - do not shift, retain the overlap  
                            'no'     - throw an error when overlap is present  
          cfg.channel     = 'all', or Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
          cfg.boxchannel  = 'all', or Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details  
                             specificies channels to use for determining channel box size (default = 'all', recommended for MEG/EEG, a selection is recommended for iEEG)  
          cfg.skipscale   = 'yes' or 'no', whether the scale should be included in the layout or not (default = 'no')  
          cfg.skipcomnt   = 'yes' or 'no', whether the comment should be included in the layout or not (default = 'no')  
          cfg.color       = empty, 'spatial', or Nx3 matrix, if non-empty, an Nx3 color matrix based on the position   
                            of the sensors will be added (default = [])  
         
        If you use cfg.headshape or cfg.mri to create a headshape outline, the input  
        geometry should be expressed in the same units and coordinate system as the input  
        sensors.  
         
        Alternatively the layout can be constructed from either one of these in the input data structure:  
          data.elec     = structure with electrode positions  
          data.grad     = structure with gradiometer definition  
          data.opto     = structure with optode definition  
         
        Alternatively you can specify the following options for systematic layouts which  
        will be generated for all channels present in the data. Note that these layouts are  
        only suitable for multiplotting, not for topoplotting.  
          cfg.layout = 'ordered'    will give you a NxN ordered layout  
          cfg.layout = 'vertical'   will give you a Nx1 ordered layout  
          cfg.layout = 'horizontal' will give you a 1xN ordered layout  
          cfg.layout = 'butterfly'  will give you a layout with all channels on top of each other  
          cfg.layout = 'circular'   will distribute the channels on a circle  
          cfg.width  = scalar (default is automatic)  
          cfg.height = scalar (default is automatic)  
         
        For an sEEG shaft the option cfg.layout='vertical' or 'horizontal' is useful to  
        represent the channels in a linear sequence . In this case you can also specify the  
        direction of the shaft as going from left-to-right, top-to-bottom, etc.  
          cfg.direction = string, can be any of 'LR', 'RL' (for horizontal), 'TB', 'BT' (for vertical)  
         
        For an ECoG grid the option cfg.layout='ordered' is useful to represent the  
        channels in a grid array. In this case you can also specify the number of rows  
        and/or columns and hwo the channels increment over the grid (e.g. first  
        left-to-right, then top-to-bottom). You can check the channel order of your grid  
        using FT_PLOT_LAYOUT.  
          cfg.rows      = number of rows (default is automatic)  
          cfg.columns   = number of columns (default is automatic)  
          cfg.direction = string, can be any of 'LRTB', 'RLTB', 'LRBT', 'RLBT', 'TBLR', 'TBRL', 'BTLR', 'BTRL' (default = 'LRTB')  
         
        See also FT_TOPOPLOTER, FT_TOPOPLOTTFR, FT_MULTIPLOTER, FT_MULTIPLOTTFR, FT_PLOT_LAYOUT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_prepare_layout.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_prepare_layout", *args, **kwargs)
