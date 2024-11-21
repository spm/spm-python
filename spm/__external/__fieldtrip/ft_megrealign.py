from spm.__wrapper__ import Runtime


def ft_megrealign(*args, **kwargs):
    """
      FT_MEGREALIGN interpolates MEG data towards standard gradiometer locations by  
        projecting the individual timelocked data towards a coarse source reconstructed  
        representation and computing the magnetic field on the standard gradiometer  
        locations.  
         
        Use as  
          [interp] = ft_megrealign(cfg, data)  
        where the input data corresponds to the output from FT_PREPROCESSING.  
         
        Required configuration options are  
          cfg.template  
          cfg.inwardshift  
         
        The new gradiometer definition is obtained from a template dataset,  
        or can be constructed by averaging the gradiometer positions over  
        multiple datasets.  
          cfg.template       = single dataset that serves as template  
          cfg.template(1..N) = datasets that are averaged into the standard  
         
        The realignment is done by computing a minumum norm estimate using a  
        large number of dipoles that are placed in the upper layer of the brain  
        surface, followed by a forward computation towards the template  
        gradiometer array. This requires the specification of a volume conduction  
        model of the head and of a source model.  
         
        A volume conduction model of the head should be specified with  
          cfg.headmodel   = structure, see FT_PREPARE_HEADMODEL  
         
        A source model (i.e. a superficial layer with distributed sources) can be  
        constructed from a headshape file, or from inner surface of the volume conduction  
        model using FT_PREPARE_SOURCEMODEL using the following options  
          cfg.spheremesh  = number of dipoles in the source layer (default = 642)  
          cfg.inwardshift = depth of the source layer relative to the headshape  
                            surface or volume conduction model (no default  
                            supplied, see below)  
          cfg.headshape   = a filename containing headshape, a structure containing a  
                            single triangulated boundary, or a Nx3 matrix with surface  
                            points  
         
        If you specify a headshape and it describes the skin surface, you should specify an  
        inward shift of 2.5 cm.  
         
        For a single-sphere or a local-spheres volume conduction model based on the skin  
        surface, an inward shift of 2.5 cm is reasonable.  
         
        For a single-sphere or a local-spheres volume conduction model based on the brain  
        surface, you should probably use an inward shift of about 1 cm.  
         
        For a realistic single-shell volume conduction model based on the brain surface, you  
        should probably use an inward shift of about 1 cm.  
         
        Other configuration options are  
          cfg.tolerance  = tolerance ratio for leadfield matrix inverse based on a truncated svd,  
                           reflects the relative magnitude of the largest singular value  
                           to retain (default =s 1e-3)  
          cfg.verify     = 'yes' or 'no', show the percentage difference (default = 'yes')  
          cfg.feedback   = 'yes' or 'no' (default = 'no')  
          cfg.channel    =  Nx1 cell-array with selection of channels (default = 'MEG'),  
                            see FT_CHANNELSELECTION for details  
          cfg.trials     = 'all' or a selection given as a 1xN vector (default = 'all')  
         
        This implements the method described by T.R. Knosche, Transformation  
        of whole-head MEG recordings between different sensor positions.  
        Biomed Tech (Berl). 2002 Mar;47(3):59-62. For more information and  
        related methods, see Stolk et al., Online and offline tools for head  
        movement compensation in MEG. NeuroImage, 2012.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_PREPARE_LOCALSPHERES, FT_PREPARE_SINGLESHELL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_megrealign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_megrealign", *args, **kwargs)
