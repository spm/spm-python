from spm._runtime import Runtime


def _fixdimord(*args, **kwargs):
    r"""
      FIXDIMORD ensures consistency between the dimord string and the axes  
        that describe the data dimensions. The main purpose of this function  
        is to ensure backward compatibility of all functions with data that has  
        been processed by older FieldTrip versions.  
         
        Use as  
          [data] = fixdimord(data)  
        This will modify the data.dimord field to ensure consistency.  
        The name of the axis is the same as the name of the dimord, i.e. if  
        dimord='freq_time', then data.freq and data.time should be present.  
         
        The default dimensions in the data are described by  
         'time'  
         'freq'  
         'chan'  
         'chancmb'  
         'refchan'  
         'subj'  
         'rpt'  
         'rpttap'  
         'pos'  
         'ori'  
         'rgb'  
         'comp'  
         'voxel'  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/fixdimord.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixdimord", *args, **kwargs)
