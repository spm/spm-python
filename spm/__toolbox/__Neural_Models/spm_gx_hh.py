from spm.__wrapper__ import Runtime


def spm_gx_hh(*args, **kwargs):
    """
      output for a single Hodgkin-Huxley like unit  
        FORMAT [y] = spm_gx_hh(x,u,P)  
         
        outputs  
       --------------------------------------------------------------------------  
        y(1) = V transmembrane potential mV (c.f. LFP)  
        y(2) = spike rate (Hz) = 1/PST  
        y(3) = dendritic energy = g(1)*x(1).*(V(1) - v).^2 + ... (mV.^2mS)  
       --------------------------------------------------------------------------  
         
        states  
       --------------------------------------------------------------------------  
        x(1) = proportion of open channels        % AMPA  
        x(2) = proportion of open channels        % GABA  
        x(3) = proportion of open channels        % K - slow  
        x(4) = proportion of open channels        % NMDA  
        x(5) = V                  % transmembrane potential mV  
        x(6) = t                  % time since last spike (peri-spike time)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_gx_hh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_hh", *args, **kwargs)
