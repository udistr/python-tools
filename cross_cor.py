import numpy as np

def cross_cor(x,y,maxlag,normalize=1):
  """cross correlation

  Parameters
  ----------
  x : array_like
      First variable
  y : array_like
      Second variable
  maxlag : scalar
      The lag range
  normalize : scalar
      1 - normalize the correlations to [-1,1] range.
      0 - do not normalize
 Returns
 -------
  out: cross correlation for -maxlag:maxlag range. Negative lag 
       corespond to x leading y.
  """
  dims=x.shape
  if len(dims)==1:
    corr=np.zeros(2*maxlag+1)
  else:
    corr=np.zeros(np.append(2*maxlag+1,dims[1:]))

  T=dims[0]

  if normalize==1:

    for i in range(-maxlag,+maxlag+1):
      #print(i)

      if i<0:
        corr[i+maxlag]=np.mean((x[0:T+i]-np.mean(x[0:T+i],0))*(y[-i:]-np.mean(y[-i:],0)),0) \
                        /(np.std(x[0:T+i],0)*np.std(y[-i:],0))
      else:
        corr[i+maxlag]=np.mean((x[i:]-np.mean(x[i:],0))*(y[0:T-i]-np.mean(y[0:T-i],0)),0) \
                        /(np.std(x[i:],0)*np.std(y[0:T-i],0))

  elif normalize==0:

    for i in range(-maxlag,+maxlag+1):

      if i<0:
        corr[i+maxlag]=np.mean((x[0:T+i]-np.mean(x[0:T+i],0))*(y[-i:]-np.mean(y[-i:],0)),0)
      else:
        corr[i+maxlag]=np.mean((x[i:]-np.mean(x[i:],0))*(y[0:T-i]-np.mean(y[0:T-i],0)),0)

  else:

    for i in range(-maxlag,+maxlag+1):

      if i<0:
        corr[i+maxlag]=np.sum((x[0:T+i])*(y[-i:]),0)
      else:
        corr[i+maxlag]=np.sum((x[i:])*(y[0:T-i]),0)
        
  return corr
