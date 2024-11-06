from spm.__wrapper__ import Runtime


def _fixsource(*args, **kwargs):
    """
      FIXSOURCE converts old style source structures into new style source structures  
         
        Use as  
          output = fixsource(input)  
        where input is a structure representing source data  
         
        Typically, old style source structures contain source.avg.XXX or source.trial.XXX.   
        Furthermore. old style source structrures do not contain a dimord field.  
         
        The new style source structure contains:  
          source.pos       Nx3 list with source positions  
          source.dim       optional, if the list of positions describes a 3D volume  
          source.XXX       the old style subfields in avg/trial  
          source.XXXdimord string how to interpret the respective XXX field:  
         
        For example   
          source.pow             = zeros(Npos,Ntime)  
          source.powdimord       = 'pos_time'  
         
          source.mom             = cell(1,Npos)  
          source.mom{1}          = zeros(Nori,Nrpttap)  
          source.momdimord       = '{pos}_ori_rpttap'  
         
          source.leadfield       = cell(1,Npos)  
          source.leadfield{1}    = zeros(Nchan,Nori)  
          source.leadfielddimord = '{pos}_chan_ori'  
         
        See also FT_CHECKDATA, FIXVOLUME  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixsource.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fixsource", *args, **kwargs)
