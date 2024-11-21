from spm.__wrapper__ import Runtime


def ft_prepare_montage(*args, **kwargs):
    """
      FT_PREPARE_MONTAGE creates a referencing scheme based on the input configuration  
        options and the channels in the data structure. The resulting montage can be  
        given as input to FT_APPLY_MONTAGE, or as cfg.montage to FT_PREPROCESSING.  
         
        Use as  
          montage = ft_prepare_montage(cfg, data)  
         
        The configuration can contain the following fields:  
          cfg.refmethod     = 'avg', 'comp', 'bipolar', 'laplace', 'doublebanana', 'longitudinal', 'circumferential', 'transverse' (default = 'avg')  
          cfg.implicitref   = string with the label of the implicit reference, or empty (default = [])  
          cfg.refchannel    = cell-array with new EEG reference channel(s), this can be 'all' for a common average reference  
          cfg.groupchans    = 'yes' or 'no', should channels be rereferenced in separate groups  
                              for bipolar and laplace methods, this requires channnels to be  
                              named using an alphanumeric code, where letters represent the  
                              group and numbers represent the order of the channel whithin  
                              its group (default = 'no')  
         
        The implicitref option allows adding the implicit reference channel to the data as  
        a channel with zeros.  
         
        The resulting montage is a structure with the fields  
          montage.tra      = MxN matrix  
          montage.labelold = Nx1 cell-array  
          montage.labelnew = Mx1 cell-array  
         
        As an example, an output bipolar montage could look like this  
          bipolar.labelold  = {'1',   '2',   '3',   '4'}  
          bipolar.labelnew  = {'1-2', '2-3', '3-4'}  
          bipolar.tra       = [  
            +1 -1  0  0  
             0 +1 -1  0  
             0  0 +1 -1  
          ];  
         
        See also FT_PREPROCESSING, FT_APPLY_MONTAGE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_prepare_montage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_prepare_montage", *args, **kwargs)
