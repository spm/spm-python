from spm.__wrapper__ import Runtime


def _offset2time(*args, **kwargs):
    """
      OFFSET2TIME converts the offset of a trial definition into a time-axis  
        according to the definition from DEFINETRIAL  
         
        Use as  
          [time] = offset2time(offset, fsample, nsamples)  
         
        The trialdefinition "trl" is an Nx3 matrix. The first column contains  
        the sample-indices of the begin of the trial relative to the begin  
        of the raw data , the second column contains the sample_indices of  
        the end of the trials, and the third column contains the offset of  
        the trigger with respect to the trial. An offset of 0 means that  
        the first sample of the trial corresponds to the trigger. A positive  
        offset indicates that the first sample is later than the trigger, a  
        negative offset indicates a trial beginning before the trigger.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/offset2time.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("offset2time", *args, **kwargs)
