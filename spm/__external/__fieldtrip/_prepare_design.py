from spm.__wrapper__ import Runtime


def _prepare_design(*args, **kwargs):
    """
      PREPARE_DESIGN makes a design matrix on the basis of the information in  
        cfg (i.c., cfg.statistic, cfg.ext, and an initial design in cfg.design)   
        and puts this design matrix in cfg.design. PREPARE_DESIGN also gives default  
        values for cfg.ivar, which specifies the independent variable, and cfg.uvar,   
        which specifies the units-of-observation.  
         
        PREPARE_DESIGN will be called from STATISTICS_WRAPPER whenever the user  
        has not specified the cfg.design field.  
         
        To construct the design matrix, PREPARE_DESIGN has to know whether   
        cfg.statistic is a statistic for a between- or a within-units   
        design. This is because, for the calculation of a statistic for a   
        within-units design, the unit-of-observation to which a particular  
        replication belongs has to be known. PREPARE_DESIGN determines the design  
        type (between or within) on the basis of cfg.statistic.  
         
        The design type has implications for how the data have to be passed to   
        PREPARE_DESIGN:  
        1. For a between-units design, by default, cfg.design is equal to the  
          last column of cfg.design. (If cfg.design is produced by  
          PREPARE_TIMEFREQDATA, and the varargin-argument of PREPARE_TIMEFREQDATA   
          contains one data set for every condition, then this column   
          contains the rank orders of these data sets.) This default   
          option can be overruled by cfg.ext, which contains an  
          external variable of order Nreplications X Nextvar. (Nextvar is the number of   
          external variables, and this can be larger that 1.) The order of the  
          replications is determined by the order of the data sets in varargin: the  
          replications in varargin{1} come first, followed by the replications  
          in varargin{2}, etc. In the case of multiple external variables, by specifying   
          cfg.ivar and cfg.cvar, the independent and the control variables can be specified.  
         
        2. For a within-units design, the default option is the following: (1)  
          the independent variable is equal to the last column of data.design,  
          and (2) the unit-variable is equal to the next-to-last column of  
          data.design. This default option only makes sense if the  
          varargin-argument of PREPARE_TIMEFREQDATA contains one data set for  
          every condition, and if the units in these data sets (subjects or  
          trials) correspond to each other. This default option can be overruled by   
          cfg.ext, which has order Nwcond X Nextvar or (Nunits*Nwcond) X Nextvar.  
          (Nwcond is the number of within-unit conditions.) The default option of   
          comparing all within-units conditions with each other can be overruled by   
          specifying 'ivar' and 'cvar'.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_design.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_design", *args, **kwargs)
