from spm.__wrapper__ import Runtime


def _rollback_provenance(*args, **kwargs):
    """
      ROLLBACK_PROVENANCE rolls the provenance one step back and should  
        be used whenever a FT function calls another FT function without  
        the user being (or having to be) aware of this.  
         
        Some examples for use  
         
          tmpcfg            = [];  
          tmpcfg.downsample = cfg.downsample;  % simply copy this option  
          tmpcfg.smooth     = 'no';            % override the default for this option  
          mri = ft_volumedownsample(tmpcfg, mri);  
          [cfg, mri] = rollback_provenance(cfg, mri);  
         
          tmpcfg           = [];  
          tmpcfg.parameter = cfg.parameter;  
          [varargin{:}] = ft_selectdata(tmpcfg, varargin{:});  
          [cfg, varargin{:}] = rollback_provenance(cfg, varargin{:});  
         
        See also FT_PREAMBLE, FT_POSTAMBLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/rollback_provenance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("rollback_provenance", *args, **kwargs)
