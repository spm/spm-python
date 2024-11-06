from spm.__wrapper__ import Runtime


def ft_trialfun_brainvision_segmented(*args, **kwargs):
    """
      FT_TRIALFUN_BRAINVISION_SEGMENTED creates trials for a Brain Vision Analyzer  
        dataset that was segmented in the BVA software.  
         
        Use this function by calling   
          [cfg] = ft_definetrial(cfg)  
        where the configuration structure should contain  
          cfg.dataset  = string with the filename  
          cfg.trialfun = 'ft_trialfun_brainvision_segmented'  
         
        Optionally, you can specify:  
          cfg.stimformat = 'S %d'  
          
        The stimformat instruct this function to parse stimulus triggers according to  
        the specific format. The default is 'S %d'. The cfg.stimformat always  
        needs to contain exactly one %d code. The trigger values parsed in this way  
        will be stored in columns 4 and upwards of the output 'trl' matrix, and  
        after FT_PREPROCESSING will end up in data.trialinfo.  
         
        A BrainVision dataset consists of three files: an .eeg, .vhdr, and a .vmrk   
        file. The option cfg.dataset should refer to the .vhdr file.  
         
        See also FT_DEFINETRIAL, FT_PREPROCESSING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_brainvision_segmented.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_brainvision_segmented", *args, **kwargs)
