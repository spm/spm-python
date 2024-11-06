from spm.__wrapper__ import Runtime


def ft_meshrealign(*args, **kwargs):
    """
      FT_MESHREALIGN rotates, translates and optionally scales a surface description of  
        the head or of the cortex. The different methods are described in detail below.  
         
        INTERACTIVE - This displays the mesh surface together with an anatomical MRI, with  
        a head model, with electrodes, with gradiometers, with optodes, or simply with the  
        axis of the coordinate system, and you manually (using the graphical user  
        interface) adjust the rotation, translation and scaling parameters.  
         
        FIDUCIAL - The coordinate system is updated according to the definition of the  
        coordinates of anatomical landmarks or fiducials that are specified in the  
        configuration. If the fiducials are not specified in the configuration, you will  
        have to click them in an interactive display of the mesh surface.  
         
        Use as  
          mesh = ft_meshrealign(cfg, mesh)  
        where the mesh input argument comes from FT_READ_HEADSHAPE or FT_PREPARE_MESH and  
        cfg is a configuration structure that should contain  
          cfg.method         = string, can be 'interactive' or fiducial' (default = 'interactive')  
          cfg.coordsys       = string specifying the origin and the axes of the coordinate  
                               system. Supported coordinate systems are 'ctf', '4d', 'bti',  
                               'eeglab', 'neuromag', 'itab', 'yokogawa', 'asa', 'acpc',  
                               and 'paxinos'. See http://tinyurl.com/ojkuhqz  
         
        When cfg.method = 'fiducial' and cfg.coordsys is based on external anatomical  
        landmarks, as is common for EEG and MEG, the following can be used to specify the  
        voxel indices of the fiducials:  
          cfg.fiducial.nas   = [x y z], position of nasion  
          cfg.fiducial.lpa   = [x y z], position of LPA  
          cfg.fiducial.rpa   = [x y z], position of RPA  
        The fiducials should be expressed in the same coordinates and units as the input  
        mesh. If the fiducials are not specified in the configuration, the mesh is  
        displayed and you have to click on the fidicuals.  
         
        When cfg.method = 'fiducial' you can specify  
          cfg.mri            = structure, see FT_READ_MRI  
          cfg.headmodel      = structure, see FT_PREPARE_HEADMODEL  
          cfg.elec           = structure, see FT_READ_SENS  
          cfg.grad           = structure, see FT_READ_SENS  
          cfg.opto           = structure, see FT_READ_SENS  
        If none of these is specified, the x-, y- and z-axes will be shown.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_READ_HEADSHAPE, FT_PREPARE_MESH, FT_ELECTRODEREALIGN, FT_VOLUMEREALIGN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_meshrealign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_meshrealign", *args, **kwargs)
