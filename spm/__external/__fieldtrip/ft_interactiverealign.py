from spm.__wrapper__ import Runtime


def ft_interactiverealign(*args, **kwargs):
    """
      FT_INTERACTIVEREALIGN allows the user to interactively translate, rotate and scale an  
        individual geometrical object to a template geometrical object. It can for example be used  
        to align EEG electrodes to a model of the scalp surface.  
         
        Use as  
          [cfg] = ft_interactiverealign(cfg)  
         
        The configuration structure should contain the individuals geometrical object that  
        has to be realigned  
          cfg.individual.elec           = structure, see FT_READ_SENS  
          cfg.individual.grad           = structure, see FT_READ_SENS  
          cfg.individual.opto           = structure, see FT_READ_SENS  
          cfg.individual.headmodel      = structure, see FT_PREPARE_HEADMODEL  
          cfg.individual.headshape      = structure, see FT_READ_HEADSHAPE  
          cfg.individual.mri            = structure, see FT_READ_MRI  
          cfg.individual.mesh           = structure, see FT_PREPARE_MESH  
        You can specify the style with which the objects are displayed using  
          cfg.individual.headmodelstyle = 'vertex', 'edge', 'surface' or 'both' (default = 'edge')  
          cfg.individual.headshapestyle = 'vertex', 'edge', 'surface' or 'both' (default = 'vertex')  
         
        The configuration structure should also contain the geometrical object of a  
        template that serves as target  
          cfg.template.axes             = string, 'yes' or 'no' (default = 'no')  
          cfg.template.elec             = structure, see FT_READ_SENS  
          cfg.template.grad             = structure, see FT_READ_SENS  
          cfg.template.opto             = structure, see FT_READ_SENS  
          cfg.template.headmodel        = structure, see FT_PREPARE_HEADMODEL  
          cfg.template.headshape        = structure, see FT_READ_HEADSHAPE  
          cfg.template.mri              = structure, see FT_READ_MRI  
          cfg.template.mesh             = structure, see FT_PREPARE_MESH  
        You can specify the style with which the objects are displayed using  
          cfg.template.headmodelstyle   = 'vertex', 'edge', 'surface' or 'both' (default = 'edge')  
          cfg.template.headshapestyle   = 'vertex', 'edge', 'surface' or 'both' (default = 'vertex')  
         
        You can specify one or multiple individual objects which will all be realigned and  
        one or multiple template objects.  
         
        See also FT_VOLUMEREALIGN, FT_ELECTRODEREALIGN, FT_DETERMINE_COORDSYS,  
        FT_READ_SENS, FT_READ_HEADMODEL, FT_READ_HEADSHAPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_interactiverealign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_interactiverealign", *args, **kwargs)
