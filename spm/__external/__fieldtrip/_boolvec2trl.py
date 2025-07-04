from spm._runtime import Runtime


def _boolvec2trl(*args, **kwargs):
    """
      BOOLVEC2TRL converts between two representations of events or trials.  
         
        FieldTrip uses a number of representations for events that are conceptually very similar  
          event    = structure with type, value, sample, duration and offset  
          trl      = Nx3 numerical array with begsample, endsample, offset  
          trl      = table with 3 columns for begsample, endsample, offset  
          artifact = Nx2 numerical array with begsample, endsample  
          artifact = table with 2 columns for begsample, endsample  
          boolvec  = 1xNsamples boolean vector with a thresholded TTL/trigger sequence  
          boolvec  = MxNsamples boolean matrix with a thresholded TTL/trigger sequence  
         
        If trl or artifact are represented as a MATLAB table, they can have additional  
        columns. These additional columns have to be named and are not restricted to  
        numerical values.  
         
        This function makes a trial definition from a Boolean vector, or a cell-array  
        of trial definitions from a Boolean matrix.  
         
        See also ARTIFACT2BOOLVEC, ARTIFACT2EVENT, ARTIFACT2TRL, BOOLVEC2ARTIFACT, BOOLVEC2EVENT, BOOLVEC2TRL, EVENT2ARTIFACT, EVENT2BOOLVEC, EVENT2TRL, TRL2ARTIFACT, TRL2BOOLVEC, TRL2EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/boolvec2trl.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("boolvec2trl", *args, **kwargs)
