from spm.__wrapper__ import Runtime


def ft_electrodeplacement(*args, **kwargs):
    """
      FT_ELECTRODEPLACEMENT allows manual placement of electrodes on a MRI scan, CT scan  
        or on a triangulated surface of the head. This function supports different methods.  
         
        VOLUME - Navigate an orthographic display of a volume (e.g. CT or MRI scan), and  
        assign an electrode label to the current crosshair location by clicking on a label  
        in the eletrode list. You can undo the selection by clicking on the same label  
        again. The electrode labels shown in the list can be prespecified using cfg.channel  
        when calling ft_electrodeplacement. The zoom slider allows zooming in at the  
        location of the crosshair. The intensity sliders allow thresholding the image's low  
        and high values. The magnet feature transports the crosshair to the nearest peak  
        intensity voxel, within a certain voxel radius of the selected location. The labels  
        feature displays the labels of the selected electrodes within the orthoplot. The  
        global feature allows toggling the view between all and near-crosshair  
        markers. The scan feature allows toggling between scans when another scan  
        is given as input.  
         
        HEADSHAPE - Navigate a triangulated scalp (for EEG) or brain (for ECoG) surface,  
        and assign an electrode location by clicking on the surface. The electrode is  
        placed on the triangulation itself.  
         
        1020 - Starting from a triangulated scalp surface and the nasion, inion, left and  
        right pre-auricular points, this automatically constructs and follows contours over  
        the surface according to the 5% system. Electrodes are placed at certain relative  
        distances along these countours. This is an extension of the 10-20 standard  
        electrode placement system and includes the 20%, 10% and 5% locations. See  
        "Oostenveld R, Praamstra P. The five percent electrode system for high-resolution  
        EEG and ERP measurements. Clin Neurophysiol. 2001 Apr;112(4):713-9" for details.  
         
        SHAFT - This is for placing electrodes along a linear sEEG shaft. The tip of the  
        shaft corresponding to the first electrode, another point along the shaft, and the  
        distance between the electrodes should be specified. If the shaft is not straight  
        but curved, you should specify multiple (at least two) points along the shaft,  
        i.e., specify cfg.shaft.along as an Nx3 array for N points along the shaft. The  
        number of electrodes to be distributed along the shaft is determined from cfg.channel.  
         
        GRID - This is for placing electrodes on a regular MxN ECoG grid. Each of the four  
        cornerpoints of the grid must be specified, along with the dimensions of the grid.  
        Following piecewise linear placement of the electrodes on the grid, you can use  
        FT_ELECTRODEREALIGN with cfg.method='project' to project them to the curved brain  
        surface.  
         
        Use as  
          [elec] = ft_electrodeplacement(cfg, mri)  
          [elec] = ft_electrodeplacement(cfg, ct)  
          [elec] = ft_electrodeplacement(cfg, mri, ct, ..)  
        where the second and subsequent input arguments should be one or multiple  
        anatomical MRIs and/or CTs, or  
          [elec] = ft_electrodeplacement(cfg, headshape)  
        where the input headshape should be a surface triangulation.  
         
        The configuration can contain the following options  
          cfg.method         = string representing the method for placing the electrodes  
                               'volume'          interactively locate electrodes on three orthogonal slices of a volumetric MRI or CT scan  
                               'headshape'       interactively locate electrodes on a head surface  
                               '1020'            automatically locate electrodes on a head surface according to the 10-20 system  
                               'shaft'           automatically locate electrodes along a linear sEEG shaft  
                               'grid'            automatically locate electrodes on a MxN ECoG grid  
          cfg.figure         = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.position       = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer       = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO (default = 'opengl')  
         
        The following options apply to the 'volume' method  
          cfg.parameter      = string, field in data (default = 'anatomy' if present in data)  
          cfg.channel        = Nx1 cell-array with selection of channels (default = {'1' '2' ...})  
          cfg.elec           = struct containing previously placed electrodes (this overwrites cfg.channel)  
          cfg.clim           = color range of the data (default = [0 1], i.e. the full range)  
          cfg.magtype        = string representing the 'magnet' type used for placing the electrodes  
                               'peakweighted'    place electrodes at weighted peak intensity voxel (default)  
                               'troughweighted'  place electrodes at weighted trough intensity voxel  
                               'peak'            place electrodes at peak intensity voxel (default)  
                               'trough'          place electrodes at trough intensity voxel  
                               'weighted'        place electrodes at center-of-mass  
          cfg.magradius      = number representing the radius for the cfg.magtype based search (default = 3)  
         
        The following options apply to the '1020' method  
          cfg.fiducial.nas   = 1x3 vector with coordinates  
          cfg.fiducial.ini   = 1x3 vector with coordinates  
          cfg.fiducial.lpa   = 1x3 vector with coordinates  
          cfg.fiducial.rpa   = 1x3 vector with coordinates  
          cfg.feedback       = string, can be 'yes' or 'no' for detailed feedback (default = 'yes')  
         
        The following options apply to the 'shaft' method  
          cfg.shaft.tip      = 1x3 position of the electrode at the tip of the shaft  
          cfg.shaft.along    = 1x3 or Nx3 positions along the shaft  
          cfg.shaft.distance = scalar, distance between electrodes  
         
        The following options apply to the 'grid' method  
          cfg.grid.corner1   = 1x3 position of the upper left corner point  
          cfg.grid.corner2   = 1x3 position of the upper right corner point  
          cfg.grid.corner3   = 1x3 position of the lower left corner point  
          cfg.grid.corner4   = 1x3 position of the lower right corner point  
         
        In the interactive 'headshape' and 'volume' methods you can click once on an  
        already assigned electrode to jump to that electrode position and you can click  
        twice to remove the assigned electrode position.  
         
        See also FT_ELECTRODEREALIGN, FT_VOLUMEREALIGN, FT_VOLUMESEGMENT, FT_PREPARE_MESH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_electrodeplacement.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_electrodeplacement", *args, **kwargs)
