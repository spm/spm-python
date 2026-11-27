from spm._runtime import Runtime


def spm_mac_permissions(*args, **kwargs):
    r"""
      SPM_MAC_PERMISSIONS Helper to fix macOS quarantine issues (Gatekeeper)  
         
        This function detects if SPM's MEX files are tainted with the macOS  
        "com.apple.quarantine" attribute (common when downloading ZIPs from the  
        web). If detected, it attempts to self-repair by removing the attribute.  
         
        This function is called automatically at startup by spm.m.  
       __________________________________________________________________________  
        Copyright (C) 2024 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mac_permissions.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mac_permissions", *args, **kwargs, nargout=0)
