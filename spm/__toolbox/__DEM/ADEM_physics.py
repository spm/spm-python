from spm._runtime import Runtime


def ADEM_physics(*args, **kwargs):
    r"""
      % This routine illustrates the application of Variational Laplace to the  
        triple-estimation (DEM) problem; namely inferring the latent states and  
        causes of a dynamical system while learning the parameters and  
        precisions. The example is chosen to highlight complementary ways of  
        dealing with random (unknown) variables that change slowly. Here, these  
        variables include the attribute of various objects (which are inferred as  
        latent causes) and the parameters underwriting their dynamics (which are  
        learned). The example in question is a simple Atari-like game but  
        expressed in continuous (generalised) coordinates of motion.  
          
        To illustrate how one can equip DEM with action (i.e., implement an  
        elementary form of active inference) it considers the problem of using a  
        (red) bat to repel a (blue) ball, in the presence of other (green)  
        objects. The dynamics underlying this behaviour are based upon  
        straightforward classical mechanics, in which interactions amongst  
        objects are parameterised with coupling parameters that have to be  
        learned.  
          
        In what follows, we first set up the generative process and accompanying  
        model. By exposing the scheme to the initial conditions (that evolve very  
        slowly) the location and attributes of objects are then inferred to  
        provide precise posteriors over latent causes of (visual) input. These  
        posteriors and then used to learn the (coupling) parameters of the  
        generative model that capture the interactions between the bat and ball.  
        These dynamics are learned in the absence of action. Finally, we enable  
        action such that the inference and learning scheme controls the ball by  
        fulfilling its predictions under what it has previously learned. This  
        results in the emergence of a nonequilibrium steady-state, here,  
        quasi-periodic orbits that inherit from the physics of the generative  
        model  
          
        The likelihood mapping from latent states generates visual input using a  
        simple convolution model, in which each (Gaussian) object of an inferred  
        size is convolved with (Gaussian) receptive fields. For biomimetic  
        reasons, these receptive fields are larger at the periphery of vision.  
        And can be regarded as an implementation of spatial basis functions  
        mapping from object location to the (TrueColour) amplitude of place-coded  
        responses: c.f., retinotopic map or a downsampled image after  
        (anisotropic) convolution with receptive field kernels. The contributions  
        of different wavelengths are generated following a softmax operator that  
        stands in for a normalisation implicit in Weber's law. Despite these  
        nonlinearities, model inversion can still proceed using local  
        linearisation as in extended Kalman-Bucy filters. It should be noted,  
        however, that changing any of the model parameters will preclude  
        convergence, illustrating the failure Variational Laplace under brittle,  
        nonlinear models. On the other hand, with the right parameterisation, the  
        ensuing scheme illustrates the simplicity of specifying and inverting  
        such models with just one inversion scheme (here, spm_ADEM).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_physics.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_physics", *args, **kwargs, nargout=0)
