from spm.__wrapper__ import Runtime


def _resampledesign(*args, **kwargs):
    """
      RESAMPLEDESIGN returns a resampling matrix, in which each row can be  
        used to resample either the original design matrix or the original data.  
        The random resampling is done given user-specified constraints on the  
        experimental design, e.g. to swap within paired observations but not  
        between pairs.  
         
        Use as  
          [resample] = randomizedesign(cfg, design)  
        where the configuration can contain  
          cfg.resampling       = 'permutation' or 'bootstrap'  
          cfg.numrandomization = number (e.g. 300), can be 'all' in case of two conditions  
          cfg.ivar             = number or list with indices, independent variable(s)  
          cfg.uvar             = number or list with indices, unit variable(s)  
          cfg.wvar             = number or list with indices, within-cell variable(s)  
          cfg.cvar             = number or list with indices, control variable(s)  
         
        The "Independent variable" codes the condition number. Since the data is  
        assumed to be independent from the condition number any reshuffeling of  
        the condition number is allowed and ivar does NOT affect the resampling  
        outcome.  
         
        The "Unit of observation variable" corresponds to the subject number (in a  
        within-subject manipulation) or the trial number (in a within-trial  
        manipulation). It is best understood by considering that it corresponds  
        to the "pairing" of the data in a paired T-test or repeared measures  
        ANOVA. The uvar affects the resampling outcome in the way that only  
        resamplings within one unit of observation are returned (e.g. swap  
        conditions within a subject, not over subjects).  
         
        The "Within-cell variable" corresponds to the grouping of the data in  
        cells, where the multiple observations in a groups should not be broken  
        apart. This for example applies to multiple tapers in a spectral estimate  
        of a single trial of data (the "rpttap" dimension), where different  
        tapers should not be shuffled separately. Another example is a blocked  
        fMRI design, with a different condition in each block and multiple  
        repetitions of the same condition within a block. Assuming that there is  
        a slow HRF that convolutes the trials within a block, you can shuffle the  
        blocks but not the individual trials in a block.  
         
        The "Control variable" can be seen as the opposite from the within-cell  
        variable: it allows you to specify blocks in which the resampling should  
        be done, at the same time controlling that repetitions are not shuffled  
        between different control blocks.  
         
        See also FT_STATISTICS_MONTECARLO  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/resampledesign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("resampledesign", *args, **kwargs)
