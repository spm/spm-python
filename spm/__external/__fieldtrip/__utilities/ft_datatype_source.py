from spm.__wrapper__ import Runtime


def ft_datatype_source(*args, **kwargs):
    """
      FT_DATATYPE_SOURCE describes the FieldTrip MATLAB structure for data that is  
        represented at the source level. This is typically obtained with a beamformer of  
        minimum-norm source reconstruction using FT_SOURCEANALYSIS.  
         
        An example of a source structure obtained after performing DICS (a frequency domain  
        beamformer scan) is shown here  
         
                  pos: [6732x3 double]       positions at which the source activity could have been estimated  
               inside: [6732x1 logical]      boolean vector that indicates at which positions the source activity was estimated  
                  dim: [xdim ydim zdim]      if the positions can be described as a 3D regular grid, this contains the  
                                              dimensionality of the 3D volume  
            cumtapcnt: [120x1 double]        information about the number of tapers per original trial  
                 time: 0.100                 the latency at which the activity is estimated (in seconds)  
                 freq: 30                    the frequency at which the activity is estimated (in Hz)  
                  pow: [6732x120 double]     the estimated power at each source position  
            powdimord: 'pos_rpt'             defines how the numeric data has to be interpreted,  
                                              in this case 6732 dipole positions x 120 repetitions (i.e. trials)  
                  cfg: [1x1 struct]          the configuration used by the function that generated this data structure  
         
        Required fields:  
          - pos  
         
        Optional fields:  
          - inside, pow, coh, eta, mom, ori, leadfield, filter, or any other field with dimensions that are consistent with pos or dim  
          - dim, transform, unit, coordsys, time, freq, cumtapcnt, dimord   
         
        Deprecated fields:  
          - method, outside  
         
        Obsoleted fields:  
          - xgrid, ygrid, zgrid, transform, latency, frequency  
         
        Revision history:  
         
        (2014) The subfields in the avg and trial fields are now present in the  
        main structure, e.g. source.avg.pow is now source.pow. Furthermore, the  
        inside is always represented as logical vector.  
         
        (2011) The source representation should always be irregular, i.e. not  
        a 3-D volume, contain a "pos" field and not contain a "transform".  
         
        (2010) The source structure should contain a general "dimord" or specific  
        dimords for each of the fields. The source reconstruction in the avg and  
        trial substructures has been moved to the toplevel.  
         
        (2007) The xgrid/ygrid/zgrid fields have been removed, because they are  
        redundant.  
         
        (2003) The initial version was defined  
         
        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP, FT_DATATYPE_FREQ,  
        FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, FT_DATATYPE_SPIKE,  
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_datatype_source.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype_source", *args, **kwargs)
