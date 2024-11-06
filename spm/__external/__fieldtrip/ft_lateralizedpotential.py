from spm.__wrapper__ import Runtime


def ft_lateralizedpotential(*args, **kwargs):
    """
      FT_LATERALIZEDPOTENTIAL computes lateralized potentials such as the  
        lateralized readiness potential (LRP)  
         
        Use as  
          [lrp] = ft_lateralizedpotential(cfg, avgL, avgR)  
         
        where the input datasets should come from FT_TIMELOCKANALYSIS  
        and the configuration should contain  
          cfg.channelcmb = Nx2 cell-array  
         
        An example channelcombination containing the homologous channels  
        in the 10-20 standard system is  
           cfg.channelcmb = {'Fp1'   'Fp2'  
                             'F7'    'F8'  
                             'F3'    'F4'  
                             'T7'    'T8'  
                             'C3'    'C4'  
                             'P7'    'P8'  
                             'P3'    'P4'  
                             'O1'    'O2'}  
         
        The lateralized potential is computed on combinations of channels and  
        not on indivudual channels. However, if you want to make a topographic  
        plot with e.g. FT_MULTIPLOTER, you can replace the output lrp.label  
        with lrp.plotlabel.  
         
        The concept for the LRP was introduced approximately simultaneously in the  
        following two papers  
        - M. G. H. Coles. Modern mind-brain reading - psychophysiology,  
          physiology, and cognition. Psychophysiology, 26(3):251-269, 1988.  
        - R. de Jong, M. Wierda, G. Mulder, and L. J. Mulder. Use of  
          partial stimulus information in response processing. J Exp Psychol  
          Hum Percept Perform, 14:682-692, 1988.  
        and it is discussed in detail on a technical level in  
        - R. Oostenveld, D.F. Stegeman, P. Praamstra and A. van Oosterom.  
          Brain symmetry and topographic analysis of lateralized event-related  
          potentials. Clin Neurophysiol. 114(7):1194-202, 2003.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_TIMELOCKANALYSIS, FT_MULTIPLOTER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_lateralizedpotential.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_lateralizedpotential", *args, **kwargs)
