from spm.__wrapper__ import Runtime


def FEP_self_entropy(*args, **kwargs):
  """  This demonstration uses an ensemble of particles with intrinsic (Lorentz  
    attractor) dynamics and (Newtonian) short-range coupling.  This routine  
    illustrates self organisation in terms of the entropy of blanket states  
    (and concomitant changes in terms of mutual information (i.e., complexity  
    cost or risk). Here, the ensemble average of these entropy measures is  
    taken over all (128) particles of macromolecules; where the Markov  
    blanket of each particle comprises all but the third (electrochemical)  
    hidden state. The graphics produced by this routine simply plot the  
    decrease in blanket entropy (and complexity cost) as the system  
    approaches its random dynamical attractor. Illustrative trajectories of  
    the particles are provided at three points during the (stochastic)  
    chaotic transient.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/FEP_self_entropy.m)
  """

  return Runtime.call("FEP_self_entropy", *args, **kwargs, nargout=0)
