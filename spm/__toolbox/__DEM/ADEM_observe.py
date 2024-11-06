from spm.__wrapper__ import Runtime


def ADEM_observe(*args, **kwargs):
    """
      This demo illustrates action-observation using synthetic writing under   
        active inference. It shows how expectations about hidden states can be   
        both cause and consequence of observed action (of self and others   
        respectively). We first illustrate the generation of behaviour using a   
        Lotka-Volterra form stable heteroclinic orbit. We then reproduce the   
        same forces on the agent's arm but switching off the precision of   
        proprioceptive inputs. This can be seen as attending selectively to   
        visual inputs. The resulting inference calls upon the same hidden-states   
        and implicit predictions (in a generalised or dynamic sense). These   
        simulations can be regarded as simulations of mirror neuron responses.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_observe.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_observe", *args, **kwargs, nargout=0)
