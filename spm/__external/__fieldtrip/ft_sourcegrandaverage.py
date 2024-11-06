from spm.__wrapper__ import Runtime


def ft_sourcegrandaverage(*args, **kwargs):
    """
      FT_SOURCEGRANDAVERAGE averages source reconstructions over either multiple  
        subjects or conditions. It computes the average and variance for all  
        known source parameters. The output can be used in FT_SOURCESTATISTICS  
        with the method 'parametric'.  
         
        Alternatively, it can construct an average for multiple input source  
        reconstructions in two conditions after randomly reassigning the  
        input data over the two conditions. The output then can be used in  
        FT_SOURCESTATISTICS with the method 'randomization' or 'randcluster'.  
         
        The input source structures should be spatially alligned to each other  
        and should have the same positions for the sourcemodel.  
         
        Use as  
         [grandavg] = ft_sourcegrandaverage(cfg, source1, source2, ...)  
         
        where the source structures are obtained from FT_SOURCEANALYSIS or  
        from FT_VOLUMENORMALISE, and the configuration can contain the  
        following fields:  
          cfg.parameter          = string, describing the functional data to be processed, e.g. 'pow', 'nai' or 'coh'  
          cfg.keepindividual     = 'no' or 'yes'  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure. For this particular function, the input data  
        should be structured as a single cell-array.  
         
        See also FT_SOURCEANALYSIS, FT_SOURCEDESCRIPTIVES, FT_SOURCESTATISTICS, FT_MATH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourcegrandaverage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sourcegrandaverage", *args, **kwargs)
